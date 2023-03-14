# # Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# # Поскольку разобраться в его кричалках не настолько просто, насколько легко
#  он их придумывает, Вам стоит написать программу.
# # Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# # Фразы отделяются друг от друга пробелами.
# # Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# # **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# #     **Вывод:** Парам пам-пам


vowels = "аеиоуыэюя"


def count_vowels(phrase):
    counter = 0
    for el in phrase:
        if el in vowels:
            counter += 1
    return counter


def find_rhythm(poem, func):
    poem = poem.split()

    result = set(map(func, poem))

    if len(result) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")


find_rhythm(input("Введите стих: "), count_vowels)
