class Vertebrate:

    def __init__(self,backbone =True):
        self.has_backbone = backbone

    def vertebrare_info(self):
        print("Vertebreate have a backbone")


class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat


    def aquatic_info(self):
        print("Aquatic animals live in water")


class Fish(Vertebrate,Aquatic):


    def __init__(self, species , backbone=True, habitat = "water"):

        super().__init__(backbone=backbone)

        self.habitat = habitat

        self.species = species

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print("The fish is swimming")

pufferfish = Fish("Puffer")

print(pufferfish.has_backbone)

print(pufferfish.has_backbone)

pufferfish.vertebrare_info()

pufferfish.aquatic_info()

pufferfish.fish_info()

pufferfish.swim()
