class Animals:
    def sounds(self):
        print("Generic sounds of animals")


class Dog(Animals):
    def sounds(self):
        print("Woof! Woof!")

class Cat(Animals):
    def sounds(self):
        print("Meow! Meow!")

animals = Animals()
animals.sounds()
dog = Dog()
dog.sounds()
cat = Cat()
cat.sounds()



