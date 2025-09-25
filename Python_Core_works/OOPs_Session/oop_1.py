"""Class is blurprint of Program, And Object is the instance of class """


class Dog:
    Species="Animal"

    def Bark(self):
        print("Woof")

Huskie=Dog()

Huskie.Bark()

###################
# lets implement Constructor
print("________________________________________________________________")


class Car:
    item = "Luxury"   # class variable

    def __init__(self, brand, colour,**kwargs):   # constructor
        self.brand = brand              # instance variable
        self.colour = colour
        """Constructor (__init__) object me pass ki gayi arguments ko instance variables
         me store kar deta hai, taaki unhe baad me methods ke through use kiya ja sake."""

    def start(self):   # method for every object
        print(f"start {self.brand}")

    def details(self):
        print(f"Brand {self.brand}, and colour {self.colour}")

# Creating object (yaha arguments pass karne padenge)

mustang = Car("Ford Mustang", "Red")
bmw_x = Car("BMW", "Black")

# Using object methods
mustang.start()
mustang.details()
bmw_x.details()
bmw_x.details()


print("-------------Class Variable-----------")

class Student(): # declare class
    School_name="DK Carmel High School,Ara" # class variable

    def __init__(self,name,Roll_no,Marks): # set constructor
        self.name = name
        self.Roll_no = Roll_no
        self.Marks = Marks

    def student_info(self):   # Instance Method
        print(f"Name: {self.name},"
              f"Roll_no: {self.Roll_no},"
              f"Marks: {self.Marks},"
              f"School_Name: {self.School_name}")

Balak=Student("Abhishek-Singh","20mecp01","A") # Declare object
Balak.student_info()

print("------------- Class Method---------------")

class BankAccount():
    Bank_Name= "State Bank Of India" # class variable

    def __init__(self,account_holder,account_no,balance): # constructor
        self.account_holder=account_holder
        self.account_no=account_no
        self.balance=balance

    def account_details(self):  # object Method
        print(
            f"Bank_Name: {self.Bank_Name},"
              f"Account_Holder: {self.account_holder},"
              f"Account_No: {self.account_no},"
              f"Balance: {self.balance}"
            )

    @classmethod    # Declaring class_method that will update Bank_Name
    def change_bank(cls,new_name): # class_method
        cls.Bank_Name=new_name

F_acc_1=BankAccount("Babu-Rao-Ganpat",
                    1243565432,
                    40000000)

F_acc_1.account_details()
BankAccount.change_bank("Punjab National Bank")
F_acc_1.account_details()

print("-----------------Statice method----------------")

"""
Static Method Kya Hai?
Ek aisa method jo na object (self) ka data use karta hai, na class (cls) ka data.
Ye bas ek helper/utility function hota hai jo logically class se related ho sakta hai.
Isse banane ke liye @staticmethod decorator lagate hain.

"""

class Temprature_converter():

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius*9/5)+32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return  (fahrenheit-32) *(5/9)


print(Temprature_converter.fahrenheit_to_celsius(100))
print(Temprature_converter.celsius_to_fahrenheit(100))


class Circle():
    def __init__(self,radius): # Constructor
        self.radius=radius

    def area_Of_Circle(self):  # Instance method
        return(f"Area:{3.14* self.radius **2}")

    def circumfrence_Of_Circle(self):
        return(f"Circumfrence: {3.14* self.radius *2}")

    @staticmethod
    def is_valid_radius(radius):
        return radius > 0


park=Circle(5)

print("Area_of_Park =", park.area_Of_Circle())
print("Circumfrence_of_Park =", park.circumfrence_Of_Circle())

print("--------- Case Implementation----------")

class SmartBankAccount():

    bank_name= "Global Trust Bank"

    def __init__(self,account_holder,account_no,balance):
        self.account_holder=account_holder
        self.account_no=account_no
        self.balance=balance

    def account_info(self):
        print(f"account_holder= {self.account_holder},"
              f"account_no={self.account_no},"
              f"balance={self.balance},"
              f"Bank_Name= {SmartBankAccount.bank_name}")

    def deposit(self,ammount):
        self.balance += ammount
        return self.balance

    def withdraw(self,ammount):
        if self.balance >= ammount:
            self.balance -= ammount
            return self.balance
        else:
            return("Insufficient Balance")


    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name

    @staticmethod
    def check_account_number(account_no):
        if len(str(account_no))==10:
            return "Legitimate account_no"
        else:
            return "Invalid account_no"



a1 = SmartBankAccount("Ravi", 1234567890, 5000)
a1.account_info()

a1.deposit(2000)
print(a1.balance)

a1.withdraw(1000)
print(a1.balance)

SmartBankAccount.change_bank_name("Future Finance Bank")
a1.account_info()

print(SmartBankAccount.check_account_number(1234567890))
print(SmartBankAccount.check_account_number(12345))


print("---------------------------Inheritance---------------------------------")

