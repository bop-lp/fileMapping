import asyncio
import inspect

from typing import Callable, Any
from typing import List

import rich

from . import helperFunctions



class AsyncTaskRun:
    """
    异步任务运行器
    """
    def __init__(self, listOfFunctions: List[Callable]):
        self.listOfFunctions = listOfFunctions

    async def run(self) -> List[Any]:
        """
        运行异步任务：并发执行所有协程函数，返回结果列表
        :return: 所有任务的执行结果列表，顺序与输入函数列表一致
        """
        coroutines = [func() for func in self.listOfFunctions]
        results = await asyncio.gather(*coroutines)

        return results


def run_functions_decoration(func, **kwargs) -> Callable:
    """
    装饰函数，用于运行给定的函数或协程函数，并填充参数
    """

    kwargs = helperFunctions.parameterFilling(func, kwargs)
    # parameterFilling 函数用于将函数的参数填充到 kwargs 中，如果参数不足则使用默认值
    async def wrapper():
        if inspect.iscoroutinefunction(func):
            # 判断是否为协程函数
            return await func(**kwargs)

        else:
            return func(**kwargs)

    return wrapper


def async_packaging(listOfFunctions: List[Callable], **kwargs) -> AsyncTaskRun:
    """

    :param listOfFunctions:
    :param kwargs:
    :return:
    """
    processing = [
        run_functions_decoration(i, **kwargs) for i in listOfFunctions
    ]

    return AsyncTaskRun(processing)

