# coding=utf-8
import json
import random
import re
import string
from datetime import datetime

import pytz
from slugify import slugify

__author__ = 'DungBV'
__patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = text
    for regex, replace in __patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output


def remove_accents(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau' using unidecode lib.
    It can process well with multiple percussion
    text: input string to be converted
    Return: string converted
    """
    import unidecode
    return unidecode.unidecode(text)


def normalized(s):
    """
    Convert and lowercase, then trim
    :param s:
    :return:
    """
    return convert(s).lower().strip() if s else None


def keep_single_spaces(s):
    """
    Convert " ABC    DEF " to "ABC DEF"
    """
    if isinstance(s, str):
        return ' '.join(s.strip().split())
    return s


def create_chunks(src, step):
    res = []
    for i in range(0, len(src), step):
        res.append(src[i:i + step])

    return res


def reformat_dict(data):
    """

    :param data:
    :return:
    """
    if not isinstance(data, dict):
        return data
    formatted_data = {}
    for key in data:
        formatted_key = key
        if isinstance(key, (bytes, bytearray)):
            formatted_key = key.decode('utf-8')
        if isinstance(data[key], dict):
            formatted_data[formatted_key] = reformat_dict(data[key])
        elif isinstance(data[key], (bytes, bytearray)):
            formatted_data[formatted_key] = data[key].decode('utf-8')
        else:
            formatted_data[formatted_key] = data[key]
    return formatted_data


def list_has_duplicates(mylist):
    """
    Check if a list has duplicate elements
    :param mylist:
    :return:
    """
    if len(set(mylist)) != len(mylist):
        return True
    return False


def remove_duplicate_from_list(a_list):
    """
    Remove duplicates from list
    :param a_list:
    :return:
    """
    return list(dict.fromkeys(a_list))


def is_json(str_input):
    """
    Check if string input is a valid json or not
    :param str_input:
    :return:
    """
    try:
        json.loads(str_input)
    except (TypeError, ValueError):
        return False
    return True


def random_string(length=6):
    """Generate a random string of letters and digits """
    text = string.ascii_letters + string.digits
    return ''.join(random.choice(text) for _ in range(length))


def camel_case(s):
    """
    Perform string inflection
    :param str s: input string
    :return:
    """
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def generate_url_key(a_string):
    return ''.join(filter(
        lambda c: re.fullmatch('[a-zA-Z0-9-]', c),
        slugify(convert(a_string))
    ))


def flatten_list(a_list):
    """
    flatten a 2-dim list

    :param a_list:
    :return:
    """
    return [item for sl in a_list for item in sl]


def get_utc_time(local_name, fmt=None):
    timezones = pytz.country_timezones[local_name]
    if not timezones:
        raise ValueError(f'Local {local_name} not exist')
    local = pytz.timezone(timezones[0])
    now = datetime.now()
    now_dst = now.astimezone(local)
    if fmt:
        return now_dst.strftime(fmt)
    return now_dst


def dict_diff(old_dict: dict, new_dict: dict) -> list:
    """
    return diff of 2 dicts in format: {"key1":{"old":"old_value_key1", "new":"new_value_key1"}}
    :param old_dict: dict
    :param new_dict: dict
    :return: dict
    """
    return [{k: {'old': old_dict.get(k), 'new': new_dict.get(k)}}
            for k in set(list(old_dict) + list(new_dict)) if old_dict.get(k) != new_dict.get(k)]


def decapitalize(a_str):
    """
    Decapitalize the first character in string. Other characters
    remain unchanged.
    Example: Decapitalize string -> decapitalize string

    :param string a_str:
    :return:
    """
    return a_str[0].lower() + str[1:]


class DictToObject:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


def __cast_boolean(val, default):
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        val = val.lower()

    switch = {
        'true': True,
        1: True,
        '1': True,
        'false': False,
        0: False,
        '0': False,
    }
    return switch.get(val, default)


def safe_cast(val, to_type, default=None):
    try:
        if to_type == bool:
            return __cast_boolean(val, default)
        return to_type(val)
    except (ValueError, TypeError):
        return default


def cast_separated_string_to_ints(separated_str: str, sep: str = ','):
    return [int(v) for v in separated_str.split(sep) if v.isnumeric()]


def convert_to_html_tag(s):
    return s.replace("\n", "<br> ")


__version__ = 1.0
