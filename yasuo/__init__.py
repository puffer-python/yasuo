# coding=utf-8

"""
This package provides a collection of utility functions that
can be used to handle text and data in Python.


Author: Jung BV
Date: 2023-02-16
"""
import json
import random
import re
import string
from datetime import datetime

import pytz
import unidecode
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

    return unidecode.unidecode(text)


def normalized(a_string):
    """
    Convert and lowercase, then trim
    :param a_string:
    :return:
    """
    return convert(a_string).lower().strip() if a_string else None


def keep_single_spaces(s_string):
    """
    Convert " ABC    DEF " to "ABC DEF"
    """
    if isinstance(s_string, str):
        return ' '.join(s_string.strip().split())
    return s_string


def create_chunks(src, step):
    """

    :param src:
    :param step:
    :return:
    """
    res = []
    for i in range(0, len(src), step):
        res.append(src[i:i + step])

    return res


def reformat_dict(data):
    """
    Recursively decode byte-encoded dictionary keys and values to utf-8 strings.
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


def camel_case(s_string):
    """
    Perform string inflection
    :param str s_string: input string
    :return:
    """
    parts = iter(s_string.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def generate_url_key(a_string):
    """

    :param a_string:
    :return:
    """
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
    """

    :param local_name:
    :param fmt:
    :return:
    """
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


def decapitalize(a_string):
    """
    Decapitalize the first character in string. Other characters
    remain unchanged.
    Example: Decapitalize string -> decapitalize string

    :param string a_string:
    :return:
    """
    return a_string[0].lower() + a_string[1:]


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
    """

    :param val:
    :param to_type:
    :param default:
    :return:
    """
    try:
        if to_type == bool:
            return __cast_boolean(val, default)
        return to_type(val)
    except (ValueError, TypeError):
        return default


def cast_separated_string_to_ints(separated_str: str, sep: str = ','):
    """

    :param separated_str:
    :param sep:
    :return:
    """
    return [int(v) for v in separated_str.split(sep) if v.isnumeric()]


def convert_to_html_tag(s_string):
    """

    :param s_string:
    :return:
    """
    return s_string.replace("\n", "<br> ")


def fibonacci(number: int) -> int:
    """
    Calculate the nth value in the Fibonacci sequence.

    Args:
        number (int): The position of the desired Fibonacci value (starting from 0).

    Returns:
        int: The Fibonacci value at position n.
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def convert_int_field(data, default=None, min_number=None, ignore_error=True, error_message=None):
    """
    Convert any type to an integer
    Raise an exception if the data is not an integer
    :param data: the data to be converted
    :param default: the default value to be returned if the data is None or empty
    :param min_number: the minimum value that the integer can take
    :param ignore_error: whether to ignore errors and return default value instead
    :param error_message: the error message to be raised in case of error
    :return: the integer representation of the data
    """
    # if data is empty, return default
    if data is None or data == '':
        return default

    # if data is numeric and greater than or equal to the minimum allowed value,
    # return integer representation of data
    if str(data).isnumeric() and (min_number is None or int(data) >= min_number):
        return int(data)

    # if ignore_error is False, raise a value error with the error_message
    if not ignore_error:
        raise ValueError(error_message)

    # return default value if any other error occurs
    return default


__version__ = 1.0
