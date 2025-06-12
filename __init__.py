#######################
# 以下为快捷导入
import os

from .core import File
from .core import pathConversion
# from .core import parameterApplication

#######################
# 以下为各个模块的导入
from . import core
from .core import abnormal
# abnormal 模块 异常处理模块
from .core import Class
from .core import config
from .core import decorators
# fileMapping.decorators 装饰器模块
from .core import fileImport
from .core import helperFunctions
# helperFunctions 辅助函数模块
from .core import multithreading
from .core import multiThreadedHelperFunctions
from .core import parameterApplication
from .core import wordProcessing
# 文字处理模块


# 加载fileMapping的内置插件
if not __name__ == '__main__':
    # print(pathConversion(__file__, "builtInPlugins"))
    # print(os.path.dirname(__file__), os.path.abspath("builtInPlugins"))
    _f = File(pathConversion(__file__, "builtInPlugins"), {})


__all__ = [
    *core.__all__
]

