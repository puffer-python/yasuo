# Yasuo Package

Yasuo Package is a Python package that provides functionality related to the popular game League of Legends.
Specifically, it provides tools for analyzing data related to the champion Yasuo.

## Installation

You can install Yasuo Package using pip:

```commandline
pip install yasuo
```

## Usage

After installation, you can import Yasuo Package in your Python script as follows:

```python

import yasuo

```

## List of Functions

### Convert any to an integer

This code snippet provides a function convert_int_field() that can be used to convert any data type to an integer. If
the value cannot be converted, an exception is raised. This function takes in several parameters to customize the
conversion process, such as a default value to return if conversion fails and a minimum value for the resulting integer.

Here's an example usage of convert_int_field():

```
>> convert_int_field(10)
10

>> convert_int_field("10")
10

>> convert_int_field("10a", ignore_error=False, error_message="Input must be a valid integer.")
ValueError: Input must be a valid integer.

```

### Vietnamese Text Converter

This package provides a function to convert Vietnamese text with diacritics to Vietnamese text without diacritics.

```python
from yasuo import convert

text_with_diacritics = "Đây là một ví dụ về tiếng Việt có dấu"
text_without_diacritics = convert(text_with_diacritics)
print(text_without_diacritics)  # Output: "Day la mot vi du ve tieng Viet co dau"

```

### Normalized

The normalized() function converts a string to lowercase, removes all diacritics (accents) and extra spaces. This
function can be used to normalize user input or database entries for comparison purposes.

```python
input_string = "Trường Đại học Bách Khoa Hà Nội"
normalized_string = normalized(input_string)
print(normalized_string)  # Output: "truong dai hoc bach khoa ha noi"

```

### Keep Single Spaces

This function keeps only single spaces between words in a string and removes any leading/trailing spaces.

- Inputs:
    - `s_string`: A string
- Outputs
    - A new string with only single spaces between words and no leading/trailing spaces.

Example

```python
keep_single_spaces("  This   is   a   test  ")
'This is a test'

```

### Chunks

The `create_chunks()` function takes in two parameters: `src` and `step`.

`src` is the source string or list that needs to be divided into chunks.

`step` is the maximum length of each chunk.

The function creates a list of chunks by iterating over the `src` string or list and appending slices of length step to
a new list res.

The resulting list res contains all the chunks of length `step` that make up the original `src` string or list.

Example:

```python
src = 'abcdefghijklmnopqrstuvwxyz'
step = 5
chunks = create_chunks(src, step)
print(chunks)
```

Output:

```json
[
  'abcde',
  'fghij',
  'klmno',
  'pqrst',
  'uvwxy',
  'z'
]
```

### Recursively converts byte strings in a dictionary to Unicode strings.

The function reformat_dict recursively decodes byte-encoded dictionary keys and values to utf-8 strings.

Parameters:

- data: a dictionary that may contain byte-encoded keys or values

Return:

- A new dictionary with all byte-encoded keys and values decoded to utf-8 strings

Example

```python
data = {'name': b'John', 'age': 30, 'contacts': {'email': b'john@gmail.com', 'phone': b'123456789'}}
new_data = reformat_dict(data)
print(new_data)
```

Output

```json
{
  'name': 'John',
  'age': 30,
  'contacts': {
    'email': 'john@gmail.com',
    'phone': '123456789'
  }
}



```

### List Duplicates

This function checks if a list has duplicate elements. It returns True if there are duplicates, otherwise False.

Here is an example usage:

```python
>> > list_has_duplicates([1, 2, 3, 4, 5])
False

>> > list_has_duplicates([1, 2, 3, 3, 4, 5])
True

```

### Remove duplicated

This function removes duplicates from a given list using a Python dictionary. It converts the list to a dictionary where
the elements of the list become the keys of the dictionary, then converts the dictionary back into a list. This process
eliminates any duplicate keys and returns a list with unique elements in the original order.

Example:

