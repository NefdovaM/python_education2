# Задача 1. Список вещей для похода.
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность. Предметы не должны
# дублироваться. Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# def backpack(items, max_weight):
#     possible_items = dict()
#     for key, value in items.items():
#         if value <= max_weight:
#             possible_items[key] = value
#             max_weight -= value
#     return possible_items
#
#
# items = {"ключи": 0.3, "кошелек": 0.2, "телефон": 0.5, "зажигалка": 0.1}
#
# max_weight = 5.0
#
# backpack = backpack(items, max_weight)
# print(backpack)

# Задача 2. В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. Слова разделяются пробелами. Такие слова как don t, it s, didn t
# итд (после того, как убрали знак препинания апостроф) считать двумя словами. Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# import re
# from collections import Counter
#
#
# def top_10_words(text):
#     words = re.findall(r'(\b[^\d\W]+\b)', text.lower())
#     words.sort(reverse=True)
#     return Counter(words).most_common(10)
#
#
# top = top_10_words(text)
#
# print(top)

# Задача 4. Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
#
#
# def find_duplicates(lst):
#     return list(set([x for x in lst if lst.count(x) > 1]))
#
#
# lst = [1, 1, 2, 2, 3, 3]
# print(find_duplicates(lst))