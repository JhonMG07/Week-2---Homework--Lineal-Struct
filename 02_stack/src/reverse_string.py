def reverse_string(string):
    stack = []
    for character in string:
        stack.append(character)

    reversed_string: str = ""
    while stack:  # mientras la pila esté llena
        reversed_string += stack.pop()

    return reversed_string



reverse_str: str = reverse_string("Hola mundo!")
print(reverse_str) 
