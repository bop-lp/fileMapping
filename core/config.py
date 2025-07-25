# 这个是对 fileMapping 项目的配置文件
# 主要是用于配置一些参数
# ps: 我是copy的


import os.path
import sys
import copy
from typing import List

functionsName = {
    # 保留参数
    "__fileName__": "__fileName__",
    # "__file__": "__fileName__",
    "__function__": "__init__",
    "__run__": "__run__",
    "__end__": "__end__",
    "__level__": "__level__",
    "__init__.py": "__init__.py",
    "__init__": "__init__.py",
    "__version__": "__version__",

    # 0.3.15 新增参数
    **{
        "__dependenciesOnPlugins__": "__dependenciesOnPlugins__",
        "__temporaryFolders__": "__temporaryFolders__",
        "__error__": "__error__",
        "__underlying__": "__underlying__"
    },

    # 0.3.19 新增参数
    **{
        "__dataFolders__": "__dataFolders__"
    },

    # 0.4.0 新增参数
    **{
        "__multipleInstances__": "__multipleInstances__",
    }
}
functions = {
    # 保留参数
    "__fileName__": None,
    "__function__": "main",
    "__run__": True,
    "__end__": 'end',
    "__level__": -1,
    "__init__.py": "__init__.py",
    "__init__": False,
    "__version__": None,
    "__dependenciesOnPlugins__": [],
    "__temporaryFolders__": None,
    "__error__": None,
    "__underlying__": False,
    "__dataFolders__": None,
    "__multipleInstances__": None,
}
"""
__level__
__dependenciesOnPlugins__
__underlying__
这三个是是决定导入方式, 无法导入后获取, 使用正则获取
"""
"""
在fileMapping 0.3.5之前 __fileName__ 是可以使用的
在fileMapping 0.3.5之后 __fileName__ 不可使用
原因是 pluginLoading.py 文件中的 impo 函数重写了


__fileName__: str 文件名 计划弃用

__function__: str/ func 函数名 or 一个地址(可以直接调用的)
    - 若为 str 则直接使用该值作为函数名
    - 若为 func 则直接使用该函数
        - 计划在后续版本中支持直接调用函数

    - 若为 '' 则只调用, 不执行函数

__run__: bool 控制是否导入该文件/包
    - True: 导入该文件/包
    - False: 不导入该文件/包

__end__: str 控制程序结束时的结束任务
    - 'end': 结束程序
    - '': 不执行

__level__: int 控制导入的等级
    - 0：默认等级，不影响导入顺序
    - n：由包自己控制，然后获取该整数，做出排序，然后进行导入
"""

functions_bad = {
    "__fileName__": False,
    "__function__": False,
    "__run__": False,
}

# 用于保存当前文件的路径
saveThePath = os.path.dirname(__file__)

error_list_a1 = (
    # 用于导入模块时发生的错误
    ModuleNotFoundError, TypeError, ImportError, FileNotFoundError, ModuleNotFoundError
)
error_list_a2 = (
    # 用于执行函数时发生的错误
    TypeError, Exception
)
error_all = (
    # 用于所有错误
    Exception
)

config_type_tuple = (dict, list, tuple)

screening = ("py", "pyc", "pyi")

#
path = copy.copy(sys.path)[::-1]
_ = []
for i in path:
    if i.endswith('zip'):
        _.append(i)
        break

    else:
        _.append(i)

path = _[::-1]


multithreading: bool = False
# 是否开启多线程
numberOfThreads: int = 4
# 线程数 - 合理的线程数 4 - 6

endTask: bool = True
# 是否执行结束任务


__builtInPlugins = 'builtInPlugins'
# 内置插件的目录名


disablePlugins: List[str]= []
# 禁用插件列表
# list[<插件名字>]

__all__ = [
    "functionsName",
    "functions",
    "functions_bad",
    "saveThePath",
    "error_list_a1",
    "error_list_a2",
    "error_all",
    "config_type_tuple",
    "screening",
    "path",
    "multithreading",
    "numberOfThreads",
]
