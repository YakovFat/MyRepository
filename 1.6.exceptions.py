print('Через пробел введите операцию и два числа.\nИспользуйте только положительные числа')

try:
    a = input().split()
    assert int(a[1]) > 0 and int(a[2]) >= 0
    if a[0] == '+':
        print(int(a[1]) + int(a[2]))
    elif a[0] == '-':
        print(int(a[1]) - int(a[2]))
    elif a[0] == '*':
        print(int(a[1]) * int(a[2]))
    elif a[0] == '/':
        print(int(a[1]) / int(a[2]))
    else:
        print('Данная операция не поддерживается')
except ValueError:
    print('Введены некорректные данные')
except AssertionError:
    print('Вы ввели отрицательное значение')
except IndexError:
    print('Введены некорректные данные')
finally:
    print('Программа завершена')
