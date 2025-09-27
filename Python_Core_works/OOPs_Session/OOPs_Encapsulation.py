# Cab Booking System

class Cab():


    base_fare=50            #(base fare )
    def __init__(self,driver_name,car_no,current_location,phone_no):
        self.driver_name=driver_name
        self.car_no=car_no
        self.current_location=current_location
        self.__phone_no=phone_no  # protected


    def driver_info(self):   # method to get the driver details
        print(
            f"Driver Name: {self.driver_name},"
              f"Car no: {self.car_no}"
              )

    def get_phone_no(self):   # method to get the phone no as it is protected
        print(f"Cab driver phone_no: {self.__phone_no}")

    def update_phone_no(self,new_phone_no): # method to update the phone no
        self.__phone_no=new_phone_no
        print(f"phone_no is: {self.__phone_no}")



    @classmethod
    def update_base_fare(cls ,new_fare):  # method to update the fare as it is class variable
        cls.base_fare=new_fare
        return(f"updated_base_fare: {cls.base_fare}")

    @staticmethod
    def calculate_distance(loc1,loc2):  # method to calculate the distance
        print(f"distance: {abs({loc1}-{loc2})}")

class Minicab(Cab):

    def __init__(self,driver_name,car_no,current_location):
        Cab.__init__(self,driver_name,car_no,current_location):


    def fare_calculation(self):
        print(f"fare is {self.calculate_distance()}*{self.base_fare} ")

class LuxuryCab(Cab):
    def __init__(self):
        Cab.__init__(self, driver_name, car_no, current_location):


# still need to develop