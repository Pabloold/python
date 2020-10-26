import random

words_bank = [
    'автострада', 'бензин', 'инопланетянин', 'библиотека', 'олимпиада'
]

secret_word = random.choice(words_bank)
#print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('Введите ОДНУ русскую букву: ')
    # TODO: letter validation -> if, ord(), re
    if len(letter) != 1:
        continue

    if letter in secret_word:
        for symbol in enumerate(secret_word):
            if symbol == letter:
                pass
            print(symbol)
    else:
        errors_counter += 1
        print('Ошибок допущено:', errors_counter)
        if errors_counter == 8:
            print('Вы проиграли')
            break

    print(''.join(gamer_word))