# 更新日志
## fileMapping 0.3.9


# 对比上次更新了什么？

- 重写 pluginLoading.impo 的导入逻辑
- 重写 pluginLoading.method.importThePackage 的导入逻辑
- 重写 pluginLoading.method.run
- config.py 新增参数
- 移除 `__fileName__`



# 旧版本的功能变更

```python
# 0.3.7 之前的版本

from plugins.C import api


```
```python
# 0.3.7 之后的版本

from C import api


```

------

|                 上版本                  |          下版本          |
| :-------------------------------------: |:---------------------:|
| [0.3.7](changelog-0.3.7.md) | [0.3.9](changelog.md) |

