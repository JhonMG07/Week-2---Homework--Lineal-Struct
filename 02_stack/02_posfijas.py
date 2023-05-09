def evaluar_expresion_posfija(expresion):
    stack = []
    operadores = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b,
                  '/': lambda a, b: a / b}

    for elemento in expresion: #recorre el elemento sumbolo por simbolo
        if elemento.isdigit():
            stack.append(int(elemento))
            print(f"Add number: {elemento}")
        else:
            operando2 = stack.pop()
            print(f"N2: {operando2}")

            operando1 = stack.pop()
            print(f"N1: {operando1}")

            print(f"Simbol: {elemento}")

            resultado = operadores[elemento](operando1, operando2)
            print(f"SubTotal: {resultado}")
            stack.append(resultado)
            
        print(f"Stack{stack}\n")
    return stack.pop()

# landa nos sirve cuando tenemos funciones simples lambda args: expresión

expresion = "53+82-/"
resultado = evaluar_expresion_posfija(expresion)
print(f"Reply: {resultado}")