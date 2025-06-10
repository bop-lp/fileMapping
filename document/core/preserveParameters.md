<!-- TOC -->
* [保留参数](#保留参数)
  * [保留参数列表](#保留参数列表)
  * [`__fileName__`](#__filename__)
  * [`__init__`](#__init__)
  * [`__run__`](#__run__)
  * [`__end__`](#__end__)
  * [`__level__`](#__level__)
  * [`__init__.py`](#__init__py)
  * [`__version__`](#__version__)
  * [`__dependenciesOnPlugins__`](#__dependenciesonplugins__)
  * [`__temporaryFolders__`](#__temporaryfolders__)
  * [`__error__`](#__error__)
  * [`__underlying__`](#__underlying__)
  * [`__dataFolders__`](#__datafolders__)
<!-- TOC -->

---

# 保留参数

```text
- 参数名称: 
- 是否必须: 
- 加入版本: 
- 类型: 
- 默认值: 
- 描述: 
```

## 保留参数列表


## `__fileName__`

- 参数名称: 插件名称
- 是否必须: 否
- 加入版本: init
- 类型: str
- 默认值: None


## `__init__`

- 参数名称: 插件初始化函数
- 是否必须: 否
- 加入版本: 0.4.0
- 类型: str | FunctionType
- 默认值: None
- 描述: 
  - 当是字符串是会在这个插件中寻找相同名字的 FunctionType
  - 当是 FunctionType 则直接使用这个函数作为插件的初始化函数


## `__run__`

- 参数名称: 是否运行
- 是否必须: 否
- 加入版本: 0.3.3
- 类型: bool
- 默认值: True
- 描述: 
  - 用于指定是否运行插件, 默认为True
  - 当为False时, 插件不会运行, 但会被加载到内存中
  - 一般由API进行使用


## `__end__`

- 参数名称: 结束函数
- 是否必须: 否
- 加入版本: 0.3.11
- 类型: str | object
- 默认值: None
- 描述: 用于指定插件结束时的函数, 一般用于清理工作


## `__level__`

- 参数名称: 导入等级
- 是否必须: 否
- 加入版本: 0.3.13
- 类型: int
- 默认值: -1
- 描述: 插件的导入等级, 用于控制插件的导入顺序, 值越小越先导入, 值相同则根据文件名的字母顺序进行导入


## `__init__.py`

- 参数名称: 忘了
- 是否必须: 否
- 加入版本: 0.3.14
- 类型: str
- 默认值: `__init__.py`
- 描述: 不知道


## `__version__`

- 参数名称: 插件版本
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: str
- 默认值: None
- 描述: 插件的版本号, 用于标识插件的不同版本


## `__dependenciesOnPlugins__`

- 参数名称: 依赖插件
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: list | dict
- 默认值: []
- 描述: 
  - 用于指定插件运行所需的依赖插件
  - dict 类型时, 格式为 {"pluginName": "version", ...}
  - list 类型时, 格式为 ["pluginName", "pluginName", ...]


## `__temporaryFolders__`

- 参数名称: 临时文件夹
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: str | list
- 默认值: None
- 描述: 
  - 用于申请一个临时文件夹
  - fileMapping 会在init时申请一个临时文件夹, 并在插件结束时删除
  - fileMapping.temporaryFolders() 会返回申请的临时文件夹路径
  - 无法动态申请


## `__error__`

- 参数名称: 错误处理函数
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: object
- 默认值: None
- 当运行插件错误时会进行运行该函数


## `__underlying__`

- 参数名称: 底层插件
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: bool
- 默认值: False
- 描述:
  - 用于指定插件是否为底层插件
  - 允许插件修改 fileMapping 的类 & 方法
  - `__function__`(main) 需要一定格式(dict), 不然无法更改


## `__dataFolders__`
- 参数名称: 数据文件夹
- 是否必须: 否
- 加入版本: 0.3.15
- 类型: str | list
- 默认值: None
- 描述: 
  - 用于申请一个数据文件夹
  - fileMapping 会在init时生成一个数据文件夹
  - 会返回申请的临时文件夹路径
  - 无法动态申请
