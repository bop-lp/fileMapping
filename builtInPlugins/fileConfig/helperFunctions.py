import json
from typing import Union, Tuple, List
import traceback

from fileMapping.core import abnormal



def profileReads(configPath: str) -> Union[str, abnormal.FileReadFailed]:
    """
    读取配置文件
    :param configPath: 绝对路径 一般是插件的配置文件
    :return:
    """
    try:
        with open(configPath, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return abnormal.FileReadFailed(configPath, e, traceback.format_exc())


def fileWrite(filePath: str, text: str) -> Union[bool, abnormal.FileCreationFailed]:
    """
    写入文件
    :param filePath: 绝对路径
    :param text: 文本内容
    :return:
    """
    try:
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(text)
            return True

    except Exception as e:
        return abnormal.FileCreationFailed(filePath, e, traceback.format_exc())



def characterGeneration(nameOfThePlugin: str, text: dict, jump: bool = False) -> Union[
    abnormal.FileFormattingError, str, Tuple[str, List[Exception]]]:
    """
    生成 python 代码文件
    :param nameOfThePlugin: 插件名称
    :param text: 字典类型，键值对
    :param jump: 如若发生异常 是否直接终止 然后跳出 并返回错误信息
    :return:
    """
    txt = ""
    if not jump:
        # jump 为 False 则不跳出 继续执行
        jump = []  # 跳出列表 用于记录发生异常

    for k, v in text.items():
        if isinstance(v, str):

            txt += f"{k}: str = '{v}'\n"

        elif isinstance(v, int):

            txt += f"{k}: int = {v}\n"

        elif isinstance(v, bool):

            txt += f"{k}: bool = {v}\n"

        elif isinstance(v, float):

            txt += f"{k}: float = {v}\n"

        try:
            if isinstance(v, dict):
                _ = json.dumps(v, indent=4, ensure_ascii=False)
                txt += f"{k}: dict = {_}\n"

            elif isinstance(v, list):
                _ = json.dumps(v, indent=4, ensure_ascii=False)
                txt += f"{k}: list = {_}\n"

        except Exception as e:
            if isinstance(jump, bool):
                return abnormal.FileFormattingError(nameOfThePlugin, e, traceback.format_exc())

            else:
                jump.append(e)

    if isinstance(jump, list):
        if len(jump) == 0:
            # 无异常发生
            return txt

        else:
            # 发生异常
            return [txt, jump]
    return txt

