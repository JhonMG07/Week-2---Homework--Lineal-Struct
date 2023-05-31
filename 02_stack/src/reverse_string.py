def reverse_string(string):
    stack = []
    for character in string:
        stack.append(character)

    reversed_string: str = ""
    while stack:  # while the stack is not empty
        reversed_string += stack.pop()

    return reversed_string

