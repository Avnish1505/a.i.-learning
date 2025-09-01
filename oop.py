class student:
    def ___int___ (self , name, roll):
        self.name = name 
        self.roll = roll

    def display(self):
        print("Name: {self.name}, Roll: {self.roll}" )

s1 = student("Avnish", 1230432230)
s1.display()