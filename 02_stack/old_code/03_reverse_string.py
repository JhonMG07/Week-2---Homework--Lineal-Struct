def reverse_string(string):
    stack = []
    for character in string:
        stack.append(character)

    reversed_string: str = ""
    while stack:  # mientras la pila esté llena
        reversed_string += stack.pop()
    return reversed_string


string: str = "Hola mundo!"

reverse_string: str = reverse_string(string)

print(reverse_string)  # imprime "!odnum aloH"

#explicacion, lo que hace nomas es sacar y poner los caracteres en un str