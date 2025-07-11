# ApplyParameter


这个 `fileMapping` [运行](fileRun.md)之后才运行 `ApplyParameter` 

`ApplyParameter` 是一个用于处理插件的`config` `run` `init` 等等...


如何注册一个 `ApplyParameter`
```python
from fileMapping.core.parameterApplication import wrapper

from fileMapping.core import Class

@wrapper
class MyApplyParameter(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)
        ...

    def init(self):
        """
        这个函数会在 `fileMapping` 运行之后运行
        """
        ...

    def end(self):
        """
        这个函数会在程序结束之后运行
        """
        ...
```

这个有什么用?

在 `Folders` 插件中 `ApplyParameter` 用于处理数据文件夹和临时数据文件夹

在 `fileConfig` 插件中 `ApplyParameter` 用于处理 `config.py` 文件

