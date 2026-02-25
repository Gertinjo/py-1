class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound Woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound Meow")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound Ciu Ciu")

dog = Dog("Max")
cat = Cat("Oto")
bird = Bird("Chipo")

for animals in(dog , cat , bird):
    animals.sound(
        
    )