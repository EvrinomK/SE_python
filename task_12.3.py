import doctest

L = [12, 'test', -4, [2, 4], (1, 1), -3.0, 'string string']


def swap_halfs_list(values):
    """
    >>> swap_halfs_list([1, 2])
    [2, 1]

    >>> swap_halfs_list([1, 2, 4])
    [4, 2, 1]

    >>> swap_halfs_list([1, 2, 5, 3])
    [5, 3, 1, 2]

    >>> swap_halfs_list(['Happy', 'new', 'Year'])
    ['Year', 'new', 'Happy']

    >>> swap_halfs_list([1, 2, 3, 4, 5, 6, 7])
    [5, 6, 7, 4, 1, 2, 3]

    >>> swap_halfs_list(L)
    [(1, 1), -3.0, 'string string', [2, 4], 12, 'test', -4]
    """

    middle_index = int(len(values) / 2)
    diffs = middle_index + 1 if len(values) % 2 else middle_index
    for i in range(middle_index):
        values[i], values[i + diffs] = values[i + diffs], values[i] 

    return values

doctest.testmod()
