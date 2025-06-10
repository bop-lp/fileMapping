# 多线程辅助函数
from typing import List, Dict

from .Class import EnableMultithreading


def _task(func, T: EnableMultithreading, text_dict: Dict[str, str]) -> Dict[str, str]: ...


def file_read(T: EnableMultithreading, path_dist: Dict[str, str], mode: str = 'r', encoding: str = 'utf-8') -> Dict[str, str]:
    """
    多线程读取文件内容

    :param T: enableMultithreading 对象
    :param path_dist: 文件路径列表
    :param mode:文件打开模式
    :param encoding: 文件编码
    :return: 文件对象列表
    """
    ...


def text_parsing(T: EnableMultithreading, text_dict: Dict[str, str]) -> Dict[str, Dict[str, int | str]]:
    """
    多线程文件内容解析

    :param T: enableMultithreading 对象
    :param text_dict: 文件内容列表
    :return: 已解析内容列表
    """
    ...


def file_import(T: EnableMultithreading, import_func, file_list: List[str], file_path_list: Dict[str, str], **kwargs) -> List:
    """
    多线程文件导入

    :param T: enableMultithreading 对象
    :param import_func: 导入文件的功能
    :param file_list: 文件对象列表
    :param file_path_list: 文件路径列表
    :return: 导入的对象列表
    """
    ...

