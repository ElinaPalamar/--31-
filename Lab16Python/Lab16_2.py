import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer("english")

stop_words = set(stopwords.words('english'))

processed_tokens = []
for token in tokens:
    if token.lower() not in stop_words and token not in string.punctuation:
        lemmatized_token = lemmatizer.lemmatize(token)
        stemmed_token = stemmer.stem(lemmatized_token)
        processed_tokens.append(stemmed_token)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(processed_tokens))

print("Обробка завершена. Перевірте файл 'output.txt'.")
