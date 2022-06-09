

class Pet:

	allowed = ["cat", "dog", "fish", "rat"]

	@classmethod
	def domesticate(cls, species):
		if species not in Pet.allowed:
			Pet.allowed.append(species)
			return f"{species} is now allowed to be a pet!"
		return f"{species} is already allowed to be a pet..."

	@classmethod
	def extinct(cls, species):
		if species in Pet.allowed:
			Pet.allowed.remove(species)
			return f"{species} can no longer be a pet :("
		return f"{species} wasn't allowed to be a pet"

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

print(Pet.allowed)
print(Pet.domesticate("bear"))
print(Pet.allowed)
print(Pet.extinct("cat"))
print(Pet.allowed)