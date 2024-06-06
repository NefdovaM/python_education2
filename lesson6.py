# Задание №2 создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу
# и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за
# заданное число попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина,
# а если попытки исчерпаны - ложь.
#
# import random
# from sys import argv
#
# __all__ = ['guess_number']
#
#
# def guess_number(lower_limit: int, upper_limit: int, attempts: int) -> bool:
#     hidden_number = random.randint(lower_limit, upper_limit)
#     for item in range(1, attempts + 1):
#         print(f"Attempt number: {item}")
#         user_num = int(input("Enter a number of your choice:\n"))
#         if user_num < hidden_number:
#             print("Your number is less then the target number")
#         elif user_num > hidden_number:
#             print("Your number is greater then the target number")
#         else:
#             print("You are right")
#             return True
#     print("You exhausted all attempts")
#     return False
#
#
# if __name__ == '__main__':
#     print(argv)
#     # guess_number(int(argv[1]), int(argv[2]), int(argv[3]))
#     # guess_number(*(int(num) for num in argv[1:]))
#     # guess_number(*(int(num) for num in param))
#     name, *param = argv
#     print(param)

# Задание №4 создайте модуль с функцией внутри. Функция получает на вход загадку, список с возможными вариантами
# отгадок и количество попыток на угадывание. Программа возвращает номер попытки, с которой была отгадана загадка
# или ноль, если попытки исчерпаны.
#
# def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
#     print(f"Угадайте загадку:\n{riddle}\n")
#     for attempt in range(1, attempts + 1):
#         answer = input(f"Попытка № {attempt}\n").lower()
#         if answer in answers:
#             return attempt
#     return 0
#
#
# if __name__ == '__main__':
#     my_answers = ['ель', 'ёлка', 'сосна']
#     result = secrets('Зимой и летом одним цветом', my_answers, 3)
#     print(f"Угадал с попытки {result}" if result > 0 else "Не угадал")

# Задание №5 добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря - загадка, значение -
# список с отгадками. Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
#
# def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
#     print(f"Угадайте загадку:\n{riddle}\n")
#     for attempt in range(1, attempts + 1):
#         answer = input(f"Попытка № {attempt}\n").lower()
#         if answer in answers:
#             return attempt
#     return 0
#
#
# def riddle_storage():
#     my_dict = {
#         'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
#         'Кто меня раздевает, тот слезы проливает': ['лук', 'луковица'],
#         'Летом серый, зимой белый': ['заяц', 'зайчик']
#     }
#     for key, value in my_dict.items():
#         result = secrets(key, value)
#         print(f"Угадал с попытки {result}\n" if result > 0 else "Не угадал\n")
#
#
# if __name__ == '__main__':
#     riddle_storage()

# Задание №6 добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки). И число (номер
# попытки, с которой она угадана). Функция формирует словарь с информацией о результатах отгадывания. Для хранения
# используйте защищённый словарь уровня модуля. Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.
#
# _data_dict = {}
#
#
# def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
#     print(f"Угадайте загадку:\n{riddle}\n")
#     for attempt in range(1, attempts + 1):
#         answer = input(f"Попытка № {attempt}\n").lower()
#         if answer in answers:
#             return attempt
#     return 0
#
#
# def save(puzzle: str, count: int) -> {}:
#     _data_dict.update({puzzle: count})
#
#
# def riddle_storage():
#     my_dict = {
#         'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
#         'Кто меня раздевает, тот слезы проливает': ['лук', 'луковица'],
#         'Летом серый, зимой белый': ['заяц', 'зайчик']
#     }
#     for key, value in my_dict.items():
#         result = secrets(key, value)
#         save(key, result)
#         print(f"Угадал с попытки {result}\n" if result > 0 else "Не угадал\n")
#
#
# def show_results():
#     result = (
#         f"Загадку {key} разгадали с {value} попытки." if value > 0
#         else f"Загадку {key} не разгадали."
#         for key, value in _data_dict.items()
#     )
#     print('\n'.join(result))
#
#
# if __name__ == '__main__':
#     riddle_storage()
#     show_results()

# Задание №7 создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию
#
#
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# def is_valid_date(date: str) -> bool:
#     day, month, year = map(int, date.split('.'))
#     if 1 <= year <= 9999:
#         if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
#             return True
#         elif month in [4, 6, 9, 11] and 1 <= day <= 30:
#             return True
#         elif month == 2 and 1 <= day <= 28 + is_leap_year(year):
#             return True
#     return False
#
#
# if __name__ == '__main__':
#     print(is_valid_date('02.12.2000'))
#     print(is_valid_date('02.12.1001'))
#     print(is_valid_date('02.23.2000'))
#     print(is_valid_date('50.12.2000'))
#     print(is_valid_date('02.12.10000'))
#     print(is_valid_date('29.02.2024'))