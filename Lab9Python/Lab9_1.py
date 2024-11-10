import os

def create_tf12_1():
    try:
        with open("TF12_1.txt", 'w') as file:
            lines = [
                "Це буде перший рядок",
                "Це типу другий",
                "Ще один рядок",
                "Цей рядок найбільший і найбільше символів",
                "Короткий рядок",
                "Рядок середньої довжини.",
                "Рядок з різними словами?",
                "Типу ще якийсь там рядочок",
                "Взагалі-то останній рядок у файлі."
            ]
            file.write('\n'.join(lines))
        print("Файл TF12_1.txt створено і заповнено.")
    except Exception as e:
        print("Помилка при створенні файлу TF12_1.txt :", e)

def process_and_create_tf12_2():
    try:
        with open('TF12_1.txt', "r") as source_file:
            content = source_file.read().replace("\n", "")

        with open("TF12_2.txt", "w") as target_file:
            line_length = 1
            index = 0
            while index < len(content):
                target_file.write(content[index: index + line_length] + "\n")
                index += line_length
                line_length = line_length + 1 if line_length < 10 else 1
        print("Файл TF12_2.txt створено і заповнено умовою.")
    except FileNotFoundError:
        print("Помилка: файл TF12_1.txt не знайдено")
    except Exception as e:
        print("Помилка при обробці файлів:", e)

def display_tf12_2():
    try:
        with open("TF12_2.txt", "r") as file:
            print("Вміст файлу TF12_2.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Помилка: файл TF12_2.txt не знайдено.")
    except Exception as e:
        print("Помилка при читанні файлу TF12_2.txt", e)

def main():
    create_tf12_1()
    process_and_create_tf12_2()
    display_tf12_2()

if __name__ == "__main__":
    main()
