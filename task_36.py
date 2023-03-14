# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))


def key_value(lst):
    return tuple(lst.split("="))


def create_tuples(stroka, func):
    stroka = stroka.split()

    print(tuple(map(func, stroka)))


create_tuples(input("Введите строку: "), key_value)