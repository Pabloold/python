def summary():
    fin_sum = 0
    ex = False
    while not ex:
        in_sum = 0
        numbers = input('Введите числа через пробел. Для выхода введите q или й: ').split()
        for el in numbers:
            if el.lower() == 'q' or el.lower() == 'й':
                ex = True
                break
            else:
                try:
                    in_sum += float(el)
                except ValueError:
                    print('Было введено не число!')
        fin_sum += in_sum
        print(f'Сумма введённых чисел равна: {fin_sum}')


summary()
