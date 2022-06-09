"""
Inheritance 
"""
class Animal:

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"


	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat")
		self.breed = breed
		self.toy = toy
	def play(self):
		return f"{self.name} plays with {self.toy}"

a = Cat("Blue", "Scottish Fold", "String")
a.make_sound("meow")
print(a.play())

"""
Properties
"""
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("Age can't be negative!")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"
	

js = Human("Jon", "Snow", 25)
print(js.age)
# js.age = -100
print(js.age)
print(js.full_name)