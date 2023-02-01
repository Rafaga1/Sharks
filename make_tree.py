from typing import List, Tuple
import re


TREE = {'cluster': {}}


def set_value(dict_in: dict, keys: List[str], method: str):
    """
    Собирает дерево
    :param dict_in:
    :param keys: str
    :param method: str
    :return: None
    """
    for key in keys[:-1]:
        dict_in = dict_in.setdefault(key, {})
    dict_in[keys[-1]] = method

def parse(url: str, method) -> None:
    """
    Парсит url
    :param url: str
    :param method: str,
    """
    global TREE
    tree = TREE['cluster']
    list_url = [item for item in url[re.search('cluster/', url).end():].split('/') if '{' not in item]
    set_value(tree, list_url, method)

def add_url(list_urls: List[Tuple[str, str]]) -> dict:
    """
    Принимает список картежей, возвращает дерево.
    :param list_urls: List[Tuple[str, str]]
    :return: dict
    """
    for item in list_urls:
        parse(item[1], item[0])
    return TREE
