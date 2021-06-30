from sys import argv
import doctest

def is_type_safe(arg, type):
    try:
        type(arg)
        return True
    except Exception:
        return False

def print_list(values, message):
    if values:
        print(message)
        print(*[x for x in values], sep='\n')

def get_type(arg):
    """
    >>> get_type('0')
    <class 'int'>

    >>> get_type('1')
    <class 'int'>

    >>> get_type('000123')
    <class 'int'>    

    >>> get_type('0.0')
    <class 'float'>

    >>> get_type('0.0000')
    <class 'float'>

    >>> get_type('1.00001')
    <class 'float'>

    >>> get_type('1.0')
    <class 'float'>

    >>> get_type('fdsgdgsdg1')
    <class 'str'>

    >>> get_type('1-2-3')
    <class 'str'>
    """

    if is_type_safe(arg, int):
        return int
    elif is_type_safe(arg, float):
        return float
    else:
        return str

doctest.testmod()

def sort_args_by_type():
    strings = []
    integers = []
    floats = []

    for arg in argv[1:]:
        arg_type = get_type(arg)
        if arg_type is int:
            integers.append(arg)
        elif arg_type is float:
            floats.append(arg)
        elif arg_type is str:
            strings.append(arg)
    
    return integers, floats, strings

def get_list_str_contains_last_args(strings):
    result = []
    try:
        last_arg = argv[-1]
        if last_arg == strings[-1]:
            result = [x for x in strings if last_arg in x]
    except Exception:
        pass

    return result

def main():
    integers, floats, strings = sort_args_by_type()

    print_list(integers, 'Integers:')
    print_list(floats, 'Floats:')
    print_list(strings, 'Strings:')

    string_contains_larg = get_list_str_contains_last_args(strings)
    print_list(string_contains_larg, f'Strings contains last arg:')

main()