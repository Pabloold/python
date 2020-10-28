# Чтобы запустить код удалите кавычки в начале и конце кода

# Упражнение №1
"""
a = input('Введите что-нибудь ')
b = int(input('Введите число '))
c = float(input('Введите дробное чилсо '))

print(a)
print(b)
print(c)
"""

# Упражнение №2
'''
user_time = int(input('Введите секунды '))
hour = user_time // 3600
minutes = user_time % 3600 // 60
seconds = user_time % 60

print(f'{hour:02d}:{minutes:02d}:{seconds:02d}')
'''

# Упражнение №3
'''
numb = input('Введите число от 1 до 9 ')
nsum = int(numb) + int(numb * 2) + int(numb * 3)
print(nsum)
'''

# Упражнение №4
'''
user_number = int(input('Введите число >>> '))
max_figure = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_figure:
        max_figure = user_number % 10
    user_number = user_number // 10
print(max_figure)
'''

# Упражнение №5
'''
money_in = float(input('Введите вашу выручку '))
money_out = float(input('Введите ваши издержки '))
result = money_in - money_out

if result > 0:
    print(f'Ваша прибыль: {result:.2f}')
    rentable = result / money_in * 100
    print(f'Рентабельность: {rentable:.2f} %')
    workers = int(input('Сколько у вас работает человек? '))
    result_per_worker = result / workers
    print(f'Прибыль фирмы на сотрудника - {result_per_worker:.2f}')
elif result < 0:
    print(f'Ваш убыток: {result:.2f}')
else:
    print('Ваша фирма работает в 0')
'''

# Упражнение №6
'''
start = int(input('Сколько вы пробегаете сейчас? '))
finish = int(input('Сколько вы хотите пробегать в итоге при увеличения расттояния на 10% в день? '))
day = 1

while start < finish:
    start *= 1.1
    day += 1
print(f'Вы достигните цели на {day} день')
'''
