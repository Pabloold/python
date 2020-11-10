with open('task3.1.txt') as salary_list:
    low_salary, average_salary = [], []
    my_list = salary_list.read().split('\n')
    for el in my_list:
        el = el.split()
        if int(el[1]) < 20000:
            low_salary.append(el[0])
        else:
            average_salary.append(int(el[1]))
    print('Сотрудники c окладом < 20000:', ', '.join(low_salary))
    print(f'Средний оклад у остальных сотрудников = {sum(average_salary) / len(average_salary)}')

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
russian_numbers = []

with open('task3.2.txt') as file:
    for i in file:
        i = i.split(' ', 1)
        russian_numbers.append(rus_dict.get(i[0]) + ' ' + i[1])

with open('result3.2.txt', 'w') as new_file:
    new_file.writelines(''.join(russian_numbers))

with open('result3.2.txt') as new_file:
    print(new_file.read())
