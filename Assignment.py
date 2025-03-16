def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Enter the operation (+, -, *, /, %, **, //,): ")
        if operation in ['+', '-', '*', '/', '%', '**', '//']:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /, %, **, //.")

def perform_operation(no1, no2, operation):
    if operation == '+':
        return no1 + no2
    elif operation == '-':
        return no1 - no2
    elif operation == '*':
        return no1 * no2
    elif operation == '/':
        if no2 != 0:
            return no1 / no2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        return no1 % no2
    elif operation == '**':
        return no1 ** no2
    elif operation == '//':
        return no1 // no2

def main():
    no1 = get_number("Enter the first number: ")
    no2 = get_number("Enter the second number: ")
    operation = get_operation()
    result = perform_operation(no1, no2, operation)
    print(f"The result of {no1} {operation} {no2} is: {result}")

if __name__ == "__main__":
    main()