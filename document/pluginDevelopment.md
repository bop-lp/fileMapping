# 插件开发文档


## 目录



## 介绍

本文档介绍了插件开发相关的知识，包括插件的开发流程、插件的目录结构、插件的配置文件、插件的运行方式等。


## 开发流程


一般来说插件单个文件或者文件夹的形式存在

`单个文件` 的插件一般是轻量化的插件

`包/库` 的插件一般是功能性或者复杂的插件 **(推荐使用)**


### 文件 的插件


文件的形式一个的单个文件 如：`plugin.py`

后缀一般是 `.py` 可以是 `.pyc` `.pyi`

参数管理在 `fileMapping/core/config.py` 文件中的 `screening` 参数


### 包/库 的插件


文件夹的形式的一般是文件夹下有一个 `__init__.py` 文件

参数管理写死在 `fileMapping/core/helperFunctions.py` 文件中的 `__fileFiltering__` 函数


## 保留参数 / 关键词

保留参数是 `插件` 运行时在第一层变量

最主要的几个变量
- `__init__`
- `__level__`
- `__dependenciesOnPlugins__`

```python
# 保留参数的使用例子
# 这里如果是文件形式的就在文件里中写
# 这里如果是包/库形式的就在 __init__.py 文件中写
from fileMapping.core import Class


def init(fileMapping: Class.File):  # fileMapping 在运行init函数的时候会给File类参数名为fileMapping(可选)
    ...

__init__ = init

__level__ = 3

__dependenciesOnPlugins__ = "<插件名字>"

```

对于 [保留参数/关键词 文档](https://github.com/fileMapping/keyword)



## 包/库 的插件目录结构

```text

(插件名字)
    ├── __init__.py
    ├── config.py (可选 建议有)
    └─ ...

```



## 错误类

写一个错误信息类

可以查看 [illustrate.md](illustrate.md#文件列表)



```python
from fileMapping.core import abnormal


class mistake(abnormal.Mistake):
    listOfLanguages: list  # 错误发生的语言列表 一般不要更改 默认第一个是英文
    stack: str  # 错误的堆栈信息
    
    def __init__(self, listOfLanguages: list, stack: str, *args, **kwargs):
        super().__init__()
    
    def english(self) -> str: ...
    
    def chinese(self) -> str: ...
```



## logs / 日志

这个是插件怎么记录日志的

这个是 LogData 类基础属性

`LogData`的类属性查看 [illustrate.md](illustrate.md#logdata-类属性)

### 插件写入日志


使用前提条件

使用的是在`fileMapping`[运行](core/fileRun.md)后的`File`类

```python
from fileMapping.core import Class
from fileMapping.core import abnormal


def init(fileMapping: Class.File):
    logInformation: abnormal.Mistake = abnormal.Mistake()
    # 错误信息日志
    namePlugin: str = "xxx"
    # 插件名字 一般是在 config 文件中配置的
    
    fileMapping.logData[namePlugin]: list = []  # 创建创建的日志列表
    fileMapping.logData[namePlugin].append(logInformation)

```


## 数据类

插件运行过程中产生的数据类

可以使用 `data.LogData` 类

```python

from fileMapping.core import helperFunctions


data = helperFunctions.getPluginDataSpace("pluginName")
# 这里的 pluginName 是插件名字
# 这个函数会返回一个 fileMapping 的 FilemappingDict 类
# 这个类可以用来存储插件运行的数据(需要和其他的插件共享数据 可以使用这个方法)

```


## API

### fileMapping

`fileMapping` 的api是在core.helperFunctions文件的

[API 文档](illustrate.md#helperfunctionspy)

### 插件自定义API
使用 `decorators.appRegistration` 的函数

```python
from fileMapping.core import decorators

namePluins = "ABC" # 插件名字
name = "add"  # 可选 默认为函数名字

@decorators.appRegistration(namePluins, name)
def addition(a, b):
    return a + b
```

使用 `decorators.tagAppRegistration` 的函数

这个适用于批量的注册

```python
from fileMapping.core import decorators

namePluins = "ABC" # 插件名字
wrapper = decorators.tagAppRegistration(namePluins)


@wrapper()
def add_list(*args):
    _ = 0
    for i in args:
        _ += i
    return _

@wrapper()
def add(a, b):
    return a + b
```

### 获取API

```python
from fileMapping.core import helperFunctions


add = helperFunctions.getAppRegister("ABC", "add")
if add == None:
    # 没有这个API
    # 需要检查插件是否有运行或者插件的版本
    ...
    # 异常处理模块

i = add(1, 6)
print(i)
# 预期输出 7
```

