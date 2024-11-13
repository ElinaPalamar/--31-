import nltk
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

try:
    with open('chesterton-ball.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

def count_words(text):
    sentences = nltk.sent_tokenize(text)
    k_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    return k_words

# Функція для побудови діаграми частоти
def plot_most_used_words(text, title):
    words = text.split()
    cnt = Counter(words)
    cort = cnt.most_common(10)
    x = [cort[el][0] for el in range(len(cort))]
    y = [cort[el][1] for el in range(len(cort))]
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

# Оригінальна діаграма
print(f"Кількість слів до очищення: {count_words(text)}")
plot_most_used_words(text, "10 найбільш вживаних слів (оригінальний текст)")

# Видалення стоп-слів і пунктуації
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return ' '.join(words)

cleaned_text = clean_text(text)

# Діаграма після очищення
print(f"Кількість слів після очищення: {count_words(cleaned_text)}")
plot_most_used_words(cleaned_text, "10 найбільш вживаних слів (після очищення)")
