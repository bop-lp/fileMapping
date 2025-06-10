# 多线程辅助函数
from typing import List

from . import Class
from . import wordProcessing
from . import decorators


def _task(func, T: Class.EnableMultithreading, text_dict: dict):
    task: list = [(func, i[-1]) for i in text_dict.items()]
    task: List[dict] = T.task_run(task)

    _, i = {}, 0
    for key in text_dict:
        _[key] = task[i]
        i += 1

    return _


def file_read(T: Class.EnableMultithreading, path_dist: dict, mode: str = 'r', encoding: str = 'utf-8'):
    """
    多线程读取文件内容

    :param T: enableMultithreading 对象
    :param path_dist: 文件路径列表
    :param mode:文件打开模式
    :param encoding: 文件编码
    :return: 文件对象列表
    """
    def func(path):
        with open(path, mode=mode, encoding=encoding) as f:
            return f.read()

    return _task(func, T, path_dist)


def text_parsing(T: Class.EnableMultithreading, text_dict: dict):
    """
    多线程文件内容解析

    :param T: enableMultithreading 对象
    :param text_dict: 文件内容列表
    :return: 已解析内容列表
    """
    def func(text):
        return wordProcessing.get_all(text)

    return _task(func, T, text_dict)


def file_import(T: Class.EnableMultithreading, import_func, file_list: list, file_path_list: dict, **kwargs):
    """
    多线程文件导入

    :param T: enableMultithreading 对象
    :param import_func: 导入文件的功能
    :param file_list: 文件对象列表
    :param file_path_list: 文件路径列表
    :return: 导入的对象列表
    """
    def wrapper_func(name: str):
        @decorators.my_wraps(name)  # 效果是保证, 在层层(包装/装饰)下名字不变
        def func(file_name: str):
            return import_func(file_path_list[file_name])

        return func

    return T.task_run([(wrapper_func(i), i) for i in file_list], **kwargs)


