def fib_gen(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        yield total


while True:
    try:
        number = int(input('Введите целое положительное число для вычисления факториала '))
        if number > 0:
            break
        else:
            print('Введено число < 1')
            continue
    except ValueError:
        print('Неверный формат числа!')

x = 1

for el in fib_gen(number):
    if not x > number:
        print(f'{x}! {el}')
        x += 1
    else:
        break
fib_list = [el for el in fib_gen(number)]
print(fib_list)
