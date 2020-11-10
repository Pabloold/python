with open('task5.txt', 'w') as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers)
    sum_numbers = []
    for el in numbers.split():
        try:
            sum_numbers.append(float(el))
        except ValueError:
            print(f'Неверный формат числа {el}')
    print(f'Сумма введённых чисел = {sum(sum_numbers)}')
