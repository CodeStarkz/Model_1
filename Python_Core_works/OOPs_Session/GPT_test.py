class Laptop():
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram

    def details(self):
        print(f"Brand: {self.brand}, Ram:{self.ram}")


my_machine = Laptop("HP","16GB")

my_machine.details()

print("-------------------------------------------------------------------------")


class car():
    def __init__(self,brand,model,mileage):
        self.brand=brand
        self.mileage=mileage
        self.model=model

    def car_info(self):
        print(f"car brand : {self.brand}",
              f"car model: {self.model}",
              f"car mileage: {self.mileage} ")


Benz=car("Mercidies","Suv",20)

Benz.car_info()

print("----------------------- -------------------------")

class Father:
    def __init__(self, house, f_name):
        self.house = house
        self.f_name = f_name
class Mother:
    def __init__(self, jewellery, m_name):
        self.jewellery = jewellery
        self.m_name = m_name

class Child(Father, Mother):
    def __init__(self, house, jewellery, car,f_name, m_name):
        Father.__init__(self, house, f_name)       # Explicit call
        Mother.__init__(self, jewellery, m_name)   # Explicit call
        self.car = car

c = Child("Villa", "Gold", "BMW")
print(c.house)       # Villa
print(c.jewellery)   # Gold
print(c.car)         # BMW
