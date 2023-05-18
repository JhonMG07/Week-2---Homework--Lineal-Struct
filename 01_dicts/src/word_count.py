# Read text and repeated word count
from collections import defaultdict

# funcion para leer el archivo y retornar una lista de las palabras


def read_file_and_word_count(file_name: str) -> dict:
    if(not (file_name.endswith(".txt"))):
       return None
        
    # Creamos un diccionario vacio
    word_count: dict = defaultdict(int)
    # Creamos un archivo y abrimos el archivo
    file = open(file_name, "r")
    # Convertir todo a un mismo tipo
    file = file.read().lower()

    words: list = file.split()
    print(f"Separadas: {words}")

    # Creamos un bucle para leer cada linea del archivo
    for word in words:
        word_count[word] += 1

    print(f"Palabra y frecuencia: {word_count.items()}")

    return word_count

def sort_alphabetically(dict_words:dict) -> list:
    word_sorted:list = sorted(dict_words.keys())
    return word_sorted


word_counted: dict = read_file_and_word_count("./01_dicts/src/file.txt")

word_sorted: list = sort_alphabetically(word_counted)

print(f"la lista ordenada es: {word_sorted}")