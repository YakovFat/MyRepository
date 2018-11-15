print('Используйте только положительные числа')

try:
    a = input().split()
    b = int(a[1])
    if a[0] == '+':
        print(int(a[1]) + int(a[2]))
    elif a[0] == '-':
        print(int(a[1]) - int(a[2]))
    elif a[0] == '*':
        print(int(a[1]) * int(a[2]))
    elif a[0] == '/':
        print(int(a[1]) / int(a[2]))

except ValueError:
    print("Введены некорректные данные")

# assert int(a[1]) > 0 or int(a[2]) > 0, 'Вы ввели отрицательное знначение'


# if a[0] == '+':
#     print(int(a[1])+int(a[2]))
# elif a[0] == '-':
#     print(int(a[1])-int(a[2]))
# elif a[0] == '*':
#     print(int(a[1])*int(a[2]))
# elif a[0] == '/':
#     print(int(a[1])/int(a[2]))

