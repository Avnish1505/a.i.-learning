try: 
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print("An unexpected error occurred:", e)