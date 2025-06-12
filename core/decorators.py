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



def functionRegistrations(name: str = None):
    def func_wrapper(func: Union[FunctionType, ModuleType]):
        # 注册函数
        data.plugInData.decorators.functionRegistrations.append(Class.FunctionTypeData(
            func.__name__ if name is None else name, func
        ))

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return func_wrapper



# parameterApplication 的装饰器
def appRegistration(name: str=None):
    """
    参数应用装饰器
    将数据放入 data.plugInData.parameterApplication 中
    然后由 parameterApplication.py 的函数进行处理
    """
    def func_wrapper(func: Class.ParameterApplication) -> Class.ParameterApplication:
        data.plugInData.parameterApplication[func.__name__ if name is None else name] = func

        return func
    return func_wrapper


__all__ = [
    "parameters_wrapper",
    "wrapper_recursion",
    "my_wraps",
    "functionRegistrations",
    "TimeWrapper",
    "InfoWrapper",
]

