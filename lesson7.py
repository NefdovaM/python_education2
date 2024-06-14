# Задание №1. Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

# import random
# from pathlib import Path
#
#
# def random_editer(str_num: int, file_name: str | Path) -> None:
#     with open(file_name, 'a', encoding='utf-8') as file:
#         for _ in range(str_num):
#             int_num = random.randint(-1000, 1000)
#             float_num = random.uniform(-1000, 1000)
#             # file.write(f'{int_num} | {float_num}\n')
#         print(f'{int_num} | {float_num}', file=file)
#
#
# if __name__ == '__main__':
#     random_editer(10, 'numbers.txt')

# Задание №2. Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из
# 4-7 букв, среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.

# from random import randint, choice
# from pathlib import Path
#
# VOWELS = 'eyuioa'
# CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
# MIN_LEN = 4
# MAX_LEN = 7
#
#
# def pseudonames_gen(str_num: int, file_name: str | Path) -> None:
#     with open(file_name, 'a', encoding='utf-8') as f:
#         flag: bool = choice([True, False])
#     for _ in range(str_num):
#         name = ''
#     for i in range(randint(MIN_LEN, MAX_LEN)):
#         if flag:
#             name += choice(VOWELS)
#         else:
#             name += choice(CONSONANTS)
#             flag = not flag
#             f.write(name.title() + '\n')
#
#
# if __name__ == '__main__':
#     pseudonames_gen(10, 'names.txt')

# Задание №3. Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение: если результат умножения отрицательный, сохраните
# имя записанное строчными буквами и произведение по модулю если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого. В результирующем файле должно быть столько же строк,
# сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало.

# from pathlib import Path
# from typing import TextIO
#
#
# def read_line_or_begin(fd: TextIO) -> str:
#     line = fd.readline()
#     if line == '':
#         fd.seek(0)
#         line = fd.readline()
#     return line[:-1]
#
#
# def convert(names: str | Path, numbers: str | Path, results: str | Path) -> None:
#     with (
#         open(names, 'r', encoding='utf-8') as f_names,
#         open(numbers, 'r', encoding='utf-8') as f_numbers,
#         open(results, 'w', encoding='utf-8') as f_results
#     ):
#     # len_names = len(f_names.readlines())
#     # len_numbers = len(f_numbers.readlines())
#     len_names = sum(1 for _ in f_names)
#     len_numbers = sum(1 for _ in f_numbers)
#     for _ in range(max(len_names, len_numbers)):
#         name = read_line_or_begin(f_names)
#     # print(name)
#     number = read_line_or_begin(f_numbers)
#     a, b = map(float, number.split(' | '))
#     res = a * b
#     if res < 0:
#         f_results.write(f'{name.lower()} {-res}\n')
#     elif res > 0:
#         f_results.write(f'{name.upper()} {round(res)}\n')
#
#
# if __name__ == '__main__':
#     convert(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))

# Задание №4. Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 15
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 3
# Имя файла и его размер должны быть в рамках переданного диапазона.

# import os
# from string import ascii_letters, ascii_lowercase
# from random import randint, choices, randbytes
#
#
# def file_gen(
#         extent: str,
#         min_len: int = 6,
#         max_len: int = 30,
#         min_size: int = 256,
#         max_size: int = 4096,
#         file_num: int = 3
# ) -> None:
#     for _ in range(file_num):
#         data = bytes(randint(0,255)) for i in range(randint(min_size, max_size))
#         data = randbytes(randint(min_size, max_size))
#
#     file_name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len, max_len)))
#     with open(f'C:\\Users\\annao\\Documents\\NEW_LIFE_PYTHON\\new_file\\{file_name}.{extent}', 'wb') as f_wb:
#         f_wb.write(data)


# Задание №5. Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров. Количество переданных расширений может быть
# любым. Количество файлов для каждого расширения различно. Внутри используйте вызов функции из прошлой задачи.

# def gen_files(**kwargs) -> None:
#     for extent, count in kwargs.items():
#         file_gen(extent, file_num=count)
#
#
# if __name__ == '__main__':
#     gen_files(txt=2, jpeg=1)

# Задание №6. Дорабатываем функции из предыдущих задач. Генерируйте файлы в указанную директорию — отдельный параметр
# функции. Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
#
#
# import os
# from string import ascii_lowercase, digits
# from random import randint, choices, randbytes
# from pathlib import Path
#
#
# def file_gen(
#         extent: str,
#         min_len: int = 6,
#         max_len: int = 30,
#         min_size: int = 256,
#         max_size: int = 4096,
#         file_num: int = 3
# ) -> None:
#     for _ in range(file_num):
#         # data = bytes(randint(0,255)) for i in range(randint(min_size, max_size))
#         data = randbytes(randint(min_size, max_size))
#
#
# file_name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len, max_len)))
# with open(f'{Path.cwd()}\\{file_name}.{extent}', 'wb') as f_wb:
#     f_wb.write(data)
#
#
# def gen_files(path: Path | str, **kwargs) -> None:
#     if isinstance(path, str):
#         path = Path(path)
#
#
# if not path.is_dir():
#     path.mkdir(parents=True)
#     os.chdir(path)
#     for extent, count in kwargs.items():
#         file_gen(extent, file_num=count)
#
# if __name__ == '__main__':
#     gen_files(r'C:\Users\khokh\PycharmProjects\Sem_7\ex1\test', txt=2, jpeg=1)

# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения,
# текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для
# сортировки.

# import os
# import task_6 as tsk
# from pathlib import Path
#
#
# def sort_files(path: Path | str, groups: dict[Path, list[str]] = None) -> None:
#     if groups is None:
#         groups = {
#             Path("video"): ['avi', 'mkv'],
#             Path("pic"): ['png', 'jpg'],
#             Path("music"): ['mp3']
#         }
#
#
# if isinstance(path, str):
#     path = Path(path)
#
# os.chdir(path)
# for target_dir, ext_list in groups.items():
#     if not target_dir.is_dir():
#         target_dir.mkdir()
# for file in list(os.walk(Path.cwd()))[0][-1]:
#     if file.split('.')[-1] in ext_list:
#         os.replace(file, os.path.join(target_dir, file))
#
# # tsk.gen_files(r'C:\Users\khokh\PycharmProjects\Sem_7\ex1\test', avi=2, mkv=1, png=2, mp3=2, jpg=2)
# variable = r'C:\Users\khokh\PycharmProjects\Sem_7\ex1\test'
# sort_files(variable)
