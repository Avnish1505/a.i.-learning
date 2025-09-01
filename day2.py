12# Task 1: Even or Odd
def check_even_odd():
    print("-------- Task 1: Even or Odd --------")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
    print("\n")

# Task 2: Area of Circle
def calc_area_circle():
    print("-------- Task 2: Area of Circle --------")
    def calc_area(radius):
        return 3.14 * radius * radius

    r = float(input("Enter radius: "))
    area = calc_area(r)
    print("Area of circle is:", area)
    print("\n")

# Task 3: Table Printing
def print_table():
    print("-------- Task 3: Table Printing --------")
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print("\n")

# Task 4: Reverse Counting
def reverse_counting():
    print("-------- Task 4: Reverse Counting --------")
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("\n")

# Main function to call all tasks
def main():
    check_even_odd()
    calc_area_circle()
    print_table()
    reverse_counting()

# Start the program
main()
