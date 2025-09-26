# Python_Core_works

#Desinging School Management System


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        print(
            f"name: {self.name},"
            f"age: {self.age}"
              )

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        Person.__init__(self,name,age)
        self.subject=subject
        self.salary=salary

    def show_details(self):
        print(
            f"Teacher_Name: {self.name},"
              f"Subject: {self.subject},"
              f"Salary: {self.salary}"
        )
class Student(Person):

    def __init__(self,name,age,roll_no,grade):
        Person.__init__(self,name,age)
        self.roll_no=roll_no
        self.grade=grade

    def show_details(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")

class Monitor(Student,Teacher):
    def __init__(self,duty,name,age,roll_no,grade,subject,salary):
        Student.__init__(self,name,age,roll_no,grade)
        Teacher.__init__(self,name,age,subject,salary)
        self.duty=duty
    def show_details(self):
        print(
            f"Monitor_name: {self.name},"
            f"Roll_no: {self.roll_no},"
            f"Subject_Assigned: {self.subject},"
            f"Duty: {self.duty}"

        )

#--------------------Test zcase_-------------------

m = Monitor("Class Discipline", "Abhishek", 22, 7, "A", "Math", 50000)
m.show_details()