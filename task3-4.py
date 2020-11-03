while True:
    try:
        dev_1 = float(input('Введиет положительное число для возведения в степень: '))
        dev_2 = int(input('Введите отрицательное целое число: '))
        break
    except ValueError:
        print('Неверный формат!!!')

print(f'Результат: {(lambda a, b: a ** b)(dev_1, dev_2):.10f}')


def power(a, b):
    result = 1
    for i in range(abs(b)):
        result *= a
    if b >= 0:
        return result
    else:
        return 1 / result


print(f'Результат: {power(dev_1, dev_2):.10f}')
