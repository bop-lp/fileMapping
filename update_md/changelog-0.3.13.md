# 更新日志
## fileMapping 0.3.13


# 对比上次更新了什么？

- `__level__` 新增，用于控制导入插件的级别，默认为 `-1` 
用于控制导入插件的级别，默认为 `-1` ，`-1` 表示最低级别
由库作者决定是否使用 

# 如使用？
```python
# __init__.py


def end():
    print('程序结束')

__level__ = 5 # 设置级别为 5

```


------

|              上版本              |              下版本              |
|:-----------------------------:|:-----------------------------:|
| [0.3.11](changelog-0.3.11.md) | [0.3.14](changelog-0.3.14.md) |

