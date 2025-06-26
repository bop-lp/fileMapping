import copy
import os
import sys
from types import ModuleType
from typing import Any, Union
import traceback
import importlib

from . import config
from . import Class
from . import abnormal
from . import helperFunctions


class Module(Class.Module):
    def __init__(self, path: str):
        """
        :param path: 这个是绝对路径
        """
        super().__init__(path)

        self.pointer = None
        self.path = path
        self.absolutePath = os.path.dirname(path)
        self.packageName = os.path.basename(path)

        self.__import__()
        # 导入包

    def __import__(self):
        if self.path.endswith(config.screening):
            self.path = os.path.dirname(self.path)
            # 去除后文件名字

        self.pack = py_import(self.absolutePath, self.packageName)

        if isinstance(self.pack, abnormal.PackageImport):
            raise self.pack

    def run(self, **kwargs) -> Union[Any, abnormal.PackageRun]:
        """
        运行包
        :return:
        """
        try:
            if self.pointer is None:
                return None

            parameterFilling = helperFunctions.parameterFilling(self.pointer, kwargs)
            return self.pointer(**parameterFilling)

        except Exception as e:
            raise abnormal.PackageRun(traceback.format_exc(), self.path, e)


def f(path: str) -> Union[Class.Module, bool]:
    """

    :param path:
    """
    if path.endswith('__init__.py'):
        path = os.path.dirname(path)
        return Module(path)

    else:
        return Module(path)



def py_import(file_path: os.path, callObject: str) -> Union[ModuleType, abnormal.PackageImport]:
    """
    在 importlib.import_module 中有一个缓存机制
    如果 sys.module 中有这个包，就会直接返回这个包
    所以需要在 sys.module 中 临时删除这个包 然后再重新导入
    :param file_path: 绝对路径
    :param callObject: 'main'
    :return:

    """
    callObject = callObject.split('.')[0]  # 去除 .py
    # 检查 sys.module 中是否有这个包
    temporaryPackages = False
    if callObject in sys.modules:
        temporaryPackages = sys.modules[callObject]
        del sys.modules[callObject]

    try:
        sys.path.append(file_path)
        the_api = importlib.import_module(callObject)

    except Exception:
        the_api = abnormal.PackageImport(traceback.format_exc(), file_path)

    if not isinstance(temporaryPackages, bool):
        # 恢复 sys.module 中原来的包
        sys.modules[callObject] = temporaryPackages

    sys.path = sys.path[:-1]  # 去除 sys.path 中最后一个路径
    return the_api
