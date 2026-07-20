import os
from ast import While



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
def Calculator():
  number1 = float(input("Enter First number:"))
  for symbol in operations_dict:
    print(symbol)

  continue_calculating = True
  while continue_calculating:  
   op_symbol = input("Pick an operation from the above symbols:")
   number2 = float(input("Enter Second number:"))
   calculator_function = operations_dict[op_symbol]
   output =calculator_function(number1, number2)
   print(f"{number1} {op_symbol} {number2} = {output}")

   Continue=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation or 'x' to exit.").lower()
   if Continue == "y":
     number1 = output
   elif Continue == "n":
        continue_calculating = False
        os.system('cls')
        Calculator()
        # print("Starting a new calculation...")
   else:
        continue_calculating = False
        print("Bye...")

Calculator()