```python
a_list = [1, 2, 3, 1, 4, 2, 5, 6, 5]
remove_duplicate_from_list(a_list)
[1, 2, 3, 4, 5, 6]

```

### Is Json

The `is_json` function checks whether the input string is a valid JSON or not.

`str_input`: a string to be checked. If the string is a valid JSON, the function returns True. Otherwise, it returns
False.

Here is an example usage:

```python
input_str = '{"name": "John", "age": 30, "city": "New York"}'
result = is_json(input_str)
print(result)  # True

invalid_str = 'this is not a valid JSON'
result = is_json(invalid_str)
print(result)  # False
```

### Random String

This function generates a random string of a specified length, consisting of both letters (upper and lower case) and
digits.

- `length`: An optional integer argument that specifies the length of the generated string. The default length is 6.-

The function uses the `string` and `random` modules to generate a string with a combination of upper and lower case
letters and digits. It then uses a join function to `join` these characters together to form the random string.

Example usage:

```python

random_string()  # Output: 'tDy8Vc'
random_string(10)  # Output: 'JnZ8WbKu3P'

```

### Camel Case

The camel_case function takes an input string with underscore-separated words and converts it to camel case format.

For example, if the input string is `"hello_world"`, the output will be `"helloWorld"`.

The function takes one parameter:

- `s_string`: the input string to be converted The function returns a string in camel case format. If the input string
  is empty or not a string, the function returns None.

Example

```python
>> > camel_case('hello_world')
'helloWorld'
>> > camel_case('hello_big_world')
'helloBigWorld'
>> > camel_case('hello')
'hello'
>> > camel_case('hElLo')
'hello'

```

### Generate URL Key

The `generate_url_key` function takes an input string and returns a URL-safe version of the string, suitable for use as
a URL key.

The function first converts the input string to a normalized format, then removes any characters that are not letters,
numbers, or hyphens. The resulting string is then returned.

The function takes one parameter:

- `a_string`: the input string to be converted The function returns a string in URL-safe format. If the input string is
  empty or not a string, the function returns None.

Example

```python
 generate_url_key('Hello, world!')
'hello-world'
generate_url_key('Python is awesome')
'python-is-awesome'
generate_url_key('My favorite number is 42')
'my-favorite-number-is-42'
generate_url_key('')
None

```

### Flatten List

The `flatten_list` function takes a two-dimensional list as input and flattens it into a one-dimensional list.

For example, if the input list is `[[1, 2], [3, 4], [5, 6]]`, the output will be `[1, 2, 3, 4, 5, 6]`.

The function takes one parameter:

- `a_list`: the input two-dimensional list to be flattened The function returns a one-dimensional list. If the input is
  not a two-dimensional list, the function returns None.

Example:

```commandline
>> flatten_list([[1, 2], [3, 4], [5, 6]])
[1, 2, 3, 4, 5, 6]
>> flatten_list([[1, 2, 3], [4], [5, 6]])
[1, 2, 3, 4, 5, 6]
>> flatten_list([[1, 2], [3, 4], 5, 6])
None

```

### Get UTC

The `get_utc_time` function retrieves the current UTC time given a local time zone name. It uses the pytz library to
convert the local time zone to UTC. The function takes two parameters:

- `local_name`: a string representing the name of the local time zone.
- `fmt` (optional): a string representing the format of the returned UTC time.

If not provided, the function returns a datetime object in the UTC time zone. If the local time zone name is not found,
the function raises a ValueError.

Example:

```commandline
>> get_utc_time('US/Eastern', '%Y-%m-%d %H:%M:%S')
'2022-03-07 02:30:26'
>> get_utc_time('Europe/London')
datetime.datetime(2022, 3, 7, 7, 30, 26, 518046, tzinfo=<UTC>)

```

### Dict Diff

