while True:
    try:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))
        third = float(input('Введите третье число: '))
        break
    except ValueError:
        print('Неверный формат!!!')


def sum_max(a, b, c):
    return max(a, b, c) + max(min(a, b), min(b, c), min(a, c))


print(sum_max(first, second, third))
