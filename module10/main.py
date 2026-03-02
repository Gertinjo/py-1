class Student:
    def __init__(self , name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
         self.__age = age
    def set_name(self, name):
         self.__name = name


student1 = Student("Gerti" , 5)

print("Name: ", student1.get_name())

print("Age : ", student1.get_age())
student1.set_name("Dreni")
print("Updated name: ", student1.get_name())

print("Age : ", student1.get_age())

student1.set_age(16)
print("Update age: " , student1.get_age())