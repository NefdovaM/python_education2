# Задание №1
# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# def print_words(text):
#     words = sorted(text.split())
#     # max_len = max(len(word) for word in words)
#     max_len = len(max(words, key=len))
#     # print(max_len)
#
#     for i, word in enumerate(words, 1):
#         space = ' '*(max_len - len(word) + 1)
#         # print(f'{i}.{space}{word}')
#         # print(f'{i:<3} {word:>{max_len}}')
#         print(str(i).ljust(3), word.rjust(max_len))
#
#
# input_text = input('Введите произвольный текст: ')
# print_words(input_text)


# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


# def my_func(str_in):
#     print(sorted(map(ord, set(str_in)), reverse = True))
#
# my_text = 'символа введённой строки отсортированный по убыванию'
# my_func(my_text)


# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно


# def my_function(text: str) -> dict[str, int]:
#     """Documentation."""
#     num_min, num_max = sorted(map(int, text.split()))
#     return {chr(num): num for num in range(num_min, num_max + 1)}
#
#
# print(my_function('100 60'))


# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант, напишите сортировку пузырьком. Её описание есть в википедии.

# def my_sort(lst: list[int]) -> None:
#     for i in range(len(lst)):
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#
#
# nums = [5, 8, 2, 7, 3, 9, 1]
# print(nums)
# my_sort(nums)
# print(nums)

# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
#     ✔ имена str,
#     ✔ ставка int,
#     ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

# def my_func(names: list[str] = ['Vasya'], salaries: list[int] = [10_000],
#             bonuses: list[str] = ['10%']) -> dict:
#     """Documentation."""
#     # return {
#     #     name: salary * float(bonus[:-1]) / 100
#     #     for name, salary, bonus in zip(names, salaries, bonuses)
#     # }
#     return dict(
#         map(
#             lambda cur_tuple: (cur_tuple[0], cur_tuple[1] * float(cur_tuple[2][:-1]) / 100),
#             zip(names, salaries, bonuses)
#         )
#     )
#
#
# names_out = ['Ivanov', 'Petrov', 'Sidorov']
# rates_out = [10_000, 12_000, 15_000]
# awords_out = ['15.75%', '12.50%', '10.25%']
#
# print(my_func(bonuses=awords_out, names=names_out, salaries=rates_out))

# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

#
# lst = [3, 4, 5, 2, 3, 1, 7, 9, 3]
# indices = [-2, 1]
#
#
# def sum_by_ind(lst, lst_ind):
#     if lst_ind[0] > lst_ind[1]:
#         lst_ind[0], lst_ind[1] = lst_ind[1], lst_ind[0]
#     sum_ = 0
#     for i, item in enumerate(lst):
#         if lst_ind[0] <= i < lst_ind[1] + 1:
#             sum_ += item
#
#     return sum_
#
#
# print(*enumerate(lst))
# print(sum(lst))
# print(sum_by_ind(lst, indices))

# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы
# одна убыточная — ложь.

# def my_func(my_dict: dict) -> bool:
# # return all(sum(value) > 0 for value in my_dict.values())
#     return all(map(lambda x: sum(x) > 0, my_dict.values()))
#
# income_statement = {
#     'ForEx': [125_000, -75_550, 85_000, -64_300, 20_000],
#     'Vertex': [225_750, 145_5000, -179_950, -450_000, 152_000],
#     'RosAl': [175_800, -225_000, -330_000, 127_880, 25_750]
# }
#
# print(my_func(income_statement))


# Задание №8
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
#
# def my_func():
#     dict_vars = globals()
#     dict_new_vars = {}
#     for key, value in dict_vars.items():
#         if key.endswith("s") and key != "s":
#             dict_new_vars[key[:-1]] = value
#             dict_vars[key] = None
#             dict_vars.update(dict_new_vars)
#
#
# datas = [42, -73, 12, 85, -15, 2]
# s = 'Hello world!'
# names = ('NoName', 'OtherName', 'NewName')
# sx = 42
#
# print(globals())
# my_func()
# print(globals())
# print(datas, s, names, sx)
# print(name, data)