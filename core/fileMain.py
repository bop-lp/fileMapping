from typing import Union, Tuple, Dict

import rich

from . import data, abnormal
from . import Class
from . import helperFunctions
from . import config as Config
from . import decorators

from . import multithreading
from . import multiThreadedHelperFunctions

from . import wordProcessing
from . import fileImport
from . import parameterApplication


class File(data.File):
    def __init__(self, path: Union[str, list], config: dict):
        """

        :param path: 插件路径列表 必须为绝对路径
        :param config: fileMapping的配置
        """
        super().__init__()

        if isinstance(path, str):
            # 兼容 str
            path = [path]

        if helperFunctions.pathValidation(path if isinstance(path, (list, tuple)) else [path]):
            raise FileNotFoundError(f"不是一个有效的绝对路径。: '{path}'")

        _ = [helperFunctions.__fileFiltering__(i, Config.screening) for i in path]
        listOfFiles = helperFunctions.dictMerge(*_)
        config = helperFunctions.deep_update(helperFunctions.configConvertTodict(Config),config) \
            if config else helperFunctions.configConvertTodict(Config)

        data.configData = data.ConfigData(config)
        self.config = data.configData
        self.path = path

        if self.config.get('multithreading', False):
            self.multithreading = multithreading.EnableMultithreading(
                self.config.numberOfThreads
            )
            self.plugInRunData = __multithreading__(self.multithreading, listOfFiles)

        else:
            self.plugInRunData = __singleThreaded__(listOfFiles)

        parameterApplication.ApplyParameter(self)
        # for i in self.plugInRunData.moduleAbnormal:
        #     print(i.stack)


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
        info_wrapper = decorators.InfoWrapper(Config.functions)
        for __level__, L in run_order.items():
            data = multiThreadedHelperFunctions.file_import(multithreading, fileImport.f, L, listOfFiles,
                                                wrapper_list=[time_wrapper.wrapper, info_wrapper.wrapper])
            # callObject |= dict(zip(L, data))
            # invoke |= dict(zip(L, [i.pack for i in data]))
            # 以上是 python3.9 才支持的语法
            moduleData = [
                i for i in data if isinstance(i, Class.Module)
            ]
            plugInData.moduleAbnormal += [
                i for i in data if not isinstance(i, Class.Module)
            ]

            plugInData.callObject.update(dict(zip(L, moduleData)))
            plugInData.invoke.update(dict(zip(L, [i.pack for i in moduleData])))

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
        info_wrapper = decorators.InfoWrapper(Config.functions)
        for __level__, L in run_order.items():
            for name in L:
                fileImport.f.__name__ = name
                plugInData.callObject[name] = info_wrapper.wrapper(time_wrapper.wrapper(fileImport.f))(
                    listOfFiles[name])
                plugInData.invoke[name] = plugInData.callObject[name].pack

        else:
            # 获取 时间 & 信息 -> information.run_time & file_info
            plugInData.information = Class.Information(time_wrapper.data, info_wrapper.data)
            return plugInData

    # sorting_plugin -> tuple 表示插件循环依赖
    else:
        raise abnormal.PluginLoopsDependencies(run_order)


