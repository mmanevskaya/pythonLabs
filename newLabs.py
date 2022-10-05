import numpy as np



def lab1(words):

    my_list = [len(i) for i in words]

    result = max(my_list) + min(my_list)

    print(f"Список длин значений входного списка {my_list}\n Сумма min и max значений равна {result}")


def lab2(numbers):

    print("Минимальное:", min(numbers), "\nМаксимальное:", max(numbers))

    numbers = [i * min(numbers) if i % 2 == 0 else i * max(numbers) for i in numbers]

    print("Измененный список:", numbers)


def lab3(n_min, n_max, n):

    left = -10
    right = 10

    print(f"Заданный диапазон по условию [{left}, {right}]\n")

    lst_random = [np.random.uniform(left, right) for i in range(n)]

    print(f"Полученный список методом uniform: {lst_random}\n")

    print("Количество значений, совпавших с условием:", sum([True if n_min < j < n_max else False for j in lst_random]))


def lab4(lst_numbers):

    if len(lst_numbers) < 4:
        raise IOError("Вы ввели меньше 4х символов ;((")

    lst_no_extremum = [i for i in lst_numbers if i != max(lst_numbers) and i != min(lst_numbers)]

    print("До:\t\t", lst_numbers)
    print("После:\t", lst_no_extremum)

    # с исключенными из него наибольшими и наименьшими значениями => их может быть несколько :P

def lab5(count_sailors):

    lst = {}
    iter = 1

    print("Введите через пробел имя и возраст матроса:")
    for person in range(count_sailors):
        name, age = map(str, input(f"{iter}ый: ").split())
        lst[name] = int(age)
        iter += 1

    print()

    first_group = []
    second_group = []

    for name, age in lst.items():
        if 20 < age < 40:
            first_group.append(name)
        else:
            second_group.append(name)

    first_group.sort()
    second_group.sort()

    print("Команда 1:", *first_group)
    print("Команда 2:",*second_group)



def input_int():
    print("Введите через пробел список чисел:")
    lst = list(map(int, input('>>> ').split()))
    print()
    return lst

def input_str():
    print("Введите через пробел список строк:")
    lst = list(map(str, input('>>> ').split()))
    print()
    return lst

def main():

    while True:

        print("\nКакую лабу из 5и вывести?")
        answer = int(input(">>> "))

        if answer == 1:
            print("\nНа вход дан список слов.\nНужно:\n\t- Создать новый список с длинами слов заданного списка\n\t- Переменной result присвоить сумму минимального и максимального элементна нового списка")
            #print(f"\nЗаданный список:{words}")
            print("\n-----------------------------------\nРешение:\n")
            lab1(input_str())
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения")

        elif answer == 2:

            print("\nНа вход подается список чисел.\n Нужно:\n\t- Вывести минимальное значение\n\t- Вывести максимальное значение\n\t- Вывести измененный список по правилу")
            #print(f"\nЗаданный список:{numbers}")
            print("\n-----------------------------------\nРешение:\n")
            lab2(input_int())
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения")


        elif answer == 3:

            print("\nНа вход дается диапазон чисел для проверки диапазона рандомно-сгенерированного списка чисел так же заданной длины.\nНужно:\n\t- Вывести количество совпадений по заданному диапазону")

            print("\nВведите минимальное и максимальное значение через пробел:")
            n_min, n_max = map(float, input('>>> ').split())

            print("\nВведите количество элементов списка:")
            n = int(input(">>> "))

            print("\n-----------------------------------\nРешение:\n")
            lab3(float(n_min), float(n_max), n)
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения")

        elif answer == 4:
            print("На вход дается список чисел, количество которых должно быть больше 3.\nНужно:\n\t- Проверить количество элементов в списке\n\t- Исключить экстремумы")

            print("\n-----------------------------------\nРешение:\n")
            lab4(input_int())
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения ")

        elif answer == 5:

            print("Введите количество моряков:")
            count_sailors = int(input(">>> "))

            print("\n-----------------------------------\nРешение:\n")
            lab5(count_sailors)
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения ")

        else:
            print("\nТакой лабы нет :(")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения ")

if __name__ == '__main__':
    main()
    
