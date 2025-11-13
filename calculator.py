def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def calculator():
    while True:
        operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ")
        
        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please try again.")
            continue
        
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        
        if operation == '+':
            result = add(x, y)
        elif operation == '-':
            result = sub(x, y)
        elif operation == '*':
            result = mul(x, y)
        elif operation == '/':
            result = div(x, y)
        
        print(f"Result: {result}")

calculator()
