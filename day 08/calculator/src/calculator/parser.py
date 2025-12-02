import re

def tokenize(expression):
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string.")

    if not expression.strip():
        return []

    token_patterns = {
        'NUMBER': r'\d+\.?\d*',
        'OPERATOR': r'[+\-*/]',
        'PARENTHESIS': r'[()]'
    }

    tokens = []
    i = 0
    while i < len(expression):
        match = None
        for token_type, pattern in token_patterns.items():
            regex = re.compile(pattern)
            m = regex.match(expression, i)
            if m:
                tokens.append(m.group(0))
                i = m.end()
                match = True
                break
        if not match:
            if expression[i].isspace():
                i += 1
            else:
                raise ValueError(f"Invalid character: {expression[i]}")
    return tokens

def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    if not tokens:
        return []

    for token in tokens:
        if re.fullmatch(r'\d+\.?\d*', token):
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Mismatched parentheses")
            operator_stack.pop()  # Pop '('
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            # This case should ideally be caught by tokenize, but for robustness:
            raise ValueError(f"Invalid token encountered during postfix conversion: {token}")

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(operator_stack.pop())

    # Basic validation for missing operands/operators
    # This is a simple check; more robust validation would be in evaluator
    if not output:
        return []

    operand_count = 0
    operator_count = 0
    for token in output:
        if re.fullmatch(r'\d+\.?\d*', token):
            operand_count += 1
        elif token in precedence:
            operator_count += 1

    if operand_count - operator_count != 1 and not (operand_count == 0 and operator_count == 0):
        raise ValueError("Invalid expression: missing operand or operator")

    return output
