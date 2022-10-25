import pandas as pd
from glob import glob
import os
import webbrowser


def check_file_in_dir(name_file):
    # проверка на наличие введенного имени файла в директории
    if name_file + ".csv" not in list_csv_files():
        raise IOError("Такого файла нет в текущей директории!")


def list_csv_files():
    # функция возвращает список файлов .csv в текущей директории
    list_files = []
    for i in glob("*.csv"):
        list_files.append(str(i))
    return list_files


def print_all_files():
    print()
    # функция по пунктам выводит актуальные файлы
    for i in list_csv_files():
        print(f" - {i}")


def read_note():
    # функция выводит содержимое файла
    print("Введите название csv файла в локальной директории")
    print_all_files()

    name_file = input("\n>>> ")

    check_file_in_dir(name_file)

    print('\n', pd.read_csv(name_file + ".csv"))

    return name_file, pd.read_csv(name_file + ".csv",
                                  index_col=False,
                                  # usecols=[ "task_number",
                                  #           "task_body",
                                  #           "time",
                                  #           "date",
                                  #           "priority",
                                  #           "status" ]
                                  )


def create_new_note():
    # функция создает пустой файл с заданным именем
    df = pd.DataFrame({
                       "task_number": [],
                       "task_body": [],
                       "time": [],
                       "date": [],
                       "priority": [],
                       "status": []})

    print("Название создаваемого файла")
    df.to_csv(input("\n>>> ") + ".csv")

    print("\nОбновленный список актуальных файлов:")
    print_all_files()



def change_note():
    name_file, df = read_note()

    print("\nИзменить избранную запись блокнота или добавить в конец?")

    answer = input("\n>>> ")

    if (answer == "1") or (answer == "изменить"):
        print("\n• Jupyter notebook - среда разработки с локальным веб-сервером и удобными оконными окнами для программирования")
        print("• Numpy - библиотека для векторных вычислений и не только")
        print("• Pandas - библиотека для анализа данных")

        print('\nОткрыть ссылки для получения подробной информации?')
        answerlink = input("\n>>> ")
        if answerlink.lower() == "да":
            webbrowser.open("https://jupyter.org/")
            webbrowser.open("https://numpy.org/")
            webbrowser.open("https://pandas.pydata.org/")
        else:
            pass

    elif (answer == "2") or (answer == "добавить"):
        print("\nВведите через пробел значения полей")

        # print("Список атрибутов фактический:", *df.columns)

        task_body = input("Задача: ")
        time = input("Время: ")
        date = input("Дата: ")
        priority = input("Приоритет: ")
        status = input("Статус: ")

        df.loc[len(df.index)] = [str(df.shape[0]+1),task_body, time, date, priority, status]

        # print(df)

        df.to_csv(name_file + ".csv", index=False, index_label=["task_number",
                                                                    "task_body",
                                                                    "time",
                                                                    "date",
                                                                    "priority",
                                                                    "status"])
    else:
        print("Такого варианта не предусмотрено :(\n")



def delete_note():
    print("Введите название блокнота, который хотите удалить (введите имя файла без расширения)")
    print_all_files()

    name_file = input("\n>>> ")

    check_file_in_dir(name_file)

    print(f"\nВы точно желаете удалить файл '{name_file}.csv'? Этот файл будет невозможно восстановить!")
    answer = input("\n>>> ")

    if answer == "Да" or answer == "да":
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name_file}.csv')
        os.remove(path)
        print("\nОбновленный список актуальных файлов:")
        print_all_files()


def main():
    while True:
        os.system('clear')
        print("\nВыберете команду из списка:\n")
        print(" 1. Просмотреть содержимое блокнота")
        print(' 2. Создать новый блокнот')
        print(' 3. Изменить существующий блокнот')
        print(' 4. Посмотреть список существующих блокнотов')
        print(' 5. Удалить существующий блокнот')

        command = input("\n>>> ")

        if command == "1":
            os.system('clear')
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            read_note()
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        elif command == "2":
            os.system('clear')
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            create_new_note()
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        elif command == "3":
            os.system('clear')
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            change_note()
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        elif command == "4":
            os.system('clear')
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("Список актульных csv файлов")
            print_all_files()
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        elif command == "5":
            os.system('clear')
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            delete_note()
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")

        else:
            os.system('clear')
            print("Нет такого варианта")
            print("\nПродолжить?")
            check = input("\n>>> ")
            print()
            if check.lower() == "да" or check.lower() == "yes":
                continue
            elif check.lower() == "нет" or check.lower() == "no":
                os.system('clear')
                break
            else:
                raise IOError("Отсутсвие навыка чтения и (или) умения попадать пальцами по клавишам")



if __name__ == '__main__':
    main()