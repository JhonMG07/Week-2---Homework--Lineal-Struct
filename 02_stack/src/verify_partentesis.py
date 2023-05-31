
def verify_parentheses(parenthesis: str):
    print(parenthesis)

    for char in parenthesis:
        if char.isdigit():  
            return None

        if char.isalpha():
            return None

    stack: list = []
    pairs: dict = {"(": ")", "[": "]", "{": "}"}

    for char in parenthesis:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack:
                return False

            last_opened = stack.pop()
            if pairs[last_opened] != char:
                return False

    return not stack

