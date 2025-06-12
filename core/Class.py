# 这个文件是用来定义类的，包括类属性、方法等
from typing import Any, Callable, Dict, Union, Tuple, TypeVar, List, ItemsView
from types import ModuleType, FunctionType

from . import abnormal


class FilemappingDict:
    """
    增强类，支持通过字典语法访问和设置实例属性，
    所有字典操作（如 obj["key"]）映射到实例属性（obj.key）。
    """

    def __init__(self, initial_data: Dict[str, Any] = None) -> None:
        """初始化时接受字典数据，转换为实例属性"""
        super().__init__()

        if initial_data:
            self.update(initial_data)

    def __getitem__(self, key: str):
        """通过字典语法访问实例属性"""
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"'{self.__class__.__name__}' object has no key '{key}'")

    def __setitem__(self, key: str, value: Any):
        """通过字典语法设置实例属性"""
        setattr(self, key, value)

    def __delitem__(self, key: str):
        """通过字典语法删除实例属性"""
        if hasattr(self, key):
            delattr(self, key)
        else:
            raise KeyError(f"'{self.__class__.__name__}' object has no key '{key}'")

    def __contains__(self, key: str):
        """检查实例是否有某个属性"""
        return hasattr(self, key)

    def __iter__(self):
        """迭代所有实例属性名"""
        return iter(self.__dict__.keys())

    def __len__(self):
        """返回实例属性数量"""
        return len(self.__dict__)

    def keys(self):
        """返回所有属性名"""
        return self.__dict__.keys()

    def values(self):
        """返回所有属性值"""
        return self.__dict__.values()

    def items(self):
        """返回所有属性键值对"""
        return self.__dict__.items()

    def get(self, key: str, default: Any = None):
        """获取属性值，不存在时返回默认值"""
        return getattr(self, key, default)

    def update(self, other: dict):
        """批量更新属性"""
        for key, value in other.items():
            setattr(self, key, value)


logData = TypeVar("logData", bound="List[abnormal.Mistake]")


class LogData(Dict[str, logData], FilemappingDict):
    # 这里是日志数据
    fileMapping: List[abnormal.Mistake] = []
    # fileMapping是日志数据
    parameterApplication: List[abnormal.Mistake] = []


class ConfigData(FilemappingDict):
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
    multithreading: bool
    numberOfThreads: int
    endTask: bool


# 以上是数据类


# 多线程类
class EnableMultithreading:
    max_workers: int = 4
    callback_function: Any
    errorHandling: Any

    def __init__(self, max_workers: int = 4, callback_function=None, errorHandling=None):
        self.max_workers = max_workers
        self.callback_function = callback_function
        self.errorHandling = errorHandling

    def __func__(self, func, **kwargs): ...

    def task_run(self, task_list: list, clogging: bool = True, wrapper_list: list = None,
                 wrapper_parameters: dict = None, parameters: dict = None): ...

    def task_recursion(self, task_dict: dict, clogging: bool = True, wrapper_list: list = None,
                       wrapper_parameters: dict = None, parameters: dict = None) -> dict: ...

    def close(self) -> bool: ...


# fileMapping的 Module (模块)类
class Module:
    pack: Any = None

    path: str
    packageName: str
    absolutePath: str

    def __init__(self, path: str):
        self.path = path

    def run(self, **kwargs: Any) -> Any: ...

    def __import__(self): ...


# 装饰器类
class Decorators:
    data: dict

    # 一般用来保存装饰器运行时的数据

    def wrapper(self, func: Callable) -> Callable: ...


# 插件的基本类 一般用不的 就是用来继承的
class PlugIns(FilemappingDict):
    def items(self) -> ItemsView[str, Any]:
        # 这里直接调用父类的 items 方法
        return super().items()

    def __init__(self, initial_data: Dict[str, dict] = None):
        super().__init__()
        if initial_data:
            self.update(initial_data)



# 给TimeWrapper 类 用于记录插件运行时间信息类
class PluginTimestamp(PlugIns):
    init: float
    # 插件初始化时间戳
    end: float
    # 插件结束时间戳
    take: float
    # end - init 得到插件运行时间


# TimeWrapperDataType: TypeAlias = Dict[Any, PluginTimestamp]
timeWrapperData = TypeVar("timeWrapperData", bound="PluginTimestamp")


class TimeWrapperData(Dict[str, timeWrapperData], PlugIns): ...


# 用于记录插件运行时间的类
class TimeWrapper(Decorators):
    data: TimeWrapperData

    def get_data(self, func_id) -> Union[PluginTimestamp, None]: ...


