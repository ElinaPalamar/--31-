def find_word_in_list(word_list, word_to_find):
    if word_to_find in word_list:
        print(f"Слово '{word_to_find}' знайдено у списку!")
    else:
        print(f"Слово '{word_to_find}' не знайдено у списку.")

user_input = input("Введіть список слів, розділених пробілом: ")
word_list = user_input.split()

word_to_find = input("Введіть слово для пошуку: ")

find_word_in_list(word_list, word_to_find)