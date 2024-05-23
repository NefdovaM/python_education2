# Задание №1 Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.
#
# my_int = 10
# my_float = 1.5
# my_str = 'Hello world'
# my_tuple = (1, 2, 3)
#
# print(
#     f'{my_int = } имеет тип {type(my_int)}\n'
#     f'{my_float = } имеет тип {type(my_float)}\n'
#     f'{my_str = } имеет тип {type(my_str)}\n'
#     f'{my_tuple = } имеет тип {type(my_tuple)}'
# )
#
# Задание №2 Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
#
# import sys
# import typing
# a = 256
# # data = [1, 2.3, 'Hellow world!', {'key1': 83}, (1, [2], 3), True, 2.3]
# data = [a, 256, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!', 73.0]
# for i, item in enumerate(data, start=1):
#     check_int = 'Это число' if isinstance(item, int) else ''
#     check_str = 'Это строка' if isinstance(item, str) else ''
#     # check_hash = 'Не хэшируем' if isinstance(item, (dict, list, set)) else
#     # hash(item)
#     # check_hash = 'Не хэшируем' if not isinstance(item, typing.Hashable) \
#     #     else hash(item)
#     try:
#         check_hash = hash(item)
#     except TypeError:
#         check_hash = 'Не хэшируем'
#
#     print(
#         f"{i=}, {item=}, {id(item)=}, {sys.getsizeof(item)=}, "
#         f"{item.__sizeof__()=}, {check_hash=}, {check_int=}{check_str=}"
#     )
# print(id(a))
#
# Задание №3 Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое
# представление. Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
#
# OCT = 8
# BIN = 2
# HEX = 16
# num: int = int(input('Enter a number: \n'))
# print(bin(num), oct(num), hex(num))
#
# for div in (BIN, OCT):
#     new_num = num
#     result: str = ''
#     while new_num:
#         result = str(new_num % div) + result
#         new_num //= div
#     print(result)

# Задание №4 Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не
# превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

# from math import pi
# import decimal
#
# decimal.getcontext().prec = 10
# PI = decimal.Decimal(pi)
#
# while (d := decimal.Decimal(input('Enter diameter: \n'))) > 1000:
#     print('Enter a number  less than 1000')
#
# circle_length = PI * d
# circle_square = PI * pow(d / 2, 2)
# print(circle_length, circle_square)
#
# circle_length = pi * float(d)
# circle_square = pi * pow(float(d) / 2, 2)
#
# print(circle_length, circle_square)


# import math
#
# # Задание №5 Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. Используйте
# # комплексные числа для извлечения квадратного корня.
#
# a = 2
# b = 3
# c = 3
#
# d = b ** 2 - 4 * a * c
# x1 = (-b + d ** .5) / (2 * a)
# x2 = (-b - d ** .5) / (2 * a)
#
# print(x1, x2)

# Задание №6 Напишите программу банкомат. Начальная сумма равна нулю:
# Допустимые действия: пополнить, снять, выйти. Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от
# суммы снятия, но не менее 30 и не более 600 у.е.После каждой третей операции пополнения или снятия начисляются проценты
# - 3%. Нельзя снять больше, чем на счёте. При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной. Любое действие выводит сумму денег:

# import decimal
#
# CMD_REPLENISH = 'r'
# CMD_WITHDRAW = 'w'
# CMD_EXIT = 'e'
# MULTIPLICITY = 50
# PERCENTAGE_4_WITHDRAWAL = decimal.Decimal(15) / decimal.Decimal(1000) # some explanation
# MIN_FEE = 30
# MAX_FEE = 600
# COUNT_OPERATION = 3
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# LUXURY_TAX = decimal.Decimal(10) / decimal.Decimal(100)
# LUXURY_LIMIT = decimal.Decimal(5_000_000)
#
# balance = decimal.Decimal(0)
# count = 0
# while True:
#     cmd = input(f'Enter command ({CMD_REPLENISH} = replenish, {CMD_WITHDRAW} = withdraw, '
#                 f'{CMD_EXIT} = exit:\n')
#     if cmd == CMD_EXIT:
#         print(f'Balance: {balance}\nBy-by')
#         break
#     if balance > LUXURY_LIMIT:
#         tax_amount = balance * LUXURY_TAX
#         balance = balance - tax_amount
#         print(f'The wealth tax has been written off in the amount of '
#               f'{tax_amount}. Balance: {balance}')
#     if cmd in (CMD_REPLENISH, CMD_WITHDRAW):
#         amount = decimal.Decimal(input(f'Enter amount multimple {MULTIPLICITY} :\n'))
#         while amount % MULTIPLICITY:
#             amount = decimal.Decimal(input(f'Enter amount multimple {MULTIPLICITY} :\n'))
#         if cmd == CMD_WITHDRAW:
#             withdrawal_fee = amount * PERCENTAGE_4_WITHDRAWAL
#             withdrawal_fee = MIN_FEE if withdrawal_fee < MIN_FEE else \
#                 MAX_FEE if withdrawal_fee > MAX_FEE else withdrawal_fee
#             withdrawal_amount = amount + withdrawal_fee
#             if balance > withdrawal_amount:
#                 balance = balance - withdrawal_amount
#                 print(f'Transaction amount = {amount}, withdrawal commission = {withdrawal_fee}, balance = {balance}')
#                 count += 1
#             else:
#                 print(f'Insufficient funds. Balance: {balance}. Withdrawal amount = {withdrawal_amount}.')
#         elif cmd == CMD_REPLENISH:
#             balance += amount
#             print(f'Your balance is {balance}')
#             count += 1
#
#         if count % COUNT_OPERATION == 0:
#             bonus = balance * PERCENT_DEPOSIT
#             balance = balance + bonus
#             print(f'You have performed three operations. Your bonus is {bonus}. Balance is '
#                   f'{balance}')