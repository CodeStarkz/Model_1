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
    item = "Luxury"   # class variable - remain same for all objects in the class / Class argument

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

class BankAccount(): # Declare Class

    def __init__(self,account_holder,account_no,balance): # Constructor
        self.account_holder=account_holder
        self.account_no=account_no
        self.balance=balance

    def deposit(self,ammount): # method
        self.balance += ammount
        return self.balance
    def withdraw(self,ammount): # method
        if self.balance >= ammount:
            self.balance -=ammount
            return self.balance

        else:
            return "insufficient balance"

class SavingAccount(BankAccount): # child class 1 having parent as BankAccount

    def __init__(self,account_holder,account_no,balance,intrestrate): # constructor
        super().__init__(account_holder,account_no,balance) # calling parent class's  constructor
        self.intrestrate=intrestrate

    def apply_intrest(self): # child method
        self.balance += (self.intrestrate / 100) * self.balance
        return self.balance


class CurrentAccount(BankAccount): # child class 2 having parent as BankAccount

    def __init__(self,account_holder,account_no,balance,overdraft_limit): # constructor
        super().__init__(account_holder,account_no,balance) # passing parent constructor
        self.overdraft_limit=overdraft_limit

    def withdraw(self,ammount): # child method
        if self.balance + self.overdraft_limit >= ammount:
            self.balance -= ammount
            return self.balance
        else:
            return("overlimit exceeded")



# -------------------test cases------------------------------------

# Create Saving Account
savings = SavingAccount("Abhishek", 101, 5000, 5)

print("---- Saving Account ----")
print("Initial Balance:", savings.balance)
print("Deposit 2000:", savings.deposit(2000))   # 7000
print("Withdraw 3000:", savings.withdraw(3000)) # 4000
print("Apply Interest:", savings.apply_intrest())  # 4000 + 5% = 4200


# Create Current Account
current = CurrentAccount("Singh", 102, 3000, 2000)

print("\n---- Current Account ----")
print("Initial Balance:", current.balance)
print("Withdraw 4000 (within overdraft):", current.withdraw(4000)) # -1000 (allowed)
print("Withdraw 2000 more (exceeds overdraft):", current.withdraw(2000)) # Overlimit exceeded
print("Deposit 5000:", current.deposit(5000)) # Balance updated

print("---------------------Single-Inheritance---------------------------")

"""
super() → parent ka constructor/method call karne ke liye.
MRO (Method Resolution Order) → agar multiple parents hain, Python left-to-right order follow karta hai.
Inheritance → real life relation jaisa (Car is a Vehicle, Dog is an Animal).
"""
# Parent class
class Vehicle():
    def __init__(self,brand):
        self.brand=brand

    def show_brand(self):
        print(f"brand name: {self.brand}")


# Child Class
class Car(Vehicle):
    def __init__(self,brand,doors):
        super().__init__(brand) # parent constructor call
        self.doors=doors

    def show_car_details(self):
        print(
            f"car brand: {self.brand},"
            f"no of doors: {self.doors},"
              )

c1 = Car("BMW", 4)
c1.show_car_details()
c1.show_brand()



print("---------------------Multi_level-Inheritance---------------------------")
"""
GrandParent>>Parent>>child

in this way child will able to recall the methods of parent as well as grand parents methods too
"""

class LinvingBeing():
    def breath(self):
        return "Inhale O2, Exhale Co2 "

class Animal(LinvingBeing):
    def Graze(self):
        return "Graze and wonder"

    def hunt_and_fuck(self):
        return(f"hunt the smaller animal then them and with with ownkind")


class Dog(Animal):
    def feature_of_dog(self):
        return "have four leg"


# declare object

husky=Dog()
husky.breath()
husky.feature_of_dog()
husky.hunt_and_fuck()


print("---------------------Multiple- Inheritance-----------------------")

"""
Jab ek child class ke multiple parents hote hain → usse multiple inheritance kehte hain.
👉 Matlab ek class do (ya zyada) classes ka code inherit kar sakti hai.

And Order of Execution Left to Right rhega
"""


