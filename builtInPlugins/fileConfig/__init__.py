"""
将每个插件的配置文件列出到 指定的文件夹中
可以具体调仓插件的配置文件
"""
import os

from fileMapping.core import Class
from fileMapping.core import parameterApplication

from . import config

import rich

@parameterApplication.wrapper
class FileConfig(Class.ParameterApplication):
    """
    配置插件的配置文件
    """
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)

        self.config_folder_path = self.self_info.plugInData.fileConfig.config["configFolderPath"]
        if self.config_folder_path in [None, "", False]:
            self.config_folder_path = False
            return

        rich.inspect(self.config_folder_path)
        if os.path.isdir(self.config_folder_path):
            print("path: ", self.config_folder_path)

    def init(self):
        """
        初始化插件的配置文件
        """
        if self.config_folder_path is False:
            return



