class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi im {self.name} and i am {self.age} years old")

person1 = Person( "Gerti" , 12)
person2 = Person( "Dreni" , 16.5)

person1.greet()
person2.greet()