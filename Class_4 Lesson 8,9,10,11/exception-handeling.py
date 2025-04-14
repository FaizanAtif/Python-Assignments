def divide_numbers():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except ValueError:
        return "Error: Please enter valid numbers!"
    else:
        return f"Result: {result}"
    finally:
        print("Calculation attempt completed.")

# Main execution
if __name__ == "__main__":
    print("Example 1: Normal division")
    print(divide_numbers())  # Try inputs like 10, 2