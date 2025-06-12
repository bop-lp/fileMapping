"""
参数的具体应用
fileMappingConfig.functions


"""
import atexit
import functools
import os
import traceback
import types
from types import FunctionType

from . import Class
from . import abnormal
from . import data
from . import helperFunctions


import rich


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
class PlugInData(Class.ParameterApplication):
    def init(self):
        # 给插件创建一个plugInData的空间
        for plugInsName in self.self_info.plugInRunData.callObject:
            self.self_info.plugInData[plugInsName] = Class.FilemappingDict()


@wrapper
class Config(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        # 读取每个插件配置文件
        super().__init__(self_info)

        self.plugInData = self.self_info.plugInData

    def init(self):
        for plugInsName, plugInsObject in self.self_info.plugInRunData.invoke.items():
            if "config" not in dir(plugInsObject):
                continue

            plugInsConfig = getattr(plugInsObject, "config")
            if isinstance(plugInsConfig, dict):
                 pass

            elif isinstance(plugInsConfig, types.ModuleType):
                plugInsConfig = helperFunctions.configConvertTodict(plugInsConfig)

            else:
                continue

            self.plugInData[plugInsName].config = plugInsConfig
            # 其中config是插件的配置文件信息


@wrapper
class Init(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

    def pointer(self, key, func):
        self.self_info.plugInRunData.callObject[key].pointer = func

    def init(self):
        for key, value in self.self_info.plugInRunData.information.file_info.items():
            pack = self.self_info.plugInRunData.callObject[key].pack
            # pointer 是函数的存放地
            # pack 是插件的包
            if value['__init__'] in dir(pack):
                _ = value['__init__']

            elif "main" in dir(pack):
                _ = "main"

            else:
                continue

            if not isinstance(_, str):
                continue

            pointer = getattr(pack, _)
            if isinstance(pointer, str):
                pointer = getattr(pack, pointer) if pointer in dir(pack) else None
                self.pointer(key, pointer)

            elif isinstance(pointer, FunctionType):
                self.pointer(key, pointer)


@wrapper
class Run(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.self_info = self_info

    def init(self):
        for key, value in self.self_info.plugInRunData.information.file_info.items():
            if value['__run__'] is False:
                self.self_info.plugInRunData.callObject[key].pointer = None


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

        except Exception as e:
            self.self_info.logData.parameterApplication.append(abnormal.pluginEndError(
                func.__name__, e, traceback.format_exc()
            ))
            return {
                "run": False
            }

    def end(self):
        if not self.self_info.config.endTask:
            # 结束任务关闭
            return

        for key, value in self.self_info.plugInRunData.invoke.items():
            if not self.self_info.config.functionsName["__end__"] in dir(value):
                continue

            pointer = getattr(value, self.self_info.config.functionsName["__end__"])
            if isinstance(pointer, str) and (pointer in dir(value)):
                pointer = getattr(value, pointer)

            elif isinstance(pointer, types.FunctionType):
                pass

            else:
                continue

            self.run(pointer)

