import os
import time

directory_path = '/Users/ilnik94/Documents/Питон/Urban/urban'
for root, dirs, files in os.walk(directory_path):
    print(f'Текущая директория: {root}')
    print(f'Поддиректории: {dirs}')
    print(f'Файлы: {files}')

    for file in files:
        filepath = os.path.join(root, file)

        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        filesize = os.path.getsize(filepath)

        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
