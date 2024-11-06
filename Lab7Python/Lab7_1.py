students_height = {
    "Петров": 180,
    "Огли": 175,
    "Гура": 190,
    "Штиря": 185,
    "Нестеренко": 178,
    "Павленко": 183,
    "Бакало": 182,
    "Шевченко": 175,
    "Бондарев": 177,
    "Василенко": 179
}

def display_all_students(data):
    for surname, height in data.items():
        print(f"{surname}: {height} см")

def add_student(data, surname, height):
    if surname in data:
        print(f"Помилка: учень з прізвищем {surname} вже існує.")
    else:
        data[surname] = height
        print(f"Учень {surname} доданий із зростом {height} см.")

def remove_student(data, surname):
    if surname in data:
        del data[surname]
        print(f"Учень {surname} видалений.")
    else:
        print(f"Помилка: учень з прізвищем {surname} не знайдений.")

def display_sorted_by_name(data):
    for surname in sorted(data.keys()):
        print(f"{surname}: {data[surname]} см")

def process_new_student(data, new_student_surname, new_student_height):
    shorter_students = [surname for surname, height in data.items() if height < new_student_height]

    sorted_heights = sorted(data.items(), key=lambda x: x[1], reverse=True)
    insert_position = None
    for i, (surname, height) in enumerate(sorted_heights):
        if height < new_student_height:
            insert_position = sorted_heights[i - 1][0] if i > 0 else sorted_heights[0][0]
            break

    closest_student = min(data.items(), key=lambda x: abs(x[1] - new_student_height))[0]

    print(f"\nУчні з меншим ростом, ніж у новенького ({new_student_height} см): {', '.join(shorter_students)}")
    print(f"Прізвище учня, після якого слід записати новенького: {insert_position}")
    print(f"Учень з найближчим зростом до новенького: {closest_student}")

def main():
    while True:
        print("\nМеню:")
        print("1 - Вивести всіх учнів")
        print("2 - Додати нового учня")
        print("3 - Видалити учня")
        print("4 - Вивести учнів за алфавітом")
        print("5 - Обробити новенького")
        print("6 - Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            display_all_students(students_height)

        elif choice == "2":
            surname = input("Введіть прізвище нового учня: ")
            try:
                height = int(input("Введіть зріст нового учня (см): "))
                add_student(students_height, surname, height)
            except ValueError:
                print("Помилка: введіть коректне числове значення для зросту.")

        elif choice == "3":
            surname = input("Введіть прізвище учня для видалення: ")
            remove_student(students_height, surname)

        elif choice == "4":
            display_sorted_by_name(students_height)

        elif choice == "5":
            new_student_surname = input("Введіть прізвище новенького: ")
            try:
                new_student_height = int(input("Введіть зріст новенького (см): "))
                process_new_student(students_height, new_student_surname, new_student_height)
            except ValueError:
                print("Помилка: введіть коректне числове значення для зросту.")

        elif choice == "6":
            print("Вихід з програми.")
            break

        else:
            print("Помилка: некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()

