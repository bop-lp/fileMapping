from typing import Dict


from . import Class
# 数据存放


class PluginData(Class.PlugInData):
    # 这里是插件数据
    parameterApplication: Dict[str, Class.ParameterApplication] = {}
    # 这里是插件注册数据
    # parameterApplication => {<插件名字>: {<函数名字>: [FunctionType], ...}, ...}
    decorators: Class.DecoratorsData
    builtInPlugins: Class.FilemappingDict = Class.FilemappingDict()
    plugInData: Class.FilemappingDict = Class.FilemappingDict()
    # plugInData 插件数据 是一个字典 key是插件名字 value是插件注册数据
    # 由插件自已写入数据 应该去看插件的文档/源码

    def __init__(self):
        super().__init__()

        self.decorators = Class.DecoratorsData()


class LogData(Class.LogData): ...



class ConfigData(Class.ConfigData): ...
    # functionsName: Dict[str, str]
    # functions: Dict[str, str]
    # functions_bad: Dict[str, str]
    # # 这里fileMapping的配置数据
    # error_list_a1: Tuple[ModuleNotFoundError, TypeError, ImportError, FileNotFoundError, ModuleNotFoundError]
    # error_list_a2: Tuple[TypeError, Exception]
    # error_all: Tuple[EOFError]
    # # error 可能用不到
    # config_type_tuple: Tuple[dict, list, tuple]
    # screening: Tuple[str]
    # multithreading: bool = True
    # numberOfThreads: int = 4


# 这里是返回值数据
class ReturnValue(Class.ReturnValue): ...


# class PublicData(Class.FilemappingDict): ...
# 这里是公共数据


logData = LogData()
plugInData = PluginData()
configData = ConfigData()
returnValue = ReturnValue()
# publicData = PublicData()
# 公共数据


class File(Class.File):
    logData: Class.LogData = logData
    plugInData: Class.PlugInData = plugInData
    returnValue: Class.ReturnValue = returnValue

