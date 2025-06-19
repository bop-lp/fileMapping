# 装饰器模块
from typing import Union

from types import FunctionType, ModuleType

import time
import functools

from . import helperFunctions
from . import wordProcessing
from . import Class
from . import data


def parameters_wrapper(func, parameters):
    # 参数装饰器
    if parameters is None:
        parameters = {}

    def wrapper(*args, **kwargs) -> dict:
        pa = helperFunctions.parameterFilling(func, {**parameters, **kwargs})
        # 参数填充
        return func(*args, **pa)

    wrapper.__name__ = func.__name__
    return wrapper


def wrapper_recursion(wrapper_list: list, func, parameter_library: dict):
    return wrapper_list[0](parameters_wrapper(func, parameter_library), parameter_library) \
        if wrapper_list.__len__() == 1 \
        else wrapper_recursion(wrapper_list[1:], wrapper_list[0](parameters_wrapper(func, parameter_library)),
                               parameter_library)


def my_wraps(name):
    """
    在层层(包装/装饰)下名字不变

    :param name: 名字
    """

    def decorator(func):
        func.__name__ = name

        return func

    return decorator


class TimeWrapper(Class.TimeWrapper):
    def __init__(self):
        self.data = Class.TimeWrapperData()

    def wrapper(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.data[func.__name__] = Class.PluginTimestamp(
                **{
                    "init": start_time,
                    "end": end_time,
                    "take": end_time - start_time
                }
            )
            return result

        return wrapper

    def get_data(self, func_id):
        return self.data.get(func_id, None)


class InfoWrapper(Class.InfoWrapper):
    def __init__(self, info_dict):
        """
        信息装饰器
        可以快速的获取 file_object 的信息
        :param info_dict: 信息字典
            - 文件信息字典 {infoName: messageDefaults, ...}
        """
        self.info_dict = info_dict if not info_dict is None else {}
        self.data = Class.InfoWrapperData()

    def wrapper(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            self.data[func.__name__] = Class.PlugInRetention(wordProcessing.get_file_info(result.pack, self.info_dict))

            return result

        return wrapper


# 注册函数
def appRegistration(nameOfThePlugin: str, name: str = None):
    """
    注册函数装饰器
    :param nameOfThePlugin: 插件名
    :param name: 函数名字  默认为 None 则为函数名
    """

    def func_wrapper(func: Class.ParameterApplication) -> Class.ParameterApplication:
        # 这里是插件注册数据
        # parameterApplication => {<插件名字>: {<函数名字>: [FunctionType], ...}, ...}
        if not data.plugInData.parameterApplication.get(nameOfThePlugin):
            data.plugInData.parameterApplication[nameOfThePlugin] = {}

        # 这里是函数注册数据
        data.plugInData.parameterApplication[nameOfThePlugin][func.__name__ if name is None else name] = func

        return func

    return func_wrapper


def tagAppRegistration(nameOfThePlugin: str) -> appRegistration:
    """
    可以标记插件的注册函数
    基于 appRegistration 进行装饰
    :param nameOfThePlugin: 插件名
    """

    def wrapper_wrapper(name: str = None):
        return appRegistration(nameOfThePlugin, name)

    return wrapper_wrapper


__all__ = [
    "parameters_wrapper",
    "wrapper_recursion",
    "my_wraps",
    "TimeWrapper",
    "InfoWrapper",
]
