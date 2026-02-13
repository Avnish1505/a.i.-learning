for i in range(5):
    print("i")

for i in range(1, 11):
    if i % 1 == 0:
        print(i)
num = int(input("Enter a number"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print("rev")
for i in range(1, 4):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
