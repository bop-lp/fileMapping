import os
import shutil
import traceback
from typing import Dict, Union

from fileMapping.core import Class
from fileMapping.core import abnormal


def mkdir(file_path) -> Union[bool, abnormal.FolderCreationFailed]:
    try:
        # os.makedirs()
        os.makedirs(file_path)
        return True

    except FileExistsError as e:
        return abnormal.FolderCreationFailed(file_path, e, traceback.format_exc())


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