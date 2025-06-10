# 这个文件是用来定义类的，包括类属性、方法等
from typing import Any, Callable, Dict, Union, Tuple, TypeVar, List, ItemsView
from types import ModuleType, FunctionType

from . import abnormal


class FilemappingDict:
    def __init__(self, initial_data: Dict[str, Any] = None) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def update(self, other: dict) -> None: ...


class PlugInData(FilemappingDict): ...


logData = TypeVar("logData", bound="List[abnormal.Mistake]")


class LogData(Dict[str, logData], FilemappingDict):
    fileMapping: List[abnormal.Mistake]
    parameterApplication: List[abnormal.Mistake]


class ConfigData(FilemappingDict):
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


class EnableMultithreading:
    max_workers: int
    callback_function: Any
    errorHandling: Any

    def __init__(self, max_workers: int = 4, callback_function=None, errorHandling=None) -> None: ...
    def __func__(self, func, **kwargs) -> Any: ...
    def task_run(self, task_list: list, clogging: bool = True, wrapper_list: list = None,
                 wrapper_parameters: dict = None, parameters: dict = None) -> Any: ...
    def task_recursion(self, task_dict: dict, clogging: bool = True, wrapper_list: list = None,
                       wrapper_parameters: dict = None, parameters: dict = None) -> dict: ...
    def close(self) -> bool: ...


class Module:
    pack: Any
    path: str
    packageName: str
    absolutePath: str

    def __init__(self, path: str) -> None: ...
    def run(self, **kwargs: Any) -> Any: ...
    def __import__(self) -> Any: ...


class Decorators:
    data: dict

    def wrapper(self, func: Callable) -> Callable: ...


class PlugIns(FilemappingDict): ...


class PluginTimestamp(PlugIns):
    init: float
    end: float
    take: float


timeWrapperData = TypeVar("timeWrapperData", bound="PluginTimestamp")


class TimeWrapperData(Dict[str, timeWrapperData], PlugIns): ...


class TimeWrapper(Decorators):
    data: TimeWrapperData

    def get_data(self, func_id) -> Union[PluginTimestamp, None]: ...


class PlugInRetention(PlugIns):
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
    __underlying__: bool
    __dataFolders__: Union[list, tuple]


infoWrapperData = TypeVar("infoWrapperData", bound="PlugInRetention")


class InfoWrapperData(Dict[str, infoWrapperData], PlugIns): ...


class InfoWrapper(Decorators):
    data: InfoWrapperData


module_type = TypeVar('module_type', bound='Module')


class CallObject(PlugIns, Dict[str, module_type]):
    def items(self) -> ItemsView[str, Module]: ...


moduleType_type = TypeVar('moduleType_type', bound='ModuleType')


class Invoke(PlugIns, Dict[str, moduleType_type]):
    def items(self) -> ItemsView[str, ModuleType]: ...


run_time_type = TypeVar('run_time_type', bound='PluginTimestamp')


class RunTime(PlugIns, Dict[str, run_time_type]):
    def items(self) -> ItemsView[str, PluginTimestamp]: ...


File_info_type = TypeVar('File_info_type', bound='PlugInRetention')


class FileInfo(PlugIns, Dict[str, File_info_type]):
    def items(self) -> ItemsView[str, PlugInRetention]: ...


class FunctionTypeData(FilemappingDict):
    name: str
    func: FunctionType
    kwargs: dict

    def __init__(self, name: str, func: FunctionType, kwargs: dict = None) -> None: ...


class DecoratorsData(FilemappingDict):
    registerList: List[FunctionTypeData]
    functionRegistrations: List[FunctionTypeData]

    def __init__(self, registerList: list = None, functionRegistrations: list = None) -> None: ...


class Information(PlugIns):
    run_time: RunTime
    file_info: FileInfo
    decorators: DecoratorsData

    def __init__(self, run_time: dict = None, file_info: dict = None) -> None: ...


class PlugInRunData(PlugIns):
    callObject: CallObject
    invoke: Invoke
    information: Information

    def __init__(self, callObject: Union[CallObject, dict], invoke: Union[Invoke, dict],
                 information: Union[Information, dict]) -> None: ...


class ReturnValue(FilemappingDict): ...


class File(FilemappingDict):
    multithreading: EnableMultithreading
    config: ConfigData
    path: str
    plugInRunData: PlugInRunData
    returnValue: ReturnValue
    logData: LogData
    plugInData: PlugInData
    configData: ConfigData


class ParameterApplication:
    self_info: File

    def __init__(self, self_info: File) -> None: ...
    def init(self) -> Any: ...
    def end(self) -> Any: ...


class EndFunc:
    name: str
    func: FunctionType

    def __init__(self, name: str, func: FunctionType) -> None: ...


class RegisterData(FilemappingDict):
    registerList: List[FunctionType]
    end_func: List[EndFunc]

    def __init__(self, registerList: list = None, end_func: list = None) -> None: ...