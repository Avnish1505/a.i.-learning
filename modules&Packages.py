def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\nMenu:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("result:", add(x, y))
    elif choice == '2':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("result:", subtract(x, y))
    elif choice == '3':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("result:", multiply(x, y))
    elif choice == '4':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("result:", divide(x, y))
    elif choice == '5':
        print("exit")
        break
    else:
        print("invalid input")