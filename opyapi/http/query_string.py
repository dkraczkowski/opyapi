from typing import ItemsView, KeysView, ValuesView, Optional
from urllib.parse import unquote_plus


def create_dict_for_key(path: str, value) -> dict:
    starting_bracket = path.find("[")
    if path[-1:] != "]":
        return {path: value}
    parsed_path = [path[:starting_bracket]]
    parsed_path = parsed_path + path[starting_bracket + 1 : -1].split("][")

    for part in parsed_path:
        if "[" in part or "]" in part:
            return {path: value}

    def _create_leaf(_parsed_path: list):
        if len(_parsed_path) == 1:
            if not _parsed_path[0]:
                return [value]
            else:
                return {_parsed_path[0]: value}
        if not _parsed_path[0]:
            return [_create_leaf(_parsed_path[1:])]
        else:
            return {_parsed_path[0]: _create_leaf(_parsed_path[1:])}

    return _create_leaf(parsed_path)


def deep_merge(a: dict, b: dict) -> dict:
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                a[key] = deep_merge(a[key], b[key])
            elif isinstance(a[key], list) and isinstance(b[key], list):
                a[key] = a[key] + b[key]
            elif isinstance(b[key], list):
                a[key] = [a[key]] + b[key]
            elif isinstance(b[key], dict):
                a[key] = {"": a[key], **b[key]}
            else:
                a[key] = [a[key], b[key]]
        else:
            a[key] = b[key]
    return a


def parse_qs(query: str, encoding: Optional[str] = None) -> dict:
    """
    Parse query string with json forms support, more available in the following link
    https://www.w3.org/TR/html-json-forms/
    :param query:
    :param encoding:
    :return:
    """
    result = {}
    if query == "":
        return result

    for item in query.split("&"):
        (name, value) = item.split("=")
        value = unquote_plus(value)
        if encoding:
            name = name.decode(encoding)
            value = value.decode(encoding)

        if "[" in name:
            value = create_dict_for_key(name, value)
            result = deep_merge(result, value)
        elif name in result:
            if isinstance(result[name], list):
                result[name].append(value)
            else:
                result[name] = [result[name], value]
        else:
            result[name] = value

    return result


class QueryString:
    def __init__(self, string: str, encoding: Optional[str] = None):
        self._str = string
        self._params = parse_qs(string, encoding)

    def __getitem__(self, key) -> str:
        return self._params[key]

    def __contains__(self, key) -> bool:
        return key in self._params

    def __str__(self) -> str:
        return self._str

    def items(self) -> ItemsView:
        return self._params.items()

    def values(self) -> ValuesView:
        return self._params.values()

    def keys(self) -> KeysView:
        return self._params.keys()


__all__ = [QueryString, parse_qs]
