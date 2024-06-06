# Задание №1 Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь,
# где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
#
# numbers = '10/12/1/4/28/30/35'
# number_list = numbers.split('/')
# key1, key2, key3 = int(number_list[0]), int(number_list[1]), int(number_list[2])
# values = tuple(map(int, number_list[3:]))
# my_dict = {key2: key1, key3: values}
# print(my_dict)
#
# st_list = '12/4/5/78/9/4'.split('/')
# res_dic = dict()
# res_dic[st_list[1]], res_dic[st_list[2]] = st_list[0], tuple(st_list[3:])
# print(res_dic)
#
# input_string = '12/4/5/78/9/4'
# numbers = input_string.split('/')
# if len(numbers) < 4:
#     print("Ошибка: необходимо ввести минимум четыре числа.")
# else:
#     numbers = list(map(int, numbers))
#
# result_dict = {
#     numbers[1]: numbers[0],
#     numbers[2]: tuple(numbers[3:])
# }
# print(result_dict)
#
# str_use = '12/4/5/78/9/4'
# lst_2 = [int(s) for s in str_use if s.isdigit()]
# print(lst_2)
# my_dict = {lst_2[1]: lst_2[0], lst_2[2]: lst_2[3::]}
# print(my_dict)
#
# one, two, three, *other = input('Какой текст преобразовать? ').split('/')
# print(map(int, other))
# print(tuple(map(int, other)))
# result = {
#     int(two): int(one),
#     int(three): tuple(map(int, other)),
# }
# print(f'{result = }')

# Задание №2 Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, где ключ — буква,
# а значение — код буквы. Напишите преобразование в одну строку.
#
# text = 'В лесу родилась елочка'
# my_dict = {char: ord(char) for char in text if char != ' '}
# print(my_dict)

# Задание №3 Продолжаем развивать задачу 2. Возьмите словарь, который вы получили. Сохраните его итератор.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
#
# text = 'В лесу родилась елочка'
# my_dict = {char: ord(char) for char in text if char != ' '}
# print(my_dict)
# count = 5
# my_iter = iter(my_dict.items())
# for _ in range(count):
#     print(next(my_iter))

# Задание №4 Создайте генератор чётных чисел от нуля до 100. Из последовательности исключите числа, сумма цифр которых
# равна 8. Решение в одну строку.

# for i in range(0, 101, 2):
#     if sum(map(int, str(i))) != 8:
#         print(i)
#
# my_gen = (i for i in range(101) if (i % 2 == 0) & (i // 10 + i % 10 != 8))
# print(*my_gen)

# Вариант 2
#
# [print(i) for i in range(2, 101, 2) if sum(map(int, str(i))) != 8]

# Задание №5 Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz». Вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
# то программа должна выводить слово «FizzBuzz». Превратите решение в генераторное выражение.
#
# for i in range(1, 101):
#     if i % 3 == i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
#
# print(*('FizzBuzz' if i % 3 == i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in
#         range(1, 101)), sep='-')

# Задание №5 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке. Таблицу создайте в виде
# однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения. Для вывода результата
# используйте «принт» без перехода на новую строку.

# def my_gen(num):
#     start = 2
#     count = 0
#     while count < num:
#         for i in range(2, int(start ** 0.5 + 1)):
#             if start % i == 0:
#                 break
#             else:
#                 count += 1
#     yield start
#     start += 1
#
#
# N = 5
#
# for num in my_gen(N):
#     print(num)
# my_iter = iter(my_gen(N))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))