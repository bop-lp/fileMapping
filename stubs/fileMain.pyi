from typing import Union, Tuple, Dict

from . import data
from . import Class

class File(data.File):
    def __init__(self, path: Union[str, list], config: dict) -> None: ...

def __multithreading__(multithreading: Class.EnableMultithreading, listOfFiles: dict) -> Class.PlugInRunData: ...

def __singleThreaded__(listOfFiles: dict) -> Class.PlugInRunData: ...


