# Задание 1. Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением
# чисел. Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

# import json
# from pathlib import Path
#
#
# def convert_to_json(file: str | Path) -> None:
#     data_dict = {}
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             name, number = line.split()
#             data_dict[name.title()] = float(number)
#
#     with open(file.stem + '.json', 'w', encoding='utf-8') as f_j:
#         json.dump(data_dict, f_j, indent=4, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     convert_to_json(Path('result.txt'))


# Задание 2. Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа
# (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо от
# уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.

# import json
# from pathlib import Path
#
#
# def set_user(path: Path) -> None:
#     id_set = set()
#
#     if path.is_file():
#         with open(path, 'r', encoding='utf-8') as f:
#             data_dict = json.load(f)
#             for id_name in data_dict.values():
#                 id_set.update(id_name)
#     else:
#         data_dict = {str(level): {} for level in range(1, 7 + 1)}
#
#     while True:
#         name = input("Enter your name:\n")
#         if not name:
#             break
#         id = input("Enter your id:\n")
#         if id not in id_set:
#             id_set.update(id)
#             level = input("Enter your access level:\n")
#             # data_dict[level].update({id: name})
#             data_dict[level][id] = name
#         else:
#             print(f'Entered id is not unique')
#
#     with open(path, 'w', encoding='utf-8') as f:
#         json.dump(data_dict, f, indent=2, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     set_user(Path('users.json'))

# Задание №3. Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
# import csv
# import json
# from pathlib import Path
#
#
# def json_2_csv(path: Path) -> None:
#     with (
#         open(path, 'r', encoding='utf-8') as f_read,
#         open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write
#     ):
#         data = json.load(f_read)
#         rows_list = []
#         for level, id_name in data.items():
#             for id, name in id_name.items():
#                 rows_list.append({'level': level, 'id': id, 'name': name})
#
#         csv_write = csv.DictWriter(
#             f_write,
#             fieldnames=['level', 'id', 'name'],
#             dialect='excel',
#             restval='Hello world',
#             quoting=csv.QUOTE_NONNUMERIC
#         )
#
#         csv_write.writeheader()
#         csv_write.writerows(rows_list)
#
#
# if __name__ == '__main__':
#     json_2_csv(Path('users.json'))

# Задание №4. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Дополните id до 10 цифр
# незначащими нулями. В именах первую букву сделайте прописной. Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
#
# import csv
# import json
# from pathlib import Path
#
#
# def csv_2_json(from_file: Path, to_file: Path) -> None:
#     json_list = []
#     with open(from_file, 'r', encoding='utf-8') as f_read:
#         csv_write = csv.reader(f_read)
#         for i, row in enumerate(csv_write):
#             if i != 0:
#                 json_dict = {}
#                 level, _id, name = row
#                 json_dict['level'] = int(level)
#                 # json_dict['id'] = _id.rjust(10, '0')
#                 json_dict['id'] = f'{int(_id):010}'
#                 json_dict['name'] = name.title()
#                 json_dict['hash'] = hash(f'{json_dict["name"]}{json_dict["id"]}')
#                 json_list.append(json_dict)
#     with open(to_file, 'w', encoding='utf-8') as f_write:
#         json.dump(json_list, f_write, indent=4)
#
#
# if __name__ == '__main__':
#     csv_2_json(Path('users.csv'), Path('new_users.json'))
#
# Задание №5 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
#
# import pickle
# from pathlib import Path
# import json
#
#
# def json_2_pickle(path: Path) -> None:
#     for file in path.iterdir():
#         if file.suffix == '.json':
#             with (
#                 open(file, 'r', encoding='utf-8') as f_read,
#                 open(f'{file.stem}.pickle', 'wb') as f_write
#             ):
#                 res = json.load(f_read)
#                 pickle.dump(res, f_write)
#
#
# if __name__ == '__main__':
#     json_2_pickle(Path(r'C:\Users\khokh\PycharmProjects\Sem_8'))

# Задание №6. Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 этого семинара. Функция должна извлекать ключи
# словаря для заголовков столбца из переданного файла.

# import pickle
# import csv
# from pathlib import Path
#
#
# def pickle_2_csv(path: Path) -> None:
#     with (
#         open(path, 'rb') as f_read,
#         open(f'{path.stem}.csv', 'w', encoding='utf-8') as f_write
#     ):
#         pickle_var = pickle.load(f_read)
#
#
# headers = list(pickle_var[0])
# csv_write = csv.DictWriter(
#     f_write,
#     fieldnames=headers,
#     dialect='excel',
#     quoting=csv.QUOTE_NONNUMERIC
# )
# csv_write.writeheader()
# csv_write.writerows(pickle_var)
#
# if __name__ == '__main__':
#     pickle_2_csv(Path('new_users.pickle'))

# Задание №7. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.Распечатайте его как
# pickle строку.

# import csv
# import pickle
# from pathlib import Path
#
#
# def csv_2_pickles(path: Path) -> None:
#     pickle_list = []
# with open(path, 'r', encoding='utf-8', newline='') as f_read:
#     csv_file = csv.reader(f_read)
# for i, line in enumerate(csv_file):
#     if i == 0:
#     headers = line
# else:
# pickle_dict = {key: value for key, value in zip(headers, line)}
# pickle_list.append(pickle_dict)
# print(pickle_list)
# print(pickle.dumps(pickle_list))
#
# with open(path, 'r', encoding='utf-8', newline='') as f_read:
#     second_csv_file = csv.DictReader(f_read)
# data = [row for row in second_csv_file]
# result = pickle.dumps(data)
# print(result)
#
#
# if __name__ == '__main__':
#     csv_2_pickles(Path('new_users.csv'))