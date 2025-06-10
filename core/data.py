from typing import Tuple, Dict


from . import Class
# 数据存放


class PluginData(Class.PlugInData):
    # 这里是插件数据
    pass



class LogData(Class.LogData): ...



class ConfigData(Class.ConfigData):
    functionsName: Dict[str, str]
    functions: Dict[str, str]
    functions_bad: Dict[str, str]
    # 这里fileMapping的配置数据
    error_list_a1: Tuple[ModuleNotFoundError, TypeError, ImportError, FileNotFoundError, ModuleNotFoundError]
    error_list_a2: Tuple[TypeError, Exception]
    error_all: Tuple[EOFError]
    # error 可能用不到
    config_type_tuple: Tuple[dict, list, tuple]
    screening: Tuple[str]
    multithreading: bool = True
    numberOfThreads: int = 4


# 这里是返回值数据
class ReturnValue(Class.ReturnValue): ...


logData = LogData()
plugInData = PluginData()
configData = ConfigData()
returnValue = ReturnValue()


class File(Class.File):
    logData: Class.LogData = logData
    plugInData: Class.PlugInData = plugInData
    returnValue: Class.ReturnValue = returnValue

