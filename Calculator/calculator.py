def add(a,b):
    return(a + b)

def subtract(a,b):
    return(a - b)

def multiply(a,b):
    return(a * b)

def divide(a,b):
    return(a / b)

operations_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

number1 = int(input("Enter First number:"))
for symbol in operations_dict:
    print(symbol)
op_symbol = input("Pick an operation from the above symbols:")
number2 = int(input("Enter Second number:"))

calculator_function = operations_dict[op_symbol]
calculator_function(number1, number2)