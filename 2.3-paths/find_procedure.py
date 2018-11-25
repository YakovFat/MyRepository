# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    list_sql = []
    list_user = []
    list_user_2 = []
    for file in os.listdir(migrations):
        if file.endswith('.sql'):
            abs_file_path = os.path.join(migrations, file)
            list_sql.append(abs_file_path)

    print('Введите строку:')
    line_user = input()

    for list_file in list_sql:
        f = open(list_file)
        files = f.read()
        if line_user in files:
            print(list_file)
            list_user.append(list_file)
        f.close()
    print(len(list_user))

    while True:
        print('Введите строку:')
        line_user = input()

        for list_file in list_user:
            f = open(list_file)
            files = f.read()
            if line_user in files:
                print(list_file)
                list_user_2.append(list_file)
            f.close()
        print(len(list_user_2))





