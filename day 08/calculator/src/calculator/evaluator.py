def evaluate_postfix(postfix_tokens):
    if not postfix_tokens:
        raise ValueError("Invalid postfix expression: cannot evaluate empty expression")

    operand_stack = []

    for token in postfix_tokens:
        if token.replace('.', '', 1).isdigit():  # Checks if it's a number (int or float)
            operand_stack.append(float(token))
        elif token in ['+', '-', '*', '/']:
            if len(operand_stack) < 2:
                raise ValueError("Invalid postfix expression: missing operand")
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            operand_stack.append(result)
        else:
            raise ValueError(f"Invalid token in postfix expression: {token}")

    if len(operand_stack) != 1:
        raise ValueError("Invalid postfix expression: too many operands")

    return operand_stack[0]
