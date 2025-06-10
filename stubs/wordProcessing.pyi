from typing import Dict, Union

pattern: Dict[str, str]

def get_all(text: str) -> Dict[str, Union[int, str, Dict]]:
    """
    获取文件全部信息

    :param text: 文本内容
    :return: 文件全部信息
    """
    ...

def get_file_underlying(text: str) -> str:
    """
    获取文件底层信息

    :param text: 文本内容
    :return: 文件底层信息
    """
    ...

def get_file_dependencies_on_plugins(text: str) -> Union[Dict, list]:
    """
    获取文件依赖插件信息

    :param text: 文本内容
    :return: 文件依赖插件信息
    """
    ...

def get_file_level(text: str) -> int:
    """
    获取文件层级信息

    :param text: 文本内容
    :return: 文件层级信息
    """
    ...

def sorting_plugin(plugin_dict: Dict[str, Dict]) -> Dict[int, Union[List[str], tuple]]:
    """
    排序插件
    应该按照插件的层级和依赖关系来排序
    按照任务执行标准来排序

    :param plugin_dict: 插件字典
    :return: 任务执行顺序字典或包含循环依赖插件的列表
    """
    ...

def get_file_info(file_object: object, info: Dict[str, object]) -> Dict[str, object]:
    """
    获取文件信息
    :param file_object: 文件对象
    :param info: 文件信息字典 {infoName: messageDefaults, ...}
    :return: 文件信息字典 {infoName: message, ...}
    """
    ...