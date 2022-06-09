class Chicken:

    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

c1 = Chicken(name="Bob", species="Partridge Silkie")
c2 = Chicken("Alice", "Speckled Sussex")

print(f"There are {Chicken.total_eggs} eggs")
for i in range (0, 10): c1.lay_egg()
for i in range(0, 3): c2.lay_egg()
print(f"There are {Chicken.total_eggs} eggs")
