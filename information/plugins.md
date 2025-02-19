<!-- TOC -->
  * [`fileMapping`](#filemapping)
  * [插件内定参数](#插件内定参数)
    * [`__fileName__` = str](#__filename__--str)
    * [`__version__` = int](#__version__--int)
    * [`__run__` = bool](#__run__--bool)
    * [`__end__` = object](#__end__--object)
    * [`__dependenciesOnPlugins__` = list | dict](#__dependenciesonplugins__--list--dict)
    * [`__temporaryFolders__` = str | list](#__temporaryfolders__--str--list)
    * [`__error__` = object](#__error__--object)
    * [`__underlying__` = bool](#__underlying__--bool)
<!-- TOC -->


## `fileMapping`
更详细的说明

[//]: # (# 参数名称:)

[//]: # (# 是否必须:)

[//]: # (# 加入版本:)

[//]: # (# 类型:)

[//]: # (# 默认值:)

[//]: # (# 描述:)

## 插件内定参数

### `__fileName__` = str

- 参数名称: 插件名称
- 是否必须: 否
- 加入版本: init
- 类型: str
- 默认值: main
- 在之前的版本(0.3.8)中是用于导入时指定目标文件和 `__function__` 使用
- 现版本(0.3.8以上)已经弃用


### `__version__` = int
- 参数名称: 插件版本
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: str
- 默认值: 1
- 描述: 插件的版本号, 用于标识插件的不同版本


### `__run__` = bool
- 参数名称: 是否运行
- 是否必须: 否
- 加入版本: 0.3.3
- 类型: bool
- 默认值: True
- 描述: 用于指定是否运行插件, 默认为True
- 当为False时, 插件不会运行, 但会被加载到内存中
- 一般由API进行使用


### `__end__` = object
- 参数名称: 结束函数
- 是否必须: 否
- 加入版本: 0.3.11
- 类型: object
- 默认值: None
- 描述: 用于指定插件结束时的函数, 一般用于清理工作


### `__dependenciesOnPlugins__` = list | dict
- 参数名称: 依赖插件
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: list | dict
- 默认值: []
- 描述: 用于指定插件运行所需的依赖插件
- dict 类型时, 格式为 {"pluginName": "version", ...}
- list 类型时, 格式为 ["pluginName", "pluginName", ...]


### `__temporaryFolders__` = str | list
- 参数名称: 临时文件夹
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: str | list
- 默认值: None
- 描述: 用于申请一个临时文件夹
- fileMapping 会在init时申请一个临时文件夹, 并在插件结束时删除
- fileMapping.temporaryFolders() 会返回申请的临时文件夹路径
- 无法动态申请


### `__error__` = object
- 参数名称: 错误处理函数
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: object
- 默认值: None
- 当运行插件错误时会进行运行该函数


### `__underlying__` = bool
- 参数名称: 底层插件
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: bool
- 默认值: False
- 描述:
- 用于指定插件是否为底层插件
- 允许插件修改 fileMapping 的类 & 方法
- `__function__`(main) 需要一定格式(dict), 不然无法更改