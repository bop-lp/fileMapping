# fileMapping/core/abnormal.py
# abnormal 异常类声明

from typing import List, Any, Union


class Mistake(Exception):
    # 这个是对错误进行记录
    # fileMapping 的异常类，继承自 Exception 类
    # 定义了两个方法，english 和 chinese，分别返回英文和中文的错误信息
    # 英文和中文的错误信息通过列表 listOfLanguages 进行存储
    # 调用时，根据当前语言环境，调用对应的方法返回错误信息
    # 英文在前 中文在后
    listOfLanguages: List[Any]
    stack: str = ''
    # 栈的记录

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.listOfLanguages = [
            self.english, self.chinese
        ]

    def english(self) -> str: ...

    def chinese(self) -> str: ...


class Package(Mistake):
    stack: str = ''
    packageName: str = ''
    def __init__(self, stack: str, packageName: str):
        super().__init__()

        self.stack = stack
        self.packageName = packageName


class PackageImport(Package):
    def english(self) -> str:
        return f"Import package error {self.packageName}"

    def chinese(self) -> str:
        return f"导入包错误 {self.packageName}"


class PackageRun(Package):
    def __init__(self, stack: str, packageName: str, error: str):
        super().__init__(stack, packageName)

        self.error = error

    def english(self) -> str:
        return f"The package is running incorrectly {self.packageName} Error {self.error}"

    def chinese(self) -> str:
        return f"包运行错误 {self.packageName} Error {self.error}"


class PlugIns(Mistake):
    nameOfThePlugin: str

    def __init__(self, nameOfThePlugin: str):
        super().__init__()

        self.stack = ''
        self.nameOfThePlugin = nameOfThePlugin


class PluginDependencies(PlugIns):
    dependenciesOnPlugins: str
    def __init__(self, nameOfThePlugin: str, dependenciesOnPlugins: str):
        super().__init__(nameOfThePlugin)

        self.dependenciesOnPlugins = dependenciesOnPlugins

    def english(self) -> str:
        return f"Plugin dependency error '{self.nameOfThePlugin}' dependence on '{self.dependenciesOnPlugins}' plugIns"

    def chinese(self) -> str:
        return f"插件依赖错误 '{self.nameOfThePlugin}' 依赖 '{self.dependenciesOnPlugins}' 插件"


class PluginLoopsDependencies(PlugIns):
    plugInLoops: Union[list, tuple]

    def __init__(self, plugInLoops: Union[list, tuple]):
        super().__init__('')

        self.plugInLoops = plugInLoops

    def english(self) -> str:
        return f"Plugin circular dependencies error '{self.plugInLoops}'"

    def chinese(self) -> str:
        return f"插件循环依赖错误 '{self.plugInLoops}'"


class pluginEndError(PlugIns):
    error: str
    stack: str
    def __init__(self, nameOfThePlugin: str, error: str, stack: str):
        super().__init__(nameOfThePlugin)

        self.stack = stack
        self.error = error

    def english(self) -> str:
        return f"Plugin end error '{self.nameOfThePlugin}' Error: '{self.error}'"

    def chinese(self) -> str:
        return f"插件结束 '{self.stack}' error:'{self.error}'"


class ParameterApplication(Mistake):
    ApplicationName: str
    error: str
    stack: str

    def __init__(self, ApplicationName: str, error: str, stack: str):
        super().__init__()

        self.ApplicationName = ApplicationName
        self.error = error
        self.stack = stack

    def english(self) -> str:
        return f"Application error: {self.ApplicationName} error: {self.error}"

    def chinese(self) -> str:
        return f"应用错误: {self.ApplicationName} 错误: {self.error}"


class ParameterApplicationRun(ParameterApplication):
    def english(self) -> str:
        return f"Application run error: {self.ApplicationName} error: {self.error}"

    def chinese(self) -> str:
        return f"应用运行错误: {self.ApplicationName} 错误: {self.error}"


class ParameterApplicationEnd(ParameterApplication):
    def english(self) -> str:
        return f"Application end error: {self.ApplicationName} error: {self.error}"

    def chinese(self) -> str:
        return f"应用结束错误: {self.ApplicationName} 错误: {self.error}"


class ParameterApplicationInit(ParameterApplication):
    def english(self) -> str:
        return f"Application init error: {self.ApplicationName} error: {self.error}"

    def chinese(self) -> str:
        return f"应用初始化错误: {self.ApplicationName} 错误: {self.error}"

