name = input('Введите имя: ').capitalize()
s_name = input('Введите фамилию: ').capitalize()
y_birthd = input('Введите год рождения: ')
sity = input('Введите город проживания: ').capitalize()
email = input('Введите ваш email: ').lower()
fone_number = input('Введите ваш телефон: ')


def user_info(a_6, a_5, a_4, a_3, a_2, a_1):
    return ' '.join([a_2, a_1, a_3, a_4, a_6, a_5])


print(user_info(a_1=name, a_2=s_name, a_3=y_birthd, a_4=sity, a_5=email, a_6=fone_number))
