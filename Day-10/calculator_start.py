from art import logo


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    isContinue = True
    num1 = float(input('What is the first number? '))

    for o in operations:
        print(o)

    while isContinue:
        operation_symbol = input('Pick an operation: ')

        num2 = float(input('What is the next number? '))

        calculation = operations[operation_symbol]

        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to calculate with {answer} or 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            isContinue = False
            calculator()


calculator()
