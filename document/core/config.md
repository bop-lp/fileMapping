# [config.py](../../core/config.py)

这里面的 `functionsName` 和 `functions` 分别具有命名错误

这个是在之前的版本造成的  ~~我也不敢改~~

`functionsName` 这个是保留参数 会有一些意想不到的效果

`functions` 这个是对应保留参数的默认值


这些我是从原来的项目copy过来的 

所以一些可能有一些用不到


在创建这个`核心类` `(Class.File)`的时候

```python
from fileMapping import Class

class File(Class.File):
    def __init__(self, path: Union[str, list], config: dict, pluginConfig: Union[dict, list]): ...
```

`config` 这个就是用于给定这个 config.py 的配置参数 

在`核心类(File)`中调用了这个函数 `helperFunctions.configConvertTodict` 然后进行了转换 然后再做了深度合并 以提供了参数为主


模块在哪里导入时会生成这些参数?

会在 `decorators.InfoWrapper` 中的 `get_file_info` 生成


## 保留参数

`保留参数` 在这个文档中不会更新了

[点击跳转](https://github.com/fileMapping/keyword)
