# Explicacion:
# Si en el caracter entrante esta en las "keys" = abierto
# entonces lo guardamos en la pila.

# Avanzamos y cogemos el otro caracter y si este esta en "values"
# preguntamos si la pila está vacia (dado que si esta vacia, no
# está balanceada), si esto no es cierto cogemos el ultimo "key"
# que será el key de un parentesis abierto y si no es igual al value
# correspondiente, entonces no estará balanceado


def verify_parentheses(string):
    print(string)
    stack: list = []
    if not stack:
        print("Empty")

    pairs: dict = {"(": ")", "[": "]", "{": "}"}

    for char in string:
        if char in pairs.keys():
            stack.append(char)
            print(f"Was added to the stack:{char}")
        elif char in pairs.values():
            if not stack:
                print("Empty")
                return False

            last_opened = stack.pop()
            print(f"Was deled to the stack:{char}")
            if pairs[last_opened] != char:
                print(f"Don't mach: {pairs[last_opened]} =! {char}")
                return False

    return not stack


res: bool = verify_parentheses("[{()}]")

if res:
    print("Yes")
else:
    print("No")

print("\n----\n")

res = verify_parentheses("[{({}}]")

if res:
    print("Yes")
else:
    print("No")
