class Vehicle:

    def __init__(self, make, modul, year):

        self.make = make
        self.module = modul
        self.year = year

    def display_info(self):
        print(f"Make :{self.make}, Module {self.module} , Year:{self.year}")



class Car(Vehicle):
    def __init__(self, make , modul ,year, body_style):
        super().__init__(make,modul,year)
        self.body_style = body_style





class ElectricCar(Car):

    def __init__(self,make,modul,year,body_style,battery_capacity):
        super().__init__(make,modul,year,body_style)

        self.battery_capacity = battery_capacity


    def charge(self):
        print("Charging electric car.")


tesla = ElectricCar(" Tesla", " Cybertruck" ,  2023, " triangular", 122.4)


tesla.display_info()

print("Body Style:", tesla.body_style)

print("Battery Capacity",  tesla.battery_capacity)

tesla.charge()