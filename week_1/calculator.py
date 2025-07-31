# Function to perform calculation based on the operator
def calculate(num1, num2, operator):
    # Addition
    if operator == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    
    # Subtraction
    elif operator == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    
    # Multiplication
    elif operator == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    
    # Division (with zero check)
    elif operator == "/":
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "❌ Error: Division by zero is not allowed."
    
    # Modulus (with zero check)
    elif operator == "%":
        if num2 != 0:
            return f"{num1} % {num2} = {num1 % num2}"
        else:
            return "❌ Error: Modulus by zero is not allowed."
    
    # Exponentiation
    elif operator == "**":
        return f"{num1} ** {num2} = {num1 ** num2}"
    
    # Floor Division (with zero check)
    elif operator == "//":
        if num2 != 0:
            return f"{num1} // {num2} = {num1 // num2}"
        else:
            return "❌ Error: Floor division by zero is not allowed."
    
    # Handle invalid operator
    else:
        return "❌ Invalid operation. Please use +, -, *, /, %, **, or //."


# Main function to run the calculator program
def main():
    print("🔢 Welcome to my basic Python Calculator!")
    print("Available operators: +  -  *  /  %  **  //")
    
    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))
        
        # Get the operator (e.g. +, -, etc.)
        operator = input("Enter an operator: ").strip()
        
        # Get the second number from the user
        num2 = float(input("Enter the second number: "))
        
        # Display the expression first
        print(f"\n🧮 Expression: {num1} {operator} {num2}")
        
        # Perform the calculation and print the result
        result = calculate(num1, num2, operator)
        print("✅ Result:", result)

    except ValueError:
        # Handle non-numeric input
        print("❌ Error: Please enter valid numeric input.")
        
# Entry point: run the program
if __name__ == "__main__":
    main()
