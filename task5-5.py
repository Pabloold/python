my_dict, new_dict = {}, {}

with open('for_task5.txt') as file:
    for line in file:
        subject, lecture, practical, laboratory = line.split()
        my_dict[subject] = lecture + practical + laboratory

    for key, value in my_dict.items():
        new_string = ''
        key = key.replace(':', '')
        for symbol in value:
            if symbol.isdigit():
                new_string += ''.join(symbol)
            else:
                new_string += symbol.replace(symbol, ' ')
        result = 0
        for number in new_string.split():
            result += int(number)
        new_dict[key] = result

print(f'Общее количество занятий по предметам >>> {new_dict}')
