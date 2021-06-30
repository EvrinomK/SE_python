import doctest

def sum_matrix_values_over_main_diagonal(matrix):
    """
    >>> sum_matrix_values_over_main_diagonal([[1]])
    0

    >>> sum_matrix_values_over_main_diagonal([[1, 2], [8, 9]])
    2

    >>> sum_matrix_values_over_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    11

    """
    return sum([matrix[i][j] for i in range(len(matrix)) for j in range(i + 1, len(matrix[i]))])

doctest.testmod() 