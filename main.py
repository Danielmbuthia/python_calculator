from replit import clear
from art import logo
#calculator 

#add 
def add(n1,n2):
    return n1 + n2

# Substract 
def subtract(n1,n2):
    return n1 - n2

# multiply
def multiply(n1,n2):
    return n1 * n2
    
# divide
def divide(n1,n2):
    return n1 / n2

operations = {}
operations['+'] = add
operations['-'] = subtract
operations['*'] = multiply
operations['/'] = divide

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for key in operations:
            print(key)
        
    continue_calculation = True
    while continue_calculation:
        operation = input("Select one of the operation above: ")
        num2 = float(input("What's the next number? "))
    
        my_function  = operations[operation]
        
        answer = my_function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
    
        continue_with = input(f"Type 'Y' to continue calculating with {answer}, or 'n' to start a new caclulation: ")
        if continue_with.lower() == 'y':
            num1 =answer
        else:
            continue_calculation =False
            clear()
            calculator() #recursion --- a function calling itself 

calculator()
        

    

