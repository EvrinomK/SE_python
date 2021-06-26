from sys import argv
import doctest

def is_type_safe(arg, type):
    try:
        converted_arg = type(arg)
        return True
    except Exception:
        return False

def print_list(values):
    print()
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

def main():
    strings = []
    integers = []
    floats = []

    if not argv[1:]:
        return

    for arg in argv[1:]:
        arg_type = get_type(arg)
        if arg_type is int:
            integers.append(arg)
        elif arg_type is float:
            floats.append(arg)
        elif arg_type is str:
            strings.append(arg)

    if strings:
        print('Strings:')
        print_list(strings)

    if integers:
        print('Integers:')
        print_list(integers)

    if floats:
        print('Floats:')
        print_list(floats)

    try:
        last_arg = argv[-1]
        if last_arg == strings[-1]:
            print(f'Found string {last_arg} in following args:')
            for string in strings:
                if last_arg in string:
                    print(string)
    except Exception:
        pass

main()