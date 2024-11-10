import json

input_file = "students_data.json"
output_file = "height_comparison.json"

initial_data = [
    {"name": "Anna", "height": 160, "gender": "female"},
    {"name": "Maria", "height": 158, "gender": "female"},
    {"name": "Ivan", "height": 175, "gender": "male"},
    {"name": "Oleg", "height": 170, "gender": "male"},
    {"name": "Danylo", "height": 165, "gender": "male"},
    {"name": "Sofia", "height": 162, "gender": "female"},
    {"name": "Andriy", "height": 178, "gender": "male"},
    {"name": "Olena", "height": 159, "gender": "female"},
    {"name": "Max", "height": 180, "gender": "male"},
    {"name": "Viktoria", "height": 161, "gender": "female"}
]

def initialize_file(): #Щоб записати вихідні дані у файл
    try:
        with open(input_file, "w") as file:
            json.dump(initial_data, file, indent=4)
        print(f"Initial data written to {input_file}")
    except Exception as e:
        print(f"Error initializing file: {e}")

def load_data():
    try:
        with open(input_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{input_file} not found, initializing with default data.")
        initialize_file()
        return initial_data
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def save_data(data):
    try:
        with open(input_file, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def display_data():
    data = load_data()
    print("Поточна інформація про студента:")
    for record in data:
        print(record)

def add_record():
    data = load_data()
    name = input("Введіть ім'я студента: ")
    height = int(input("Введіть зріст: "))
    gender = input("Введіть гендер (male/female): ")
    data.append({"name": name, "height": height, "gender": gender})
    save_data(data)
    print("Запис додано успішно!")

def delete_record():
    data = load_data()
    name = input("Введіть ім'я студента, якого хочете видалити: ")
    data = [record for record in data if record['name'] != name]
    save_data(data)
    print(f"Запис для {name} успішно видалений.")

def search_by_field():
    data = load_data()
    field = input("Введіть поле, за яким здійснювати пошук (name/height/gender): ")
    value = input("Введіть значення за яким шукати: ")
    if field == "height":
        value = int(value)
    results = [record for record in data if record.get(field) == value]
    print("Пошук результатів:")
    for record in results:
        print(record)

def compare_heights():
    data = load_data()
    total_female_height = sum(record['height'] for record in data if record['gender'] == 'female')
    total_male_height = sum(record['height'] for record in data if record['gender'] == 'male')

    comparison_result = {
        "total_female_height": total_female_height,
        "total_male_height": total_male_height,
        "female_height_greater": total_female_height > total_male_height
    }

    with open(output_file, 'w') as file:
        json.dump(comparison_result, file, indent=4)

    print("Порівняння зросту збережено до", output_file)

def main():
    while True:
        print("\nВиберіть опцію:")
        print("1. Показати контент файлу JSON")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Шукати за полем")
        print("5. Порівняти загалом зріст дівчаток і хлопчиків")
        print("6. Exit")

        choice = input("Введіть число меню (1-6): ")

        if choice == '1':
            display_data()
        elif choice == '2':
            add_record()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            search_by_field()
        elif choice == '5':
            compare_heights()
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Некоректне значення. Спробуйте ще раз")

if __name__ == "__main__":
    main()