# [config.py](../../core/config.py)

这里面的 `functionsName` 和 `functions` 分别具有命名错误

这个是在之前的版本造成的  ~~我也不敢改~~

`functionsName` 这个是保留参数 会有一些意想不到的效果

`functions` 这个是对应保留参数的默认值

```python
functionsName = {
    # 保留参数
    "__fileName__": "__fileName__",
    "__function__": "__init__",
    "__run__": "__run__",
    "__end__": "__end__",
    "__level__": "__level__",
    "__init__.py": "__init__.py",
    "__init__": "__init__.py",
    "__version__": "__version__",
    "__dependenciesOnPlugins__": "__dependenciesOnPlugins__",
    "__temporaryFolders__": "__temporaryFolders__",
    "__error__": "__error__",
    "__underlying__": "__underlying__",
    "__dataFolders__": "__dataFolders__"
}

functions = {
    # 保留参数
    "__fileName__": None,
    "__function__": "main",
    "__run__": True,
    "__end__": 'end',
    "__level__": -1,
    "__init__.py": "__init__.py",
    "__init__": "__init__.py",
    "__version__": None,
    "__dependenciesOnPlugins__": [],
    "__temporaryFolders__": None,
    "__error__": None,
    "__underlying__": False,
    "__dataFolders__": None
}

multithreading: bool = True
# 是否开启多线程
numberOfThreads: int = 4
# 线程数 - 合理的线程数 4 - 6

```


这些我是从原来的项目copy过来的 

所以一些可能有一些用不到


在创建这个`核心类` `(Class.File)`的时候

```python
class File(Class.File):
    def __init__(self, path: Union[str, list], config: dict): ...
```

`config` 这个就是用于给定这个 config.py 的配置参数 

在`核心类(File)`中调用了这个函数 `helperFunctions.configConvertTodict` 然后进行了转换 然后再做了深度合并 以提供了参数为主


模块在哪里导入时会生成这些参数?

会在 `decorators.InfoWrapper` 中的 `get_file_info` 生成

[保留参数](preserveParameters.md)
