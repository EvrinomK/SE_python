import doctest

L = [-8, 8, 6.0, 5, 'строка', -3.1]

def sum_of_numbers(values):
    """
    >>> sum_of_numbers([1])
    1

    >>> sum_of_numbers([1, 2])
    3

    >>> sum_of_numbers([1, 2, 3.0])
    6.0

    >>> sum_of_numbers([1, '2', 3])
    4

    >>> sum_of_numbers([1, '2', 3, 'test data', 11.9])
    15.9

    >>> sum_of_numbers([1, '2', 3, 'test data', 11.9, [11, 22], ('asf', 6), {'x' : 'y'}])
    15.9

    >>> sum_of_numbers(['2'])
    0

    >>> sum_of_numbers(['2', 'test data', ('asf', 6), {'x' : 'y'}])
    0

    >>> sum_of_numbers(L)
    7.9
    """

    return sum([x for x in values if type(x) is int or type(x) is float])

doctest.testmod()

print(sum_of_numbers(L))


