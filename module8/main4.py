class Student:
    school_name = "Digital School"
    def __init__(self , name , age , course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Gerti" , 12 , "Python")
print(student1.course)