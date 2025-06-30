import os
import shutil
import traceback
from typing import Dict, Optional

from fileMapping.core import parameterApplication
from fileMapping.core import Class
from fileMapping.core import abnormal
from fileMapping.core import decorators
# 导入fileMapping的核心模块
from fileMapping.core import File

from . import helperFunctions
from . import config



@parameterApplication.wrapper
class TemporaryFolders(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.config = self.self_info.plugInData.Folders.config
        self.tempFolderPath = False
        self.whetherItIsSelfCreated = False
        self.createDict: Dict[str, str] = {}
        # 文件列表

        if self.config["tempFolderPath"] in [None, '', False]:
            # 是否开启临时文件夹路径
            return

        if not os.path.isdir(os.path.isdir(self.config.tempFolderPath)):
            # 临时文件夹路径是否存在
            # 存在则不创建
            # 返回绝对路径
            _ = helperFunctions.mkdir(self.config.tempFolderPath)
            if isinstance(_, abnormal.FolderCreationFailed):
                self.self_info.logData.parameterApplication.append(_)
                return

        self.tempFolderPath = os.path.realpath(self.config.tempFolderPath)
        self.self_info.plugInData.Folders.TemporaryFolders = {}
        # 文件夹列表

        decorators.appRegistration(config.__name__)(helperFunctions.wrapper(self)(dynamicTemporaryFolders))


    def init(self):
        if isinstance(self.tempFolderPath, bool):
            return

        self.createDict = helperFunctions.statistics(self.config.tempFolderPath, self.self_info.plugInRunData.information.file_info)

        for key, path in self.createDict:
            returnValue = helperFunctions.mkdir(os.path.join(self.tempFolderPath, path))
            if isinstance(returnValue, abnormal.FolderCreationFailed):
                self.self_info.logData.parameterApplication.append(returnValue)
                continue

            self.self_info.plugInData.Folders.TemporaryFolders[key] = path


    def end(self):
        for key, path in self.createDict:
            _ = helperFunctions.delete(path)
            if isinstance(_, abnormal.FolderDeletion):
                self.self_info.logData.parameterApplication.append(_)


@decorators.appRegistration(config.__name__)
def getTemporaryFolders(path: str) -> Optional[str]:
    if not File.plugInData.get("Folders", False):
        # 没有Folders插件
        return None

    if not File.plugInData.Folders.get("TemporaryFolders", False):
        # 没有运行 TemporaryFolders
        return None

    return File.plugInData.Folders.TemporaryFolders.get(path, None)


def dynamicTemporaryFolders(self: TemporaryFolders, path: str):
    """
    动态创建临时文件夹
    :param self:
    :param path:
    :return:
    """

    returnValue = helperFunctions.mkdir(os.path.join(self.tempFolderPath, path))
    if isinstance(returnValue, abnormal.FolderCreationFailed):
        return returnValue

    self.self_info.plugInData.Folders.TemporaryFolders[path] = returnValue
    self.createDict[path] = returnValue
    return returnValue

