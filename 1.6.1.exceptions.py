documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def information_number():
    print("Введите номер документа: ")
    number = input()
    for information in documents:
        if information["number"] == number:
            print("Имя владельца документа:", information["name"])
    print("Введены некорректные данные")


def information_list():
    print("Данные документов:")
    for information in documents:
        print(information["type"], information["number"], information["name"])


def information_shelf():
    print("Введите номер документа: ")
    number_1 = input()
    for information, i in directories.items():
        if number_1 in i:
            print("Номер полки:", information)
    print("Введены некорректные данные")


def information_add():
    doc = {"type": None, "number": None, "name": None}
    print("Введите тип документа:")
    doc["type"] = input()
    print("Введите номер документа:")
    doc["number"] = input()
    print("Введите имя владельца документа:")
    doc["name"] = input()
    documents.append(doc)
    print("Введите номер полки:")
    number_1 = input()
    for i in directories:
        if number_1 == directories[i]:
            directories[number_1].append(doc["number"])
    print("Извините, полка отсутствует")


def information_name():
    try:
        print("Имена всех владельцев документов:")
        for information in documents:
            print(information["name"])
    except KeyError:
        print("Отсутствует поле 'name'")


print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n'
      'l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n'
      's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n'
      'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, '
      'тип,имя владельца и номер полки, на котором он будет храниться;\n'
      'n – name – команда, которая выведет имена всех владельцев документов.\n\n'
      'Введите одну из вышеперечисленных команд:')

comand = input()
if comand == "p":
    information_number()
elif comand == "l":
    information_list()
elif comand == "s":
    information_shelf()
elif comand == "a":
    information_add()
elif comand == "n":
    information_name()
