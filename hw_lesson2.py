# Задача 1. Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
#
# num = 255
# HEX = 16
# hex_digits = '0123456789ABCDEF'
#
# def to_hex(num):
#     hex_str = ''
#     while num > 0:
#         hex_str = hex_digits[num % HEX] + hex_str
#         num = num // HEX
#     return hex_str
#
# hex_str = to_hex(num)
#
# print(f'Шестнадцатеричное представление числа: {hex_str}')
# print(f'Проверка результата: {hex(num)}')

# Задача 2. На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
#
# from fractions import Fraction
# frac1 = '2/5'
# frac2 = '3/5'
#
# numerator1_str, denominator1_str = frac1.split('/')
# numerator2_str, denominator2_str = frac2.split('/')
#
# numerator1 = int(numerator1_str)
# denominator1 = int(denominator1_str)
# numerator2 = int(numerator2_str)
# denominator2 = int(denominator2_str)
#
# common_denominator = denominator1 * denominator2
#
# new_numerator1 = numerator1 * denominator2
# new_numerator2 = numerator2 * denominator1
#
# summation_numerator = new_numerator1 + new_numerator2
# multiplication_numerator = numerator1 * numerator2
#
# print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
# print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")
#
# fraction1 = Fraction(frac1)
# fraction2 = Fraction(frac2)
#
# summation = fraction1 + fraction2
# multiplication = fraction1 * fraction2
#
# print(f"Сумма дробей: {summation}")
# print(f"Произведение дробей: {multiplication}")
