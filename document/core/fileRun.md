# fileMapping 运行说明


# 运行前准备

```text
文件结构:

<插件名字>
    ├─ config.py  # -> 配置文件 (可选)
    ├─ .config    # -> 配置目录 (可选)
    ├─ .plugins   # -> 插件目录 (可选)
    └─ main.py    # -> 一个项目的中心文件，调用 fileMapping 进行文件映射 (可选)
```

## 

```python
# main.py

import fileMapping


config = {
    "multithreading": True,  # 是否启用多线程
}
# 这个是fileMapping的配置，可以根据需要进行修改
# 可以在 fileMapping/core/config.py 中查看默认配置

plugins = {
    "plugin1": {
        # 插件1的配置
        # 这里写插件的配置 一般在插件的config.py中查看
    }
}
# 这里可以是一个字典, key为插件的名字, value为插件的配置
# 一般插件的配置都在插件的config.py中查看
# 也可以是一个绝对路径文件夹 (这个是内置插件的功能 fileConfig)
# 当是一个文件夹时文件夹下 文件应该为 <插件名字>.py 格式的文件
# 更具体应该查看fileConfig 的文档


file = fileMapping.File(
    fileMapping.pathConversion(__file__, ".plugins"),  # 插件目录
    # pathConversion 可以使用pathConversion函数将相对路径转换为绝对路径
    config,  # fileMapping的配置
    plugins,  # 插件的配置
)
file.runAll()  # 运行所有插件
# file.runOne("plugin1")  # 运行单个插件 (插件名字)
```


## 运作流程

`File` 的初始化函数 `__init__` 接收三个参数:

生成全部插件的绝对路径经历函数 
`helperFunctions.pathValidation` `helperFunctions.__fileFiltering__` `helperFunctions.dictMerge`
`helperFunctions.configConvertTodict` `helperFunctions.deep_update`

过滤禁用插件写在`core.fileMain.File` 中的 `listOfDiles`

运行插件的 `init` 函数由 `__multithreading__` `__singleThreaded__` 这两个函数中的一个进行调用运行

由 `getPluginConfig` 函数获取插件的配置加载到 `self.pluginsConfig` 中

加载 `parameterApplication.ApplyParameter` 

`ApplyParameter` [文档查看](ApplyParameter.md)