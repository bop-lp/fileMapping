"""
参数的具体应用
fileMappingConfig.functions


"""
import atexit
import shutil
import functools
import os
import traceback
import types

from . import Class
from . import abnormal
from . import data


registerData = Class.RegisterData()


@atexit.register
def AppEnd():
    for i in registerData.end_func:
        func = i.func
        name = i.name
        try:
            func()
        except Exception as e:
            data.logData.parameterApplication.append(
                abnormal.ParameterApplicationEnd(
                    name, e, traceback.format_exc()
                )
            )


def ApplyParameter(self_info: Class.File) -> bool:
    """
    应用参数

    规定如下
    类, 初始化时必须包含self_info参数
    可以有 init 和 end 方法, 用于初始化和结束
    """
    for i in registerData.registerList:
        func: Class.ParameterApplication = i(self_info)
        try:
            if hasattr(func, "init"):
                func.init()
        except Exception as e:
            self_info.logData.parameterApplication.append(
                abnormal.ParameterApplicationRun(
                    func.__ne__, e, traceback.format_exc()
                )
            )


        if hasattr(func, 'end'):
            registerData.end_func.append(Class.EndFunc(
                func.__ne__,
                func.end
            ))

    return True


def wrapper(func: Class.ParameterApplication):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        return func(*args, **kwargs)

    registerData.registerList.append(wrapper_func)
    return func


@wrapper
class TemporaryFolders(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.self_info = self_info
        self.temporaryFolders = True
        if not self_info.path in [False, True, None, '']:  # temporaryFolders 关闭
            self.path = os.path.join(self_info.lordPath, self_info.public.config['temporaryFolders'])

            self.information_temporaryFolders = self.self_info.information["temporaryFolders"] = {}  # 临时文件夹信息
            self.logs = self.self_info.logs["temporaryFolders"] = {"error": []}
            self.create_path = []
            self.init_tmp = False
            # 用于判断临时的文件夹是否自主创建，如果是的话则在结束时删除
            if not os.path.exists(self.path):
                os.mkdir(self.path)
                self.init_tmp = True

        else:
            self.temporaryFolders = False

    def __mkdir(self, temporaryFolders):
        path = os.path.join(self.path, temporaryFolders)
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                self.create_path.append(path)

            self.information_temporaryFolders[temporaryFolders] = path
            return True

        except FileExistsError as e:
            self.logs["error"].append({path: e})
            return False

    def init(self):
        if not self.temporaryFolders:
            return False

        for key, value in self.self_info.Class.File_info.items():
            temporaryFolders = value['__temporaryFolders__']
            if temporaryFolders is None:
                continue

            if isinstance(temporaryFolders, str):
                self.__mkdir(temporaryFolders)

            else:  # temporaryFolders is a list
                for folder in temporaryFolders:
                    self.__mkdir(folder)

    def end(self):
        for i in self.create_path:
            shutil.rmtree(i)

        if self.init_tmp:
            shutil.rmtree(self.path)


@wrapper
class DataFolders(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.self_info = self_info
        self.dataFolders = True
        self.create_path = []
        self.rootPath = self_info.public.get("config", {}).get("rootPath", False)  # 根目录
        run = self_info.public.get("config", {}).get("dataFolder", False)
        if not ((self.rootPath is False) and (run is False)):
            # dataFolders 开启
            self.logs = self.self_info.logs["dataFolders"] = {"error": []}
            dataFolder_path = self_info.public.config["dataFolder"]
            self.information_dataFolders = self.self_info.information["dataFolders"] = {}  # 临时文件夹信息
            self.path = os.path.join(self.rootPath, dataFolder_path)
            if not os.path.exists(self.path):
                os.mkdir(self.path)  # 创建 dataFolder 目录

        else:
            self.dataFolders = False

    def __mkdir(self, file_path):
        path = os.path.join(self.path, file_path)
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                self.create_path.append(path)

            self.information_dataFolders[file_path] = path
            return True

        except FileExistsError as e:
            self.logs["error"].append({path: e})
            return False

    def init(self):
        if not self.dataFolders:
            return False

        for key, value in self.self_info.Class.File_info.items():
            dataFolders = value['__dataFolders__']
            if dataFolders is None:
                continue

            if isinstance(dataFolders, str):
                dataFolders = [dataFolders]

            for dataFolder in dataFolders:
                self.__mkdir(dataFolder)  # 创建 dataFolder 目录


@wrapper
class Init(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

    def init(self):
        for key, value in self.self_info.plugInRunData.information.file_info.items():
            _ = None
            if not value['__init__'] is [None, False, '']:
                try:
                    _ = getattr(self.self_info.plugInRunData.callObject[key].pack, value['__init__'])

                except AttributeError as e:
                    self.self_info.logData.parameterApplication.append(
                        abnormal.ParameterApplicationInit(key, e, traceback.format_exc())
                    )

            self.self_info.plugInRunData.callObject[key].pointer = _



@wrapper
class Run(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.self_info = self_info

    def init(self):
        for key, value in self.self_info.plugInRunData.information.items():
            if value['__run__'] is False:
                self.self_info.plugInRunData.callObject[key].pointer = None


@wrapper
class ReadRegistration(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        """
        register.threadRegistration

        :param self_info:
        """
        super().__init__(self_info)

        self.self_info = self_info
        self.info = self_info.plugInRunData.information.registration
        self.logs = self_info.logs["readRegistration"] = {"error": []}

    def init(self):
        func_list = {}
        for key, value in self.info.items():
            level = value['level']
            if level not in func_list:
                func_list[level] = []

            func_list[level].append(key)

        func_list = sorted(func_list.items(), key=lambda x: x[0])
        for level, func_list in func_list:
            for func in func_list:
                try:
                    func(**self.info[func]['kwargs'])

                except Exception as e:
                    self.self_info.logs['readRegistration']['error'].append({func: e})


@wrapper
class Config(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        """
        终于解决每个插件，之间的配置问题
        运行时会插件的配置和用户的配置深度合成,并放入File.config到
        :param self_info: 初始化信息 -> fileMapping.File
        """
        super().__init__(self_info)

        self.self_info = self_info
        self.logs = self_info.logs["config"] = {"error": []}

    def init(self):
        for key, value in self.self_info.information.items():
            pass


@wrapper
class End(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        """
        用于解决每个插件的结束 "end" / "__end__"

        """
        super().__init__(self_info)

        self.self_info = self_info

    def run(self, func: types.FunctionType) -> dict:
        try:
            func()
            return {
                "run": True
            }

        except Class.FileMappingConfig.error_list_a2 as e:
            return {
                "run": False,
                "error": e,
                "traceback": traceback.format_exc()
            }

    def end(self):
        if not Class.FileMappingConfig.endTheTask:
            return

        for key, value in self.self_info.invoke.items():
            if not Class.FileMappingConfig.functionsName["__end__"] in dir(value):
                continue

            pointer = getattr(value, Class.FileMappingConfig.functionsName["__end__"])
            if isinstance(pointer, str) and (pointer in dir(value)):
                pointer = getattr(value, pointer)

            elif isinstance(pointer, types.FunctionType):
                pass

            else:
                continue

            data = self.run(pointer)
            if data["run"]:
                self.self_info.logs.fileMappingOutput(
                    information.error.EndOfPlugin(
                        key, pointer.__name__, data["error"], data["traceback"]
                    )
                )

