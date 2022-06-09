

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return (f"There are {cls.active_users} users logged in")

	@classmethod
	def from_string(cls, data_string):
		first, last, age = data_string.split(",")
		return cls(first, last, int(age)) # cls is User


	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def __repr__(self):
		return self.full_name()

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy Birthday, {self.first}! You are now {self.age}."

	def print(self):
		print(f"{self.first} {self.last} {self.age}")



# user1 = User("Geralt", "of Rivia", 99)
# user2 = User("Cloud", "Strife", 22)

# print(User.display_active_users())
# print(f"{user1},", user2, "\n")

# print(user1.initials())
# print(user1.is_senior())
# print(user1.birthday())
# print(user1.logout())

# print(User.display_active_users())
# print(user2, "\n")

# user3 = User.from_string("Jon,Snow,25")
# print(User.display_active_users())
# print(f"{user1},", user3, "\n")


class Moderator(User):

	total_mods = 0

	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_total_mods(cls):
		return f"There are currently {cls.total_mods} total mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community"

cloud = Moderator("Cloud", "Strife", 22, "Midgar")
geralt = Moderator("Geralt", "of Rivia", 22, "Witcher")
print(cloud.remove_post())
print(Moderator.display_total_mods())