def evaluate_posfixed_expression(expression):
    stack = []
    # lambda is used for simple functions lambda args: expression
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for element in expression:  # iterate through each symbol in the expression
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[element](operand1, operand2)
            stack.append(round(result, 2))
    return stack.pop()






