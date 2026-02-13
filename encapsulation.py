# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance   

#     def deposit(self, amount):     
#         self.__balance += amount

#     def get_balance(self):         
#         return self.__balance      

# acc = BankAccount("Alice", 10000)
# acc.deposit(500)
# print(acc.get_balance())

# class Student:
#     def __init__(self, marks , name): # private variable 
#         self.__marks = marks
#         self.__name = name

#     def get_marks(self):
#         return self.__marks
    
# result = Student(85, "Avnish")
# print(result.get_marks())

# class Employee:
#     def __init__(self , name , salary): #private variable
#         self.name = name 
#         self.salary = salary 

#     def increase_salary(self):
#         self.salary = self.salary + (self.salary * 0.10)
#         return self.salary 

# em1 = Employee("Avnish", 50000)
# print("salary before increase:", em1.salary)
# print("salary after increase:", em1.increase_salary())

# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def price_change(self, new_price):
#         self.price = new_price

# mobile = Mobile("Apple", 100000)
# print("Brand:", mobile.brand)
# print("price:", mobile.price)
# mobile.price_change(90000)
# print("price after change:", mobile.price)


class Car:
    def __init__(self,speed):
        self.speed = speed
    
    def speed_change(self, new_speed):
        self.speed = new_speed

bmwm5doualturbo = Speed("bmw:",300)
print("bmw:", 300)
bwmm5doualturbo.speed(350)
print("speed after change:", 350)



    
