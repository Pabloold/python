with open('test.txt', 'w') as file:
    while True:
        line = input('Введите строку текста. Окончание ввода пустая строка ')
        if len(line) != 0:
            file.writelines(f'{line}\n')
        else:
            break
