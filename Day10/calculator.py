

# Add function
def add(n1, n2):
    return n1 + n2

# Subtraction function 
def sub(n1, n2):
    return n1 - n2

# Multiply function 
def multiply(n1, n2):
    return n1 * n2

# Divide function 
def divide(n1, n2):
    return n1 / n2


# calulator ditionary 
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

def calulator():
    print("Welcome to calculator app")
    num1 = float(input("what's the first number?: "))
    for operator in operations:
        print(operator)

    run_calculation = False
    while not run_calculation:
        picked_operator = input("pick an operation: ")
        num2 = float(input("what's the next number?: "))
        cal_function = operations[picked_operator]
        answer = cal_function(num1, num2)

        print(f"{num1} {picked_operator} {num2} = {answer}")
        
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if again == 'y':
            num1 = answer
        else:
            run_calculation = True
            calulator()

calulator()
