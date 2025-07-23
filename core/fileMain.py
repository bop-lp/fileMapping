import os.path
import traceback
from typing import Union, Tuple, Dict, List, Any

from fileMapping.core.Class import FilemappingDict
from fileMapping.core.abnormal import Mistake

from . import data, abnormal
from . import Class
from . import helperFunctions
from . import config as file_config
from . import decorators

from . import multithreading
from . import multiThreadedHelperFunctions

from . import wordProcessing
from . import fileImport
from . import parameterApplication


class File(data.File):
    def __init__(self, path: Union[str, list], config: dict, pluginConfig: Union[dict, str] = None):
        """

        :param path: 插件路径列表 必须为绝对路径
        :param config: fileMapping的配置
        :param pluginConfig: 这个插件的配置参数

        """
        super().__init__()

        if isinstance(path, str):
            # 兼容 str
            path = [path]

        # 加入内置插件的路径
        path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "builtInPlugins"))
        # 路径验证
        if helperFunctions.pathValidation(path if isinstance(path, (list, tuple)) else [path]):
            raise FileNotFoundError(f"不是一个有效的绝对路径。: '{path}'")

        _ = [helperFunctions.__fileFiltering__(i, file_config.screening) for i in path]
        listOfFiles = helperFunctions.dictMerge(*_)
        config = helperFunctions.deep_update(helperFunctions.configConvertTodict(file_config), config) \
            if config else helperFunctions.configConvertTodict(file_config)

        data.configData = data.ConfigData(config)
        self.config = data.configData
        self.path = path
        # 禁用插件 data.configData.disablePlugins
        listOfFiles = {
            key: value
            for key, value in listOfFiles.items()
            if not key in data.configData.disablePlugins
        }

        if self.config.get('multithreading', False):
            self.multithreading = multithreading.EnableMultithreading(
                self.config.numberOfThreads
            )
            self.plugInRunData = __multithreading__(self.multithreading, listOfFiles)

        else:
            self.plugInRunData = __singleThreaded__(listOfFiles)

        # self.plugInRunData.pluginConfig = getPluginConfig(pluginConfig)
        plugInConfiguration, errorMessage = getPluginConfig(pluginConfig)
        if errorMessage.__len__() != 0:
            # 配置错误
            # 记录错误信息
            self.logData.plugInConfiguration.extend(errorMessage)

        # 导入插件配置
        self.plugInRunData.pluginConfig = plugInConfiguration
        parameterApplication.ApplyParameter(self)

    def runOne(self, nameOfThePlugin: str, **kwargs):
        """
        运行特定的插件
        :param nameOfThePlugin: 插件名字
        :param kwargs: 运行参数
        :return:
        """
        if nameOfThePlugin in self.plugInRunData.callObject:
            self._run_(nameOfThePlugin, self.plugInRunData.callObject[nameOfThePlugin], **kwargs)

    def runAll(self, **kwargs):
        """
        运行所有插件
        :param kwargs: 运行参数
        :return:
        """
        for key, value in self.plugInRunData.callObject.items():
            self._run_(key, value, **kwargs)

    def _run_(self, theNameOfThePlugin: str, func: Class.Module, **kwargs) -> None:
        kwargs = {
            "fileMapping": self,
            **kwargs
        }
        returnValue = func.run(**kwargs)
        if isinstance(returnValue, abnormal.PackageRun):
            # 运行错误
            self.logData.fileMapping.append(returnValue)
            return

        self.returnValue[theNameOfThePlugin] = returnValue
        # 将返回值放入到


