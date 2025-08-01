import os
import shutil
import traceback
from typing import Dict, Union
import functools

from fileMapping.core import Class
from fileMapping.core import abnormal
from fileMapping.core.abnormal import FolderCreationFailed, FolderAlreadyExists


def mkdir(file_path) -> Union[FolderCreationFailed, bool, FolderAlreadyExists]:
    try:
        if os.path.exists(file_path):
            # 文件夹已存在
            pass

        os.makedirs(file_path)
        return True

    except FileExistsError as e:
        return abnormal.FolderAlreadyExists(file_path, e, traceback.format_exc())

    except Exception as e:
        return abnormal.FolderCreationFailed(file_path, e, traceback.format_exc())
# FileExistsError(17, '当文件已存在时，无法创建该文件。')

def statistics(filePath: str, file_info: Dict[str, Class.PlugInRetention]) -> Dict[str, str]:
    """

    :param filePath: 绝对路径
    :param file_info:
    :return:
    """
    createDict = {}
    for plugInName, info in file_info.items():
        if not isinstance(info.__dataFolders__, (str, list, tuple)):
            continue

        if isinstance(info.__dataFolders__, str):
            createDict[info.__dataFolders__] = (os.path.join(filePath, info.__dataFolders__))

        elif isinstance(info.__dataFolders__, (list, tuple)):
            createDict.update({
                i: os.path.join(filePath, i)
                for i in info.__dataFolders__
            })

        else:
            continue

    return createDict


def delete(path: str) -> Union[bool, abnormal.FolderDeletion]:
    try:
        shutil.rmtree(path)
        return True

    except Exception as e:
        return abnormal.FolderDeletion(path, e, traceback.format_exc())


def wrapper(file: Class.File):
    """
    装饰器
self = {FileConfig} <fileConfig.FileConfig object at 0x000001A9F9D73160>    """
    def wrapper_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(file, *args, **kwargs)

        return wrapper

    return wrapper_func

