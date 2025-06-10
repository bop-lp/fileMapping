from typing import Tuple, Dict

from . import Class

class PluginData(Class.PlugInData): ...

class LogData(Class.LogData): ...

class ConfigData(Class.ConfigData):
    functionsName: Dict[str, str]
    functions: Dict[str, str]
    functions_bad: Dict[str, str]
    error_list_a1: Tuple[ModuleNotFoundError, TypeError, ImportError, FileNotFoundError, ModuleNotFoundError]
    error_list_a2: Tuple[TypeError, Exception]
    error_all: Tuple[EOFError]
    config_type_tuple: Tuple[dict, list, tuple]
    screening: Tuple[str]
    multithreading: bool
    numberOfThreads: int

class ReturnValue(Class.ReturnValue): ...

logData: LogData
plugInData: PluginData
configData: ConfigData
returnValue: ReturnValue

class File(Class.File):
    logData: Class.LogData
    plugInData: Class.PlugInData
    returnValue: Class.ReturnValue