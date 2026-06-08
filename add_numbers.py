def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

if __name__ == "__main__":
    # Get input from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Calculate sum
        result = add_numbers(num1, num2)
        
        # Display result
        print(f"\n{num1} + {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
