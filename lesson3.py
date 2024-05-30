# Задание №1 Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка. *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
# data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
#
# print(list(set(data)))
#
# my_list = []
# for item in data:
#     if item not in my_list:
#         my_list.append(item)
#
# print(my_list)
# my_list = []
# print([my_list.append(item) for item in data if item not in my_list])
# print(my_list)
# my_list = [item ** 2 for item in data]
# print(my_list)
# my_list = [item if item not in my_list else 0 for item in data]
#
# my_set = {item ** 2 for item in data}
# my_dict = {item: item ** 2 for item in data}
# my_gen = (item ** 2 for item in data)

# Задание №3 Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в нижнем регистре в остальных случаях
#
# user_input = input('Enter data: ')
#
# if user_input.isdigit():
#     user_input = int(user_input)
# elif user_input.replace('-', '').replace('.', '').isdigit() and \
#     user_input.count('.') < 2 and '-' not in user_input[1:]:
#     user_input = float(user_input)
# elif user_input.lower() != user_input:
#     user_input = user_input.lower()
# else:
#     user_input = user_input.upper()
# print(user_input)

# Задание №3 Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где:
# ключ — тип элемента, значение — список элементов данного типа.

# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
# my_dict = {}
#
# for item in data:
#     if type(item).__name__ not in my_dict:
#         my_dict[type(item).__name__] = [item]
#     else:
#         my_dict[type(item).__name__].append(item)
#
# print(my_dict)
#
# # №2
# my_dict = {}
# for item in data:
#     my_dict[type(item).__name__] = my_dict.get(type(item).__name__, [])
#     my_dict[type(item).__name__].append(item)
#
# print(my_dict)
#
# # №3
# my_dict = {}
# for item in data:
#     my_dict.setdefault(type(item).__name__, []).append(item)
#
# print(my_dict)

# Задание 4. Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
#
# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
# COUNT = 2
# for item in data:
#     if data.count(item) == COUNT:
#         for _ in range(COUNT):
#             data.remove(item)
# print(data)

# Задание 5. Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# Нумерация начинается с единицы.
#
# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
# new_data = []
#
# for i, item in enumerate(data, 1):
#     if item % 2 == 1:
#         new_data.append(i)
#
# print(new_data)

# Задание 6. Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# value = input('Enter some words:\n').split()
# max_len = max(len(item) for item in value)
#
# value.sort()
# for i, item in enumerate(value, 1):
#     print(f'{i} {item:>{max_len}}')

# Задание 7. Пользователь вводит строку текста.Подсчитайте сколько раз встречается каждая буква в строке без
# использования метода count и с ним. Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке. Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в
# ваших решениях.

# my_text = input('Enter some text:\n')
# my_dict = {}
# my_new_text = my_text.replace(" ", "")
# for letter in my_new_text:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
#
# for key, value in my_dict.items():
#     print(f'{key}: {value}')
#
# my_dict = {key: my_new_text.count(key) for key in set(my_new_text)}
# print(my_dict)

# Задание 8. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
#
# hike = {
#     'Ваня': ('спички', 'нож', 'парафин', 'веревка', 'рюкзак' ),
#     'Вася': ('карта', 'компас', 'топор', 'нож', 'рюкзак', 'уголь'),
#     'Петя': ('навигатор', 'мангал', 'гитара', 'спички', 'палатка', 'нож', 'топор'),
#     'Лена': ('косметичка', 'мобильник', 'рюкзак', 'планшет')
# }
#
# # Вещи, взятые всеми тремя друзьями
# all_friends_items = set(hike['Ваня']) & set(hike['Вася']) & set(hike['Петя'])
#
# # Вещи, уникальные для каждого друга
# unique_items = set()
# for friend, items in hike.items():
#     other_items = set()
# for other_friend, other_friend_items in hike.items():
#     if other_friend != friend:
#         other_items.update(other_friend_items)
# unique_items.update(set(items) - other_items)
#
# # Вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# missing_items = {}
# all_items = set()
# for items in hike.values():
#     all_items.update(items)
#
# for item in all_items:
#     friends_with_item = [friend for friend in hike if item in hike[friend]]
# if len(friends_with_item) == len(hike) - 1:
#     missing_friend = [friend for friend in hike if friend not in friends_with_item][0]
# if missing_friend in missing_items:
#     missing_items[missing_friend].add(item)
# else:
#     missing_items[missing_friend] = {item}
#
#
# print("Вещи, взятые всеми тремя друзьями:", all_friends_items)
# print("Уникальные вещи у каждого друга:", unique_items)
# print("Вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:")
# for friend, items in missing_items.items():
#     print(f"У {friend} отсутствуют: {items}")