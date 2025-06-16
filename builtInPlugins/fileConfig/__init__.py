"""
将每个插件的配置文件列出到 指定的文件夹中
可以具体调仓插件的配置文件
"""
import os
from types import ModuleType


from fileMapping.core import Class
from fileMapping.core import parameterApplication
from fileMapping.core import abnormal


from . import config
from . import helperFunctions


@parameterApplication.wrapper
class FileConfig(Class.ParameterApplication):
    """
    配置插件的配置文件
    """
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.config_folder_path = self.self_info.plugInData.fileConfig.config["configFolderPath"]
        self.configJump = self.self_info.plugInData.fileConfig.config["configJump"]
        self.reIsASkipInTheFile = self.self_info.plugInData.fileConfig.config["reIsASkipInTheFile"]

        if self.config_folder_path in [None, "", False]:
            self.config_folder_path = False
            return

        if not os.path.isdir(self.config_folder_path):
            self.config_folder_path = False
            return


    def init(self):
        """
        初始化插件的配置文件
        """
        if self.config_folder_path is False:
            return

        for nameOfThePlugin, profiles in self.self_info.plugInRunData.callObject.items():
            if not 'config' in dir(profiles.pack):
                # 跳过没有配置文件的插件
                continue

            objectFiles = getattr(profiles.pack, 'config')
            if isinstance(objectFiles, dict):
                textData = helperFunctions.characterGeneration(nameOfThePlugin, objectFiles, self.configJump)
                if isinstance(textData, list):
                    # 有错错误发生 & 配置文件格式误
                    self.self_info.logData.parameterApplication += textData[-1]
                    textData = textData[0]

                elif isinstance(textData, abnormal.FileFormattingError):
                    # 文件格式错误
                    self.self_info.logData.parameterApplication.append(textData)
                    continue

            elif isinstance(objectFiles, ModuleType):
                # helperFunctions.profileReads
                path = os.path.join(profiles.absolutePath, profiles.packageName, "config.py")
                if not os.path.isfile(path):
                    # 没有配置文件
                    continue

                textData = helperFunctions.profileReads(path)
                if isinstance(textData, abnormal.FileReadFailed):
                    # 配置文件读取失败
                    self.self_info.logData.parameterApplication.append(textData)


            else:
                continue


            returnValue = helperFunctions.fileWrite(os.path.join(self.config_folder_path, nameOfThePlugin + ".py"),
                                                    textData)
            if isinstance(returnValue, abnormal.FileCreationFailed):
                # 配置文件写入失败
                self.self_info.logData.parameterApplication.append(returnValue)



