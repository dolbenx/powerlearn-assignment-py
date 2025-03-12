def calculator():
    first_number = float(input("Enter the first number: "))
    sec_number = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    
    if operation == '+':
        result = first_number + sec_number
        print(f"{first_number} + {sec_number} = {result}")
    elif operation == '-':
        result = first_number - sec_number
        print(f"{first_number} - {sec_number} = {result}")
    elif operation == '*':
        result = first_number * sec_number
        print(f"{first_number} * {sec_number} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = first_number / sec_number
            print(f"{first_number} / {sec_number} = {result}")
    else:
        print("Wrong Operation. Please enter +, -, *, or /.")

calculator()