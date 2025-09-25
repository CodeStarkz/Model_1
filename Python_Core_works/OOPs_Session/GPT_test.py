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