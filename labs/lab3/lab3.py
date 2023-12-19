import os
import random


def print_char_list(array):
    for i in range(len(array)):
        print(array[i])


def task1():
    n = int(input("Введите длину массива "))
    array = ['a'] * n
    for i in range(n):
        input_value = str(input("Введите элемент массива "))
        if len(input_value) > 1:
            input_value = input_value[:1]
        array[i] = input_value
    print_char_list(array)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        for i in range(n):
            if int(array[i]) in numbers:
                array[i] = "*"
    except:
        pass
    print("\n")
    print_char_list(array)


def task3():
    file_path = "text.txt"
    input_value = str(input("Введите текст:\n"))
    with open(file_path, "w") as file:
        file.write(input_value)


def print_string_list(array):
    for word in array:
        print(word)


def random_choise(array):
    return random.choice(array)


def task4():
    physical_terms = [
        "Температура",
        "Энергия",
        "Скорость",
        "Масса",
        "Сила",
        "Давление",
        "Электричество",
        "Магнитизм",
        "Импульс",
        "Относительность",
        "Частота",
        "Сопротивление"
    ]
    print_string_list(physical_terms)
    while True:
        choice = random_choise(physical_terms)
        input_value = str(input("Для получания случайного элемента массива нажмите Enter: "))
        if input_value == "":
            print(choice)
        else:
            break


def task5():
    file_path = "task1.out"
    input_value = str(input("Введите текст:\n"))
    with open(file_path, "w") as file:
        file.write(input_value)


def task7():
    file_path = "directory.txt"

    with open(file_path, "r") as file:
        paths = [line.strip() for line in file.readlines()]

    for path in paths:
        folder = os.path.split(path)[0]
        file_name = os.path.split(path)[1]
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(path, "w") as new_file:
            new_file.write(f"Contens of {file_name}")

    print("Файловая структура успешно создана.")


if __name__ == "__main__":
    # array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print_char_2d_array(array)
    task7()