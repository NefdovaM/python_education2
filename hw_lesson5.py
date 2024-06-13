# Задача 1. Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)
#
# print(get_file_info(file_path = 'C:/Users/User/Documents/example.txt'))

# Задача 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида 10.25%. В результате result получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.

# def generate_salary_dict(names_list, salaries_list, bonuses_list):
#     return {name: (round(salary * (1 + float(bonus.strip('%')) / 100) - salary, 0)) for name, salary, bonus in
#             zip(names_list, salaries_list, bonuses_list)}
#
#
# names = ["Eva", "David", "Frank"]
# salary = [7500, 8000, 9000]
# bonus = ["8%", "12%", "7%"]
#
# salary_dict = generate_salary_dict(names, salary, bonus)
# print(salary_dict)

# # Задача 3. Создайте функцию генератор чисел Фибоначчи fibonacci
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# f = fibonacci()
# for i in range(10):
#     print(next(f))
