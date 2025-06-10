import copy
import os
import sys
from types import ModuleType
from typing import Any, Union
import traceback
import importlib

import rich

from . import config
from . import Class
from . import abnormal
from . import helperFunctions


class Module(Class.Module):
    def __init__(self, path: str):
        """
        111
        :param path: 这个是绝对路径
        """
        super().__init__(path)

        self.pointer = None
        self.path = path
        self.absolutePath = self.path if os.path.isabs(self.path) == True else os.path.realpath(self.path)
        self.packageName = os.path.basename(path)

        self.__import__()
        # 导入包

    def __import__(self):
        if self.path.endswith(config.screening):
            self.path = os.path.dirname(self.path)
            # 去除后文件名字

        self.pack = py_import(self.path, self.packageName)

        rich.print(dir(self.pack))
        if isinstance(self.pack, abnormal.PackageImport):
            raise self.pack

    def run(self, **kwargs) -> Any:
        """
        运行包
        :return:
        """
        try:
            if self.pointer is None:
                return None

            parameterFilling = helperFunctions.parameterFilling(self.pointer, kwargs)
            return self.pointer(**parameterFilling)

        except Exception:
            raise abnormal.PackageRun(traceback.format_exc(), self.path)


def f(path: str) -> Union[Class.Module, bool]:
    """

    :param path:
    """
    if path.endswith('__init__.py'):
        return Module(os.path.dirname(path))

    else:
        return Module(path)



def py_import(file_path: os.path, callObject: str) -> Union[ModuleType, abnormal.PackageImport]:
    """
    :param callObject: 'main'
    :param file_path: 绝对路径
    :return:

    """
    path = copy.copy(sys.path)
    callObject = callObject.split('.')[0]  # 去除 .py
    try:
        sys.path = config.path+[file_path]
        the_api = importlib.import_module(callObject)

    except Exception:
        the_api = abnormal.PackageImport(traceback.format_exc(), file_path)

    sys.path = path
    return the_api