class father():
    def __init__(self,job,car,house):
        self.job=job
        self.car=car
        self.house=house

    def Dads_property(self):
        print(
            f"Profession: {self.job},"
              f"Dad have: {self.house},"
              f"dad car: {self.car}"
              )

class Mother():
    def __init__(self,cooking,Jwellery,kindness):
        self.cooking=cooking
        self.Jwellery=Jwellery
        self.kindness=kindness


    def skill(self):
        print(f"cooking skill: {self.cooking},"
              f"mummy ownership: {self.Jwellery},"
              f"mummy behaviour: {self.kindness}"
              )

class its_me_Abhishek(father,Mother):
    # def __init__(self,skill,profession,ownership):
    #     super().__init__(job,car,house)
    #     super().__init__(cooking,Jwellery,kindness)
    #     self.skill=skill
    #     self.profession=profession
    #     self.ownership=ownership
    """ In case of multiple parent  we have to call them explicitly """

    def __init__(self, job, car, house, cooking, jewellery, kindness, my_skill, profession, ownership):
        father.__init__(self, job, car, house) # explicitly call the parent constructor
        Mother.__init__(self, cooking, jewellery, kindness) # explicitly call the parent constructor
        self.my_skill = my_skill
        self.profession = profession
        self.ownership = ownership

    def child_skill(self):
        print(
            f"My skill: {self.cooking} (from mother), "
            f"My car: {self.car} (from father), "
            f"My profession: {self.my_skill}"
        )



    def child_ownership(self):
        print(f"My ownership : {self.house},{self.Jwellery},{self.car}")


# Test case

abhi = its_me_Abhishek(
    job="Engineer", car="BMW", house="Villa",
    cooking="Indian Food", jewellery="Gold", kindness="Polite",
    my_skill="Coding", profession="Software Developer", ownership="Laptop"
)

abhi.Dads_property()
abhi.skill()
abhi.child_skill()
abhi.child_ownership()

print("--------------------Encalsulation---------------------------------")


"""
Encapsulation ka matlab hai data (attributes  object ) aur methods (functions) ko ek class ke andar pack karna aur unki direct access ko control karna.

Matlab: Class ke bahar se koi bhi attribute directly modify na kar paaye.
Hum use karte hain access modifiers (yeh sirf ek convention hote hain Python me).

Types of Access Modifiers 

Public Modifiers = By default, means atributes can be accessed from anywhere

Protected (_var)
Ek convention hai: “Ye sirf class aur subclasses ke liye hai, bahar se use karna allowed hai but recommended nahi hai.”

Protected (_var)
Ek convention hai: “Ye sirf class aur subclasses ke liye hai, bahar se use karna allowed hai but recommended nahi hai.”

"""
# Example for Public
class car(): # Declaring Class
    def __init__(self,brand): # Inititalizing Attributes
        self.brand=brand

    def brand_detail(self):   # declaring method
        print(f"brand detail: {self.brand}")


Scarpion=car("Mahindra") # creating object


Scarpion.brand_detail() # calling object method


# let see the Protected Encasulation

class car():
    def __init__(self,brand):
        self._brand=brand

    def brand_details(self,brand):
        print(f"Brand name is {self._brand}")


GT_Mustang=car("Ford")

print(GT_Mustang._brand)


# lets go for private encasulation


class Bike():
    def __init__(self,mileage,top_speed):
        self.__mileage=mileage
        self.__top_speed=top_speed


    def bike_details(self):
        print(f"topspeed: {self.__top_speed}")
        print(f"mileage: {self.__mileage}"
              )

pulsar=Bike(15,189)

pulsar.bike_details()


print("------------------Abstraction-------------------")
"""

Abstraction: Logic/Implementation hide karna (user ko sirf interface dikhao, andar ka process chhupao).

Python me abstraction karne ke liye hum abc module (Abstract Base Class) use karte hain.
Ek abstract class banate hain jisme abstract methods hote hain (sirf declare, implement nahi karte).
Us class ko koi child inherit karega, to usse compulsory override karna hoga.
"""




























