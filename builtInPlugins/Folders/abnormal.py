
from fileMapping.core import abnormal



class Folder(abnormal.Mistake):
    def __init__(self, folderName: str, error: str, stack: str):
        self.stack = stack
        self.folderName = folderName
        self.error = error

class FolderCreationFailed(Folder):
    def english(self) -> str:
        return f"Failed to create folder {self.folderName}, error message: {self.error}"

    def chinese(self) -> str:
        return f"创建文件夹 {self.folderName} 失败，错误信息：{self.error}"


class FolderDeletion(Folder):
    def english(self) -> str:
        return f"Failed to delete folder {self.folderName}, error message: {self.error}"

    def chinese(self) -> str:
        return f"删除文件夹 {self.folderName} 失败，错误信息：{self.error}"

