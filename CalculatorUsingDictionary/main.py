from art import logo
print(logo)

#Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    exit_flag = False
    
    num1 = float(input("Please enter a number: "))
    
    while not exit_flag:
        for symbol in operations:
            print(symbol, end = " ")
        operation_symbol = input("\nPick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        exit_value = input("Please type yes to continue or type no to ecit or start a new calculation: ").lower()
        if exit_value == "no":
            exit_flag = True
            calculator()
        else:
            num1 = answer

calculator()
