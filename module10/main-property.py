from tkinter.font import names

from main import student1


class Student:
    def __init__(self, name , age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

student1 = Student("Dreni" , 12)

print("Name : ", student1.name)
print("Age :" , student1.age)

student1.name = "Gerti"
student1.age = 13

print("Updated name : ", student1.name)
print("Updated age : ", student1.age )