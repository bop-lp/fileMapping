import os
import shutil
import traceback
from typing import List

from fileMapping.core import decorators
from fileMapping.core import Class

from . import abnormal
from . import helperFunctions


@decorators.appRegistration()
class TemporaryFolders(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.config = self.self_info.plugInData.Folder.config
        self.tempFolderPath = False
        self.whetherItIsSelfCreated = False
        self.createList: List[str] = []
        # 文件列表

        if self.config.tempFolderPath is not [None, '', False]:
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

    def init(self):
        if isinstance(self.tempFolderPath, bool):
            return

        self.createDict  = helperFunctions.statistics(self.config.tempFolderPath, self.self_info.plugInRunData.information.file_info)

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