# 给 InfoWrapper 类 用于记录插件信息类
class PlugInRetention(PlugIns):
    # 插件保留关键字
    __fileName__: str
    __function__: str
    __run__: bool
    __end__: str
    __level__: int
    __init__: str
    __version__: str
    __dependenciesOnPlugins__: list
    __temporaryFolders__: Union[list, tuple]
    __error__: Any
    __underlying__: bool = False
    __dataFolders__: Union[list, tuple] = False


infoWrapperData = TypeVar("infoWrapperData", bound="PlugInRetention")


class InfoWrapperData(Dict[str, infoWrapperData], PlugIns): ...


# 用于记录插件信息的类
class InfoWrapper(Decorators):
    data: InfoWrapperData


# PlugInRunData 的子类 用于保存插件 Module(fileMapping的 Module 类) 类
module_type = TypeVar('module_type', bound='Module')


class CallObject(PlugIns, Dict[str, module_type]):  ...



# PlugInRunData 的子类 用于保存插件 ModuleType(python的 ModuleType 类) 类
moduleType_type = TypeVar('moduleType_type', bound='ModuleType')


class Invoke(PlugIns, Dict[str, moduleType_type]): ...


# Information 的子类 用于保存插件运行时间和信息类
run_time_type = TypeVar('run_time_type', bound='PluginTimestamp')


class RunTime(PlugIns, Dict[str, run_time_type]): ...


# Information 的子类 用于保存插件信息类
File_info_type = TypeVar('File_info_type', bound='PlugInRetention')


class FileInfo(PlugIns, Dict[str, File_info_type]): ...


class FunctionTypeData(FilemappingDict):
    name: str
    func: FunctionType
    kwargs: dict

    def __init__(self, name: str, func: FunctionType, kwargs: dict = None):
        super().__init__()

        if kwargs is None:
            kwargs = {}

        self.name = name
        self.func = func
        self.kwargs = kwargs


class DecoratorsData(FilemappingDict):
    registerList: List[FunctionTypeData] = []
    functionRegistrations: List[FunctionTypeData] = []

    def __init__(self, registerList: list = None, functionRegistrations: list = None):
        super().__init__()

        if registerList is None:
            registerList = []

        if functionRegistrations is None:
            functionRegistrations = []

        self.registerList = registerList
        self.functionRegistrations = functionRegistrations


# PlugInRunData 的子类 用于保存插件运行时间和信息类
class Information(PlugIns):
    run_time: RunTime = RunTime
    file_info: FileInfo = FileInfo
    decorators: DecoratorsData = DecoratorsData

    def __init__(self, run_time: dict = None, file_info: dict = None):
        super().__init__()

        if run_time is None:
            run_time = {}

        if file_info is None:
            file_info = {}

        self.run_time = RunTime(run_time)
        self.file_info = FileInfo(file_info)


class PlugInRunData(PlugIns):
    callObject: CallObject = CallObject
    invoke: Invoke = Invoke
    information: Information = Information
    moduleAbnormal: List[abnormal.Mistake] = []

    def __init__(self, callObject: Union[CallObject, dict], invoke: Union[Invoke, dict],
                 information: Union[Information, dict]):
        super().__init__()

        self.callObject = CallObject(callObject) if isinstance(callObject, dict) else callObject
        # 这里是插件 callObject 类 保存插件 Module 类
        self.invoke = Invoke(invoke) if isinstance(invoke, dict) else invoke
        # 这里是插件 invoke 类 保存插件 python.Module 类
        self.information = Information(information) if isinstance(information, dict) else information
        # 这里是插件 information 类 保存插件 插件信息和运行时间 类
        self.moduleAbnormal: List[abnormal.Mistake] = []


class ReturnValue(FilemappingDict): ...




class PlugInData(FilemappingDict):
    # 这里是插件数据
    parameterApplication: Dict
    # parameterApplication: Dict[str, ParameterApplication]
    decorators: DecoratorsData
    builtInPlugins: FilemappingDict


# 核心类
class File(FilemappingDict):
    multithreading: EnableMultithreading = EnableMultithreading
    config: ConfigData = ConfigData
    path: str = None
    plugInRunData: PlugInRunData = PlugInRunData
    returnValue: ReturnValue = ReturnValue
    logData: LogData = LogData
    plugInData: PlugInData = PlugInData
    configData: ConfigData = ConfigData


# 这个是给 RegisterData 用的
class ParameterApplication:
    self_info: File

    def __init__(self, self_info: File):
        self.self_info = self_info

    def init(self): ...

    def end(self): ...


class EndFunc:
    name: str
    func: FunctionType

    def __init__(self, name: str, func: FunctionType):
        self.name = name
        self.func = func


class RegisterData(FilemappingDict):
    registerList: List[FunctionType]
    end_func: List[EndFunc]

    def __init__(self, registerList: list = None, end_func: list = None):
        super().__init__()

        if registerList is None:
            registerList = []

        if end_func is None:
            end_func = []

        self.registerList = registerList
        self.end_func = end_func

