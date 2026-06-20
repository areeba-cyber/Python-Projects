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