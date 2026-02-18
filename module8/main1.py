from main import calculate_area, perimeter, calculate_perimeter


class  Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def calculated_area(self):
        return self.length * self.width
    def calculated_perimeter(self):
        return 2 * (self.length + self.width)
    # def calculated_perimeter(self):
    #     return 2 * (self.length + self.width) , self.length * self.width

my_rectangle = Rectangle(5 , 3)


area = my_rectangle.calculated_area()
perimeter = my_rectangle.calculated_perimeter()
# perimeter1 = my_rectangle.calculated_perimeter()

print(f"Your area is {area}")
print(f"Your perimeter is {perimeter}")
# print(f"Your perimeter is {perimeter1}")