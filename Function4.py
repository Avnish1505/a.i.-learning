def greet(n=3):
    if n == 0:
        return
    print("hello, world!")
    greet(n - 1)