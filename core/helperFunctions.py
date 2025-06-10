import os
from collections import ChainMap
from typing import List
import inspect

from . import config as Config


def pathValidation(path_lit: list) -> bool:
    """
    路径验证
    :param path_lit: 路径 list
    """
    return False in [
        (os.path.isabs(i) or os.path.exists(i))
        for i in path_lit
    ]


def pathConversion(cpath: os.path, path: os.path) -> os.path:
    """
    如果插件路径文件夹在根目录下 可以使用这个快速生成绝对路径

    具体请看fileMapping插件文档
    :param cpath: __file__
    :param path: 必须为文件夹
    :return:
    """
    return os.path.join(os.path.dirname(cpath)if os.path.isfile(cpath)else cpath, os.path.abspath(path))



def dictMerge(*args: List[dict]) -> dict:
    """
    多个dict合并
    :param args: dict
    """
    return dict(ChainMap(*reversed(args)))  # 需要反转参数顺序


def __fileFiltering__(cpath: os.PathLike, screening: tuple) -> dict:
    """
    文件筛选
    :param cpath: 路径
    :param screening: 允许的文件扩展名元组
    :return: 文件名(不含扩展名)->文件路径的映射字典
    """
    result = {}

    for entry in os.scandir(cpath):
        if entry.is_file():
            # 处理文件：检查扩展名是否在筛选列表中
            name_parts = entry.name.split('.')
            if len(name_parts) > 1 and name_parts[-1] in screening:
                key = name_parts[0]
                result[key] = entry.path
        elif entry.is_dir():
            # 处理目录：检查是否包含 __init__.py 文件
            init_file = os.path.join(entry.path, Config.functionsName["__init__.py"])
            if os.path.isfile(init_file):
                key = entry.name  # 使用目录名作为键
                result[key] = init_file

    return result

def deep_update(dict1: dict, dict2: dict) -> dict:
    """
    深度合并两个字典

    :param dict1: 字典1
    :param dict2: 字典2
    """
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            # 如果键存在且对应的值都是字典，则递归调用 deep_update 进行深度合并
            deep_update(dict1[key], value)
        else:
            # 否则直接更新键值对
            dict1[key] = value

    return dict1



def configConvertTodict(config) -> dict:
    """
    将配置文件转换为dict格式
    :param config: 配置文件
    :return: dict 格式的配置文件
    """
    # config_type_tuple -> (dict, list, tuple)
    if isinstance(config, Config.config_type_tuple):
        return config

    systemConfiguration = {}
    for obj in dir(config) if not isinstance(config, Config.config_type_tuple) else config:
        if obj.startswith("__"):
            continue

        if isinstance(getattr(config, obj), Config.config_type_tuple) \
                if not isinstance(config, Config.config_type_tuple) else isinstance(
                config[obj], Config.config_type_tuple):
            systemConfiguration[obj] = configConvertTodict(getattr(config, obj))

        else:
            systemConfiguration[obj] = getattr(config, obj) \
                if not isinstance(config, Config.config_type_tuple) else config[obj]

    return systemConfiguration


def parameterFilling(pointer, kwargs: dict) -> dict:
    """
    填充参数

    :param pointer: 参数指向的函数
    :param kwargs: 关键字参数
    :return:
    """
    if kwargs is None:
        kwargs = {}

    return {
        key: value for key, value in kwargs.items() if key in list(inspect.signature(pointer).parameters.keys())
    }



def sort(original_dict: dict) -> dict:
    """
    对字典的键进行排序，并返回一个新的字典，其中键按升序排列
    :param original_dict:
    :return:
    """
    return {key: original_dict[key] for key in sorted(original_dict.keys())}

