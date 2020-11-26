class MyTypeError(Exception):
    def __str__(self):
        return 'Wrong value'


data_list = []
stop = False


def control_value(element):
    if element.isdigit():
        data_list.append(int(element))
    elif element.replace('.', '').isdigit():
        data_list.append(float(element))
    else:
        raise MyTypeError(element)


while not stop:
    data = input("Enter numbers separated by space. To stop type 'STOP' >>> ").split()
    for el in data:
        try:
            control_value(el.rstrip(','))
        except MyTypeError as exception:
            if el.rstrip(',').lower() == 'stop':
                stop = True
            else:
                print(f"{el.rstrip(',')} is't a digit")
                continue

print(data_list)
