# 更新日志
## fileMapping 0.3.14


# 对比上次更新了什么？
server 新增了 Pull_plugin & Upload_plugin 类，用于插件的下载与上传。

# 如使用？
```python
# __init__.py
import os


from fileMapping import server

path = "plugIns"
# 下载插件
pull = server.Pull_plugin(path, "test")
print(pull.logs)

# 上传插件
server.Upload_plugin(os.path.join(path, "test"), "test", "1.0.0")
print(pull.logs)

```


------

|                    上版本                    |          下版本           |
|:-----------------------------------------:|:----------------------:|
| [0.3.13](update_md%2Fchangelog-0.3.13.md) | [0.3.14](changelog.md) |

