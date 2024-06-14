# Задача 1. Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет. Ваша программа должна предоставить ответ "True" (дата корректна) или
# "False" (дата некорректна) в зависимости от результата проверки.

# from sys import argv
#
#
# def is_leap(year: int):
#     return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
#
#
# def valid(full_date: str):
#     date, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
#         return False
#     if month in (4, 6, 9, 11) and date > 30:
#         return False
#     if month == 2 and is_leap(year) and date > 29:
#         return False
#     if month == 2 and not is_leap(year) and date > 28:
#         return False
#     return True
#
#
# date_to_prove = '15.4.2023'
# if len(argv) > 1:
#     print(valid(argv[1]))
# else:
#     print(valid(date_to_prove))

# Задача 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8
# ферзях, включающий в себя функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не
# били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
# друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

# from itertools import combinations
#
#
# def is_attacking(q1, q2):
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
#
# def check_queens(queens):
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
#
# print(check_queens(queens=[(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))

# Задача 3.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки. Под "успешной расстановкой ферзей" в данном контексте подразумевается
# такая расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены
# таким образом, что они не находятся на одной вертикали, горизонтали или диагонали. Список из 4х комбинаций координат
# сохраните в board_list. Дополнительно печатать его не надо.

# import random
# from itertools import combinations
#
#
# def generate_board():
#     board = []
#
#     for i in range(1, 8 + 1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board
#
#
# def is_attacking(q1, q2):
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
#
# def check_queens(queens):
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
#
# def generate_boards():
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list
#
#
# board_list = generate_boards()
# if len(board_list) != 4:
#     print("Вы собрали не то количество комбинаций")
# else:
#     print("Отлично!")