# Read text and repeated word count
from collections import defaultdict

# 1. Read the text and save it

file: str = open("./01_dicts/file.txt", "r")

# 2. we convert everything to the same type

file = file.read().lower()

print(f"Frase: {file}")

# 3. we split the text into words

words: list = file.split()

print(f"Separadas: {words}")

# 4. we count the number of repeated words
# create a empy dict

word_count: dict = defaultdict(int)  # word_count= {key: int}

for word in words:  # recorre la lista
    word_count[word] += 1  # aumenta 1 y añade al dict

print(f"Palabra y frecuencia: {word_count.items()}")

# 5. sort alphabetically

word_sorted: list = sorted(word_count.keys())

print(f"Palabra y frecuencia ordenada:")

for word in word_sorted:  # recorre la lista ordenada
    print(f"{word}: {word_count[word]}")  # imprime la key y el value de la key
