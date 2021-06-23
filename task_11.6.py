from random import choice

words = ['самовар', 'весна', 'лето'] 
random_word = choice(words)
random_char = choice(random_word)
ask_word = random_word.replace(random_char, '?')
print(ask_word)
result_char = input('Введите пропущенную букву: ')

if result_char == random_char:
    print('Вы угадали')
else:
    print('Вы не угадали')