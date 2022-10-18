def lab1():

    foot_dict = {"Россия": "A",
                 "Португалия": "B",
                 "Франция": "C",
                 "Дания": "C",
                 "Египет": "A"}

    print("Заданный словарь:", foot_dict)

    print("\nДобавить ключ Турция со значением B")
    foot_dict["Турция"] = "B"
    print("Результат:", foot_dict)

    print("\nТеперь найдем все страны по группе.\nВведите необходимую группу:")
    mal = input(">>> ")

    count_teams_on_group = {}

    for key, value in foot_dict.items():
        if mal == value:
            print(key, end=" ")

        if value in count_teams_on_group.keys():
            count_teams_on_group[value] += 1
        else:
            count_teams_on_group[value] = 1

    print("\n\nНу и количество команд по группам\n", count_teams_on_group)



def lab2(word):
    table = {
        1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z'],
    }

    score = 0

    for char_key, char_value in {i: word.count(i) for i in word}.items():
        for table_key, table_value in table.items():
            if char_key.upper() in table_value:
                score += table_key * char_value
    print("\nИтоговый балл:", score)




def main():

    while True:

        print("\nКакую лабу из 3х вывести?")
        answer = int(input(">>> "))

        if answer == 1:
            print("Задание 1")
            print("\n-----------------------------------\nРешение:\n")
            lab1()
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        if answer == 2:
            print("Задание 2")
            print("\n-----------------------------------\nРешение:\n")
            print("\nВведите слово:")
            lab2(list(input(">>> ")))
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        if answer == 3:
            print("Задание 3")
            print("\n-----------------------------------\nРешение:\n")
            lab3()
            print("\n-----------------------------------\n")

            print("\nПродолжить? Да/Нет")
            check = input(">>> ")
            print()
            if check == "Да" or check == "да":
                continue
            elif check == "Нет" or check == "нет":
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")


if __name__ == '__main__':
    main()

