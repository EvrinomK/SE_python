def count_str_from_file(filename, substr):
    with open(filename, 'r', encoding="utf-8") as ifile:     
        text = ifile.read()
        return text.count(substr)

print(count_str_from_file('text_18.7.txt', 'тест'))