# Theory

"""
"Poly" = many, "morphism" = forms → matlab ek cheez ke multiple forms.
Python me polymorphism ka matlab hai ek function/method/class ka different behavior different situation me.

Polymorphism ke do main types hain:
Compile-time polymorphism (Method Overloading — Python me limited support)
Run-time polymorphism (Method Overriding — Python me fully supported)
"""
"""
Method Overriding (Run-time Polymorphism)
Jab child class parent class ke method ko same naam ke saath redefine karta hai, to wo method overriding hota hai.
"""
class car():
    def Top_Speed(self):
        print("General speed  150kmphr")

class racing_car(car):
    def Top_Speed(self):
        print("Have no limits,220kmphr-300")


class business_car(car):
    def Top_Speed(self):
        print("150-200 kmph")



#---------------------- Lets Test ----------------
# assinging object to different classes

ciaz=business_car()
ciaz.Top_Speed()

GT_Mustang=racing_car()
GT_Mustang.Top_Speed()


Ambasador=car()
Ambasador.Top_Speed()

# same methods when call for different object gave different results

"""
Method Overloading (Compile-time Polymorphism)
Python me true method overloading nahi hota, lekin hum default arguments ya *args/**kwargs se achieve kar sakte hain.
"""


print("------------------Practice--------------")

print("Problem1")

class shape():

    def area(self):
        print("area")


class Circle(shape):

    def area(self):
        print("area of circle")

class Rectangle(shape):

    def area(self):
        print("area of Rectangle")


class Triangle(shape):

    def area(self):
        print("area of Triangle")




cls_list = [shape(),Circle(),Rectangle(),Triangle()]


for i in cls_list:
    (i.area())

print("---------------Problem 2---------------")

class Employee():

    def get_salary(self):
        print(f"sallry: ")


class Manager(Employee):

    def get_salary(self):
        print(f"salary of manager ")

class Developer(Employee):

    def get_salary(self):
        print(f"salary of Developer")

class Intern(Employee):

    def get_salary(self):
        print(f"salary of Intern")


employee_list =[Employee(),Manager(),Developer(),Intern()]

for i in employee_list:
    i.get_salary()


print("----------------Problem3-----------")

class Payment():
    def __init__(self,amount):
        self.amount=amount


    def process_payment(self,amount):
        print(f"Payment Processed with amount: {self.amount}")

class CreditCardPayment(Payment):
    def __init__(self,amount):
        Payment.__init__(self,amount)
        self.amount=amount

    def process_payment(self,amount):
        print(f"payment Processed via CreditCard of ammount: {self.amount}")

class PayPalPayment(Payment):
    def __init__(self,amount):
        Payment.__init__(self,amount)
        self.amount=amount

    def process_payment(self, amount):
        print(f"payment Processed via Paypal of ammount: {self.amount}")


class UPIPayment(Payment):
    def __init__(self,amount):
        Payment.__init__(self, amount)

    def process_payment(self, amount):
        print(f"payment Processed via UPI of ammount: {self.amount}")



Payment_mathod_list=[Payment(500),CreditCardPayment(1000),PayPalPayment(7500),UPIPayment(100000)]

for i in Payment_mathod_list:
    i.process_payment(40)