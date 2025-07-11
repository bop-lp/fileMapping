# 项目说明文档

请注意这里的文档具有时效性

简单来说就是我不会对这个文档做的更新 偶尔做一次 ~~诶嘿~~

所以呢 `点击标题`跳转到`相关的代码`然后具体查看

## 项目文件结构树

```text
fileMapping
  ├─ README.md
  ├─ __init__.py
  ├─ document             // 文档目录
  ├─ builtInPlugins       // 内置插件目录
  └─ core                 // 核心代码目录
```

```text
core
 ├─ abnormal.py                      // 异常处理模块
 ├─ Class.py                         // 类定义模块
 ├─ config.py                        // 配置模块
 ├─ data.py                          // 数据存放
 ├─ decorators.py                    // 装饰器模块
 ├─ fileImport.py                    // python文件导入模块
 ├─ fileMain.py                      // 文件主模块
 ├─ helperFunctions.py               // 辅助函数模块
 ├─ multiThreadedHelperFunctions.py  // 多线程辅助函数模块
 ├─ multithreading.py                // 多线程模块
 ├─ parameterApplication.py          // 参数应用模块
 ├─ wordProcessing.py                // 文字处理模块
 └─ __init__.py

```

## 文件列表

### [abnormal.py](../core/abnormal.py)

异常处理模块，定义了一些异常类，用于处理程序运行过程中出现的异常

```text
Mistake(Exception)                    // 错误基类
 ├─ Package                           // 包错误基类
 |   ├─ PackageImport                    // 包导入错误
 |   └─ PackageRun                       // 包运行错误
 ├─ PlugIns                           // 插件错误基类
 |   ├─ PluginDependencies               // 插件依赖错误
 |   └─ PluginLoopsDependencies          // 插件循环依赖错误
 └─ ParameterApplication              // 参数应用错误基类
     ├─ ParameterApplicationRun          // 参数应用运行错误
     ├─ ParameterApplicationEnd          // 参数应用结束错误
     └─ ParameterApplicationInit         // 参数应用初始化错误
```
```python
class Mistake(Exception):
    listOfLanguages: List[Any]
    stack: str = ''

    def __init__(self, *args: Any, **kwargs: Any):
        self.listOfLanguages = [
            self.english, self.chinese
        ]

    def english(self) -> str: ...

    def chinese(self) -> str: ...
```

`Mistake.listOfLanguages` 是用于存储多语言错误信息的列表

`Mistake.stack` 是用于存储异常堆栈信息的字符串

`english` 和 `chinese` 是 英文和中文错误信息的函数 请`english`保持在第一位


### [Class.py](../core/Class.py)

类定义模块，定义了一些类，用于IED的提醒

类的继承关系如下：
```text
FilemappingDict
 ├─ LogData
 ├─ PlugInData
 ├─ ConfigData
 ├─ PlugIns
 |   ├─ PluginTimestamp
 |   ├─ TimeWrapperData
 |   ├─ PlugInRetention
 |   ├─ InfoWrapperData
 |   ├─ CallObject
 |   ├─ Invoke
 |   ├─ RunTime
 |   ├─ FileInfo
 |   ├─ Information
 |   └─ PlugInRunData
 ├─ ReturnValue
 ├─ File
 └─ RegisterData
```

这个是我自认为的关系


```text
File                                 // 核心类
 ├─ EnableMultithreading               // 多线程类
 ├─ ConfigData                         // 配置数据类
 ├─ plugInRunData                      // 插件运行数据类
 |   ├─ CallObject                       // 调用对象数据类
 |   |   └─ Module                         // 模块数据类
 |   ├─ Invoke                           // 调用数据类
 |   |   └─ ModuleType                     // 模块类型数据(python的内置类)
 |   └─ Information                      // 插件信息数据类
 |       ├─ RunTime                        // 运行时间数据类
 |       |   └─ PluginTimestamp              // 插件时间戳数据类
 |       └─ FileInfo                      // 插件信息数据类
 |           └─ PlugInRetention             // 插件保留数据类
 ├─ ReturnValue
 ├─ LogData
 |   └─ Mistake
 ├─ PlugInData
 └─ ConfigData

Decorators                         // 装饰器类
 ├─ TimeWrapper                      // 时间装饰器
 |   └─ TimeWrapperData                // 时间装饰器数据
 |       └─ PluginTimestamp               // 插件时间戳数据
 └─ InfoWrapper                      // 信息装饰器
      └─ InfoWrapperData                // 信息装饰器数据
           └─ PlugInRetention               // 插件保留数据

RegisterData                        // 注册数据
 ├─ EndFunc                            // 结束函数
 |   └─ File                             // 核心类
 └─ ParameterApplication              // 参数应用类
```

### [config.py](../core/config.py)

