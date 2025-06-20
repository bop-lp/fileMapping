import os
import shutil
import traceback
from typing import Optional

from fileMapping.core import parameterApplication
from fileMapping.core import Class
from fileMapping.core import abnormal
from fileMapping.core import decorators
#
from fileMapping.core import File

from . import helperFunctions
from . import config


@parameterApplication.wrapper
class DataFolder(Class.ParameterApplication):
    def __init__(self, parent: Class.File):
        super().__init__(parent)

        self.dataFolder: bool = True
        self.filePath = self.self_info.plugInData.Folders.config["dataFolderPath"]
        self.createList = []
        # 文件列表
        self.self_info.plugInData.Folders.DataFolder = {}
        # 文件夹列表

        if self.dataFolder in ["", False, None]:
            self.dataFolder = False

    def init(self):
        if not self.dataFolder:
            return

        self.createDict = helperFunctions.statistics(self.filePath, self.self_info.plugInRunData.information.file_info)
        # self.createDict = {<名字>: <绝对路径>, ...}
        for key, path in self.createDict.items():
            # folderPath = os.path.join(self.filePath, path)
            returnValue = helperFunctions.mkdir(path)
            if isinstance(returnValue, abnormal.FolderCreationFailed):
                self.self_info.logData.parameterApplication.append(returnValue)
                continue

            self.self_info.plugInData.Folders.DataFolder[key] = path


@decorators.appRegistration(config.__name__)
def getTemporaryFolders(path: str) -> Optional[str]:
    if not File.plugInData.get("Folders", False):
        # 没有Folders插件
        return None

    if not File.plugInData.Folders.get("DataFolder", False):
        # 没有运行 TemporaryFolders
        return None

    return File.plugInData.Folders.DataFolder.get(path, None)
