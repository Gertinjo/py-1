class Person:
    def __init__(self, name, age , weight , height):
        self.name = input(name),
        self.age = input(age),
        self.weight = input(weight),
        self.height = input(height)
    def calculate_bmi(self):
        return self.weight/self.height
    def get_bmi_category(self):
        return "Underweight" , "normalWeight" , "OverWeight" , "Obese"
    def print_info(self):
        catogory = self.get_bmi_category()
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"weight: {self.weight}")
        print(f"height: {self.height}")

    @property
    def name(self):
        return self.name
    @property
    def age(self):
        return self.age

    @property
    def weight(self):
        return self.weight

    @property
    def height(self):
        return self.height

    @name.setter
    def name(self, name):
        self.name = name

    @age.setter
    def age(self, age):
        self.age = age

    @weight.setter
    def weight(self, weight):
        self.weight = weight
    @height.setter
    def height(self, height):
        self.height = height



class Adult(Person):
    def adult_class(self, name, age, weight, height, bmi):
        self.name = name,
        self.age = age,
        self.weight = weight,
        self.height = height
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            print(f"You are underweight your bmi is {bmi}")
        elif 18.5 < bmi < 24.9:
            print(f"You are NormalWeight your bmi is {bmi}")
        elif 24.9 < bmi < 29.9:
            print(f"You are OverWeight your bmi is {bmi}")
        elif bmi < 29.9:
            print(f"You are Obese your bmi is {bmi}")
        else:
            print("Cannot calculate")
class Child(Person):
    def adult_class(self, name, age, weight, height, bmi):
        self.name = name,
        self.age = age,
        self.weight = weight,
        self.height = height
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            print(f"You are underweight")
        elif 18.5 < bmi < 24.9:
            print(f"You are NormalWeight")
        elif 24.9 < bmi < 29.9:
            print(f"You are OverWeight")
        elif bmi < 29.9:
            print(f"You are Obese")
        else:
            print("Cannot calculate")

def collect_info():
    name = input("Name:")
    age = input("age:")
    weight = input("weight:")
    height = input("height:")
def add_person(self, person):
    self.people.append(person)
def print_result(self):
    for person in self.people:
        person.print_info()
def run(self):
    print(collect_info())