配置模块，定义了一些配置变量，用于控制程序的运行

[config.md](core/config.md)


### [data.py](../core/data.py)

数据存放模块，定义了一些数据类，用于存储程序运行过程中产生的数据
```text
 /
 ├─ PluginData         // 插件数据类
 ├─ LogData            // 日志数据类
 ├─ ConfigData         // 配置数据类
 └─ ReturnValue        // 插件运行返回值数据类
```

#### LogData 类属性

```text
LogData
 ├─ fileMapping (list[Mistake])             // fileMapping 日志数据类
 ├─ parameterApplication (list[Mistake])    // 参数应用日志数据类
 └─ plugInConfiguration (list[Mistake])     // 插件配置日志数据类

```


### [decorators.py](../core/decorators.py)

装饰器模块，定义了一些装饰器类

```text
 /
 ├─ TimeWrapper                  // 时间装饰器
 └─ InfoWrapper                  // 信息装饰器
```


### [fileImport.py](../core/fileImport.py)

python文件导入模块，定义了一些函数，用于导入python文件

```python
def py_import(file_path: os.path, callObject: str) -> Union[ModuleType, abnormal.PackageImport]:
    """
    在 importlib.import_module 中有一个缓存机制
    如果 sys.module 中有这个包，就会直接返回这个包
    所以需要在 sys.module 中 临时删除这个包 然后再重新导入
    :param file_path: 绝对路径
    :param callObject: 'main'
    :return:

    """
    callObject = callObject.split('.')[0]  # 去除 .py
    # 检查 sys.module 中是否有这个包
    temporaryPackages = False
    if callObject in sys.modules:
        temporaryPackages = sys.modules[callObject]
        del sys.modules[callObject]

    try:
        sys.path.append(file_path)
        the_api = importlib.import_module(callObject)

    except Exception:
        the_api = abnormal.PackageImport(traceback.format_exc(), file_path)

    if not isinstance(temporaryPackages, bool):
        # 恢复 sys.module 中原来的包
        sys.modules[callObject] = temporaryPackages

    sys.path = sys.path[:-1]  # 去除 sys.path 中最后一个路径
    return the_api

```

所以本质上与Python的导入没有区别


### [fileMain.py](../core/fileMain.py)

`File`

1. 检查参数的合法性

2. 合并提交的配置文件与默认配置文件

3. 获取需要加载的全部插件

4. 提交给多线程或单线程

#### File 类属性

```text
File
 ├─ config                                // 配置数据类 一般是core/config.py
 ├─ configData                            // 好像是我写错了 应该没有这个属性 实际这个属性没有用到 | 也没有什么属性
 ├─ logData (LogData[str, list] -> dict)  // 日志数据类
 |   ├─ fileMapping                           // fileMapping 日志数据类
 |   ├─ parameterApplication                  // 参数应用日志数据类
 |   └─ plugInConfiguration                   // 插件配置日志数据类
 ├─ multithreading                        // 多线程类
 ├─ path (list[str)                       // 运行插件路径列表(文件夹)
 ├─ plugInData                            // 插件数据类
 ├─ plugInRunData                            // 插件运行数据类
 |   ├─ CallObject                              // 调用对象数据类
 |   |   └─ Module                                 // 模块数据类
 |   ├─ Invoke                                  // 调用数据类
 |   |   └─ ModuleType                             // 模块类型数据(python的内置类)
 |   ├─ moduleAbnormal (list[插件异常数据类])     // 模块异常数据类
 |   ├─ pluginConfig (dict[插件配置数据类])       // 插件配置数据类
 |   └─ Information                             // 插件信息数据类
 |       ├─ RunTime                                // 运行时间数据类
 |       |   └─ PluginTimestamp                       // 插件时间戳数据类
 |       └─ FileInfo                               // 插件信息数据类
 |           └─ PlugInRetention                       // 插件保留数据类
 └─ returnValue                           // 插件运行(__init__)返回值数据类
```

fileMapping 的运行
[查看文档](core/fileRun.md)



### [helperFunctions.py](../core/helperFunctions.py)

辅助函数模块，定义了一些函数，用于辅助程序的运行

### [multiThreadedHelperFunctions.py](../core/multiThreadedHelperFunctions.py)

多线程辅助函数模块，定义了一些函数，用于辅助多线程程序的运行

### [multithreading.py](../core/multithreading.py)

~~这个我有点懒得 写所以交给AI字想了~~

~~有点懒得写了 不懂的机会，AI求求了~~

[multithreading.md](core/multithreading.md)


### [parameterApplication.py](../core/parameterApplication.py)

参数应用模块，定义了一些类，用于应用参数


### [wordProcessing.py](../core/wordProcessing.py)

文字处理模块，定义了一些函数，用于处理文字

