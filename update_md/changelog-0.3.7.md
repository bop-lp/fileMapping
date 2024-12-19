# 更新日志
## fileMapping 0.3.7


# 对比上次更新了什么？


在上次更新后，fileMapping.File 中新增了以下参数：

config
- 类型：dict
- 描述：配置文件，将会被映射到 public['config']

printLog
- 类型：bool
- 描述：是否打印日志，默认值为 False

printPosition
- 类型：file-like object
- 描述：日志输出位置，默认值为 sys.stdout 在终端输出



```python

# File
def __init__(self, 
             absolutePath: os.path, 
             screening=None, 
             config: dict = None, 
             printLog: bool =False, 
             printPosition=sys.stdout
    ):
    """
    映射文件夹下的Python[pluginLoading.py](pluginLoading.py)文件或者包
    :param absolutePath: 当前的根目录绝对路径
    :param screening: 要映射的文件夹
    :param config: 配置文件 它将会被映射到 public['config']
    :param printLog: 是否打印日志
    :param printPosition: 日志输出位置 默认为 sys.stdout 在终端输出
    """

```

更新后, 在包中的 `__function__` 可以为空, 表示只调用不运行
```python
# __init__.py

__fileName__ = ''
# __fileName__ 为空时, 表示运行当前文件  __init__.py

__function__ = ''
# __fileName__ 为空时, 只调用不运行

```


|                  上版本                  |           下版本            |
|:-------------------------------------:|:------------------------:|
| [0.3.5](changelog-0.3.5.md) | [0.3.9](../changelog.md) |
