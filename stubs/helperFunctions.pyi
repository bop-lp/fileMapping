import os
from typing import List, Dict

def pathValidation(path_lit: List[str]) -> bool:
    """
    路径验证
    :param path_lit: 路径 list
    """
    ...

def pathConversion(cpath: os.PathLike, path: os.PathLike) -> os.PathLike:
    """
    如果插件路径文件夹在根目录下 可以使用这个快速生成绝对路径

    具体请看fileMapping插件文档
    :param cpath: __file__
    :param path: 必须为文件夹
    :return:
    """
    ...

def dictMerge(*args: List[Dict]) -> Dict:
    """
    多个dict合并
    :param args: dict
    """
    ...

def __fileFiltering__(cpath: os.PathLike, screening: tuple) -> Dict[str, str]:
    """
    文件筛选
    :param cpath: 路径
    :param screening: 允许的文件扩展名元组
    :return: 文件名(不含扩展名)->文件路径的映射字典
    """
    ...

def deep_update(dict1: Dict, dict2: Dict) -> Dict:
    """
    深度合并两个字典

    :param dict1: 字典1
    :param dict2: 字典2
    """
    ...

def configConvertTodict(config: object) -> Dict:
    """
    将配置文件转换为dict格式
    :param config: 配置文件
    :return: dict 格式的配置文件
    """
    ...

def parameterFilling(pointer: callable, kwargs: Dict) -> Dict:
    """
    填充参数

    :param pointer: 参数指向的函数
    :param kwargs: 关键字参数
    :return:
    """
    ...

def sort(original_dict: Dict) -> Dict:
    """
    对字典的键进行排序，并返回一个新的字典，其中键按升序排列
    :param original_dict:
    :return:
    """
    ...

__all__: List[str] = [
    "pathValidation",
    "pathConversion",
    "dictMerge",
    "configConvertTodict",
    "parameterFilling",
    "sort",
    "deep_update",
]