def __multithreading__(multithreading: Class.EnableMultithreading, listOfFiles: dict) -> Class.PlugInRunData:
    """
    多线程运行
    :return:
    """
    plugInData = Class.PlugInRunData({}, {}, {})

    # 读取文件 & 文本解析 & 排序插件
    run_order = multiThreadedHelperFunctions.file_read(multithreading, listOfFiles)
    run_order = multiThreadedHelperFunctions.text_parsing(multithreading, run_order)
    run_order = wordProcessing.sorting_plugin(run_order)
    if not isinstance(run_order, tuple):
        time_wrapper = decorators.TimeWrapper()
        info_wrapper = decorators.InfoWrapper(file_config.functions)
        for __level__, L in run_order.items():
            data = multiThreadedHelperFunctions.file_import(multithreading, fileImport.f, L, listOfFiles,
                                                wrapper_list=[time_wrapper.wrapper, info_wrapper.wrapper])

            for i in data:
                if isinstance(i, Class.Module):
                    packageName = i.packageName[:-3] if i.packageName.endswith(".py") else i.packageName
                    plugInData.callObject[packageName] = i
                    plugInData.invoke[packageName] = i.pack

                else:
                    # 运行错误
                    plugInData.moduleAbnormal.append(i)

        else:
            # 获取 时间 & 信息 -> information.run_time & file_info
            plugInData.information = Class.Information(time_wrapper.data, info_wrapper.data)

            return plugInData

    else:
        # sorting_plugin -> tuple 表示插件循环依赖
        raise abnormal.PluginLoopsDependencies(run_order)


def __singleThreaded__(listOfFiles: dict) -> Class.PlugInRunData:
    """
    单线程运行
    """
    plugInData = Class.PlugInRunData({}, {}, {})

    # 读取文件 & 文本解析 & 排序插件
    run_order = {}
    for i in listOfFiles:
        with open(listOfFiles[i], "r", encoding="utf-8") as f:
            run_order[i] = wordProcessing.get_all(f.read())

    run_order = wordProcessing.sorting_plugin(run_order)
    if not isinstance(run_order, tuple):
        time_wrapper = decorators.TimeWrapper()
        info_wrapper = decorators.InfoWrapper(file_config.functions)
        for __level__, L in run_order.items():
            for name in L:
                fileImport.f.__name__ = name
                try:
                    plugInData.callObject[name] = info_wrapper.wrapper(time_wrapper.wrapper(fileImport.f))(
                        listOfFiles[name])
                    plugInData.invoke[name] = plugInData.callObject[name].pack

                except abnormal.PackageImport as e:
                    # 导入错误
                    plugInData.moduleAbnormal.append(e)

        else:
            # 获取 时间 & 信息 -> information.run_time & file_info
            plugInData.information = Class.Information(time_wrapper.data, info_wrapper.data)
            return plugInData

    # sorting_plugin -> tuple 表示插件循环依赖
    else:
        raise abnormal.PluginLoopsDependencies(run_order)


def getPluginConfig(path: Union[str, dict]) -> Union[
    Tuple[dict, List[Any]], Tuple[Dict[str, FilemappingDict], Union[List[Any], List[Mistake]]]]:
    """
    path: dict
        插件配置字典

    path: str
        配置文件路径
        读取插件配置文件夹
        这个文件夹是全部插件的配置文件夹
        如果 文件夹中有一个 "__init__.py" 文件 则认为是模块导入
        没有的话会使用 exec 函数导入配置文件
    :param path: 配置文件夹路径
    :return: (<插件配置字典>, <错误信息>)
    """

    if isinstance(path, dict):
        return (path, [])

    else:
        # path -> str
        # 导入配置文件
        # 优化导入
        listOfFiles = helperFunctions.__fileFiltering__(path, (".py"))
        returnValue = __singleThreaded__(listOfFiles)
        errorMessage = []
        if returnValue.moduleAbnormal.__len__() != 0:
            # 导入错误
            errorMessage = returnValue.moduleAbnormal

        # 导入成功
        # 类转化 Module -> dict -> FilemappingDict
        return ({
                    key: Class.FilemappingDict(helperFunctions.configConvertTodict(value))
                    for key, value in returnValue.invoke.items()
                }, errorMessage)
