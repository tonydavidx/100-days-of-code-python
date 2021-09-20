
def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input('What is the first number? '))

for o in operations:
    print(o)

operation_symbol = input('Pick an operation from the line above: ')    

num2 = int(input('What is the second number? '))


calculation = operations[operation_symbol]

answer = calculation(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")