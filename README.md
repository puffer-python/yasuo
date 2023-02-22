# Yasuo Functions for Python

This package provides a collection of utility functions that can be used to handle text and data in Python.

## Installation

Install Yasuo Package

```commandline
pip install yasuo
```

In your code, please import

```python

from yasuo import *

```

## List of Functions

### Convert any to an integer

This code snippet provides a function convert_int_field() that can be used to convert any data type to an integer. If
the value cannot be converted, an exception is raised. This function takes in several parameters to customize the
conversion process, such as a default value to return if conversion fails and a minimum value for the resulting integer.

Here's an example usage of convert_int_field():

```python
>>> convert_int_field(10)
10

>>> convert_int_field("10")
10

>>> convert_int_field("10a", ignore_error=False, error_message="Input must be a valid integer.")
ValueError: Input must be a valid integer.

```

### Converts a Vietnamese string with diacritics to a string without diacritics.

```python
convert(text: str) -> str
```

### Converts a Vietnamese string with diacritics to a string without diacritics using the unidecode library.

```python
remove_accents(text: str) -> str
```

### Converts a string to lowercase and removes diacritics.

```python
normalized(s: str) -> str
```

### Removes extra spaces from a string and returns a new string with single spaces.

```python
keep_single_spaces(s: str) -> str
```

### Splits a list into smaller chunks of length step.

```python
create_chunks(src: list, step: int) -> list
```

### Recursively converts byte strings in a dictionary to Unicode strings.

```python
reformat_dict(data: dict) -> dict
```

### Checks if a list has duplicate elements.

```python
list_has_duplicates(mylist: list) -> bool
```

### Removes duplicates from a list.

```python
remove_duplicate_from_list(a_list: list) -> list
```

### Checks if a string is a valid JSON.

```python
is_json(str_input: str) -> bool
```

### Generates a random string of letters and digits.

```python
random_string(length: int = 6) -> str
```

### Converts a snake_case string to camelCase.

```python
camel_case(s: str) -> str
```

### Generates a URL

Generates a URL-friendly string by removing all characters except letters, digits, and hyphens.

```python
generate_url_key(a_string: str) -> str
```

### Flattens a 2D list into a 1D list.

```python
flatten_list(a_list: list) -> list
```

### Returns the current time in UTC for a given local timezone.

```python
get_utc_time(local_name: str, fmt: str = None) -> str
```

### Diff Dicts

Returns the difference between two dictionaries in a list of dictionaries. Each dictionary in the list contains the key,
the old value, and the new value.

```python
dict_diff(old_dict: dict, new_dict: dict) -> list
```

### Decapitalizes the first character in a string.

```python
decapitalize(a_str: str) -> str
```

# License

This code is released under the MIT License.

You can copy and paste the code into your Python project and modify it as needed. If you have any questions or issues,
please don't hesitate to reach out.


