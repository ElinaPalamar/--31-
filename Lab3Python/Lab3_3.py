sentence = input("Введіть речення: ")

words = sentence.split()
min_length = min(len(word) for word in words)

print("Довжина найкоротшого слова в реченні:", min_length)