The `dict_diff` function takes in two dictionaries, `old_dict` and `new_dict`, and returns a list of differences between
them in the format of `{"key1":{"old":"old_value_key1", "new":"new_value_key1"}}`. If the value of a key is different
between the two dictionaries, it will be included in the result list.

Here's an example:

```python
old_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
new_dict = {'key1': 'value1', 'key2': 'new_value2', 'key4': 'value4'}
diff_list = dict_diff(old_dict, new_dict)
print(diff_list)

```

Output

```commandline
[{'key2': {'old': 'value2', 'new': 'new_value2'}}, {'key3': {'old': 'value3', 'new': None}}, {'key4': {'old': None, 'new': 'value4'}}]

```

### Decapitalize

The `decapitalize` function takes a string input and returns the string with the first character in lowercase and all
other characters unchanged.

For example, if the input string is `"Decapitalize string"`, the output will be `"decapitalize string"`.

The function takes one parameter:

- `a_string`: the input string to be decapitalized

The function returns a string with the first character in lowercase and all other characters unchanged. If the input
string is empty or not a string, the function returns None.

Example:

```python
>> decapitalize("Decapitalize string")
'decapitalize string'
>> decapitalize("capitalize")
'capitalize'
>> decapitalize("")
''

```

### Safe Cast

The `safe_cast` function is used to convert a value of any type to a specified type. If the conversion fails, it returns
a default value instead of raising an exception.

The function takes three parameters:

- `val`: the value to be converted
- `to_type`: the type to which val should be converted
- `default` (optional): the default value to be returned if the conversion fails. If default is not specified, None is
  returned.

The function first tries to convert `val` to `to_type` using the built-in conversion function for that type. If the
conversion fails, it tries to convert `val` to boolean if `to_type` is `bool`. If the conversion succeeds, it returns
the converted value; otherwise, it returns the default value.

Example:

```python
>> > safe_cast("10", int, 0)
10

>> > safe_cast("10.5", float, 0.0)
10.5

>> > safe_cast("True", bool, False)
True

>> > safe_cast("invalid", int, 0)
0

>> > safe_cast(None, int, 0)
0

>> > safe_cast(None, int)
None

```

### Cast Separated String

The `cast_separated_string_to_ints` function takes a string containing integers separated by a specified separator and
returns a list of integers.

The function takes two parameters:

- `separated_str`: a string containing integers separated by a specified separator
- `sep`: the separator used in the input string (default value is ,)

The function returns a list of integers extracted from the input string, ignoring any non-numeric values. If the input
string is empty, the function returns an empty list.

Example:

```python
>> > cast_separated_string_to_ints('1,2,3,4')
[1, 2, 3, 4]
>> > cast_separated_string_to_ints('1-2-3-4', '-')
[1, 2, 3, 4]
>> > cast_separated_string_to_ints('1,abc,3,def')
[1, 3]
>> > cast_separated_string_to_ints('')
[]

```

### HTML Converter

The `convert_to_html_tag` function replaces all newline characters in the input string with an HTML line break
tag (`<br>`), effectively converting the string to a format suitable for display in HTML.

Function parameters:

- `s_string` : The input string to be converted.

Function return value:

- The function returns a string with newline characters replaced by the HTML line break tag.

### Fibonacci

This function calculates the value of the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of
numbers in which each number is the sum of the two preceding numbers, starting from 0 and 1. For example, the first few
numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The number parameter is the position of the desired Fibonacci value (starting from 0). For instance, if number is 5, the
function returns the 5th number in the Fibonacci sequence, which is 5. If number is less than or equal to 1, the
function simply returns number.

The function uses recursion to calculate the Fibonacci value. Specifically, it calls itself with number - 1 and number -
2 as arguments and returns the sum of the two resulting values.

Example

```python

# Calculate the first 10 numbers in the Fibonacci sequence
for i in range(10):
    print(fibonacci(i))
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

```

# License

This code is released under the MIT License.

You can copy and paste the code into your Python project and modify it as needed. If you have any questions or issues,
please don't hesitate to reach out.
