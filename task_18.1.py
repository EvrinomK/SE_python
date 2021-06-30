import doctest

def read_all_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as ifile:
         return ifile.read()

def write_text_to_file(filename, text):
    with open(filename, 'w', encoding="utf-8") as ofile:
        ofile.write(text)

def sort_text_by_lines(text):
    """
    >>> sort_text_by_lines('abc\\nzxy\\nklm')
    'abc\\nklm\\nzxy'

    >>> sort_text_by_lines('new y:ear\\nkxy dfs s\\nklm test test')
    'klm test test\\nkxy dfs s\\nnew y:ear'
    """

    lines = text.split('\n')
    return '\n'.join(sorted(lines))

doctest.testmod()

text = read_all_from_file('plan.txt')
write_text_to_file('plan_sorted.txt', sort_text_by_lines(text))