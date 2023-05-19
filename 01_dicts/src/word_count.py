# Read text and repeated word count
from collections import defaultdict

def read_file_and_word_count(file_name: str) -> dict:
    if(not (file_name.endswith(".txt"))):
       return None
        
    
    word_count: dict = defaultdict(int)
    
    file = open(file_name, "r")
    
    file = file.read().lower()

    words: list = file.split()
    print(f"Separadas: {words}")

    # create a bucle to read each line of the file
    for word in words:
        word_count[word] += 1

    return word_count

def sort_alphabetically(dict_words:dict) -> list:
    word_sorted:list = sorted(dict_words.keys())
    return word_sorted


word_counted: dict = read_file_and_word_count("./01_dicts/src/file.txt")

word_sorted: list = sort_alphabetically(word_counted)

print(f"la lista ordenada es: {word_sorted}")