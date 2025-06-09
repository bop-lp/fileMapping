

# fileMapping

我们为什么要推出这个分支?

- 在我的长时间的开发中发现 fileMapping 已经是一个屎山了
- 而且难以维护并且难以继续开发更多的功能
- 并且文档写的也不够清楚 类的继承也非常的混乱
- 数据存放的地方也不够清晰

所以我决定对这个项目进行重构
-- 2025.06.07


---


## 项目简介


可以指定一个文件夹然后将里面的库(python)或者是Python文件快速调用

然后按照一定的规则进行运行

还提供了一些 API/接口 来进行一定的管理

## 项目安装

```shell
pip install fileMapping
```

使用清华镜像源
```shell
pip install fileMapping -i https://pypi.tuna.tsinghua.edu.cn/simple
```


## 开发文档

```text
fileMapping
└─ document                     // 文档目录
    ├─ development.md           // 开发文档
    ├─ illustrate.md            // 项目说明文档
    └─ pluginDevelopment.md     // 插件开发文档
```



### 开发文档 [development.md](document/development.md)



### 项目说明文档 [illustrate.md](document/illustrate.md)

项目说明最主要是对这个项目从结构上以及程序的运行上来说明

~~相当于对我的注释 最主要是我怕忘了，我自己要看~~

**[点击跳转](document/illustrate.md)**


### 插件开发文档 [pluginDevelopment.md](document/pluginDevelopment.md)

这个对于插件开发的一些规范以及提供的API/接口 以及特殊参数等

**[点击跳转](document/pluginDevelopment.md)**
