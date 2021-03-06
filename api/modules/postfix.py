from itertools import zip_longest

OPERATORS_PRIORITY = {
    '+': 1, '-': 2, '*': 3, '/': 4
}
OPEN_PARENTHESIS = '('
CLOSE_PARENTHESIS = ')'


def create_expression(*symbols) -> str:
    expression = ''
    for symbol, next_symbol in zip_longest(symbols, symbols[1:], fillvalue=''):
        expression += symbol
        if not (symbol.isdigit() and next_symbol.isdigit()):
            expression += ' '

    return expression.strip()


def crete_space_between_symbols(infix: str) -> str:
    symbols = list(infix.strip())
    spaced_infix = ''

    for symbol, next_symbol in zip_longest(symbols, symbols[1:], fillvalue=''):
        spaced_infix += symbol
        if not (symbol.isdigit() and next_symbol.isdigit()):
            spaced_infix += ' '

    return spaced_infix.strip()


def to_postfix(infix: str) -> str:
    infix_queue = infix.split()
    postfix_queue = []
    operator_stack = []

    while infix_queue:
        symbol = infix_queue.pop(0)
        if symbol.isalnum():
            postfix_queue.append(symbol)
        elif symbol == OPEN_PARENTHESIS:
            operator_stack.append(symbol)
        elif symbol == CLOSE_PARENTHESIS:
            while operator_stack[-1] != OPEN_PARENTHESIS:
                postfix_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and operator_stack[-1] != OPEN_PARENTHESIS and OPERATORS_PRIORITY[operator_stack[-1]] >= OPERATORS_PRIORITY[symbol]:
                postfix_queue.append(operator_stack.pop())
            operator_stack.append(symbol)

    while operator_stack:
        postfix_queue.append(operator_stack.pop())

    return ' '.join(postfix_queue)


def evaluate(postfix: str) -> int:
    postfix_queue = postfix.split()
    symbols_stack = []

    while postfix_queue:
        symbol = postfix_queue.pop(0)
        if symbol.isdigit():
            symbols_stack.append(symbol)
        else:
            operand_1 = symbols_stack.pop()
            operand_2 = symbols_stack.pop()
            result = operation(int(operand_2), int(operand_1), symbol)
            symbols_stack.append(result)
    return symbols_stack.pop()


def operation(operand_1: int, operand_2: int, operator: str) -> int:
    return eval(f"{operand_1} {operator} {operand_2}")
