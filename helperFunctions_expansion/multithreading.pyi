import concurrent.futures


def threadPools(task: dict, max_workers: int=3, callback_function=None, errorHandling=None)-> dict:
    """
    多线程处理
    :param task: 任务字典
    :param max_workers: 最大线程数
    :param callback_function: 回调函数
    :param errorHandling: 错误处理函数
    :return: 处理结果字典
    """


class enableMultithreading:
    def __init__(self, max_workers: int=3, callback_function=None, errorHandling=None):
        """
        多线程装饰器
        """
        self.executor = None
        self.executor: concurrent.futures.ThreadPoolExecutor

    def task_run(self, task_list: list, clogging: bool = True, wrapper_list: list=None, parameters: dict = None) -> list: ...

    def task_recursion(self, task_dict: dict, clogging: bool = True, wrapper_list: list = None, parameters: dict = None) -> dict: ...

    def close(self): ...

    def __func__(self, func, **kwargs): ...
