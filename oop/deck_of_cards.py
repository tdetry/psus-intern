import random

class Card:

	allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"


class Deck:
	
	def __init__(self):
		self.cards = [Card(suit, value) for suit in Card.allowed_suits for value in Card.allowed_values]

	def __repr__(self):
		return f"Deck has {self.count()} cards"

	def _deal(self, num):
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		else:	
			return [self.cards.pop() for i in range(0, min(num, self.count()))] # Don't deal out more cards than are in the deck!

	def count(self):
		return len(self.cards)

	def shuffle(self):
		if self.count() != 52:
			raise ValueError("Only full decks can be shuffled")
		else:
			random.shuffle(self.cards)
			return self

	def deal_card(self):
		card = self._deal(1)
		return card[0]

	def deal_hand(self, num):
		hand = self._deal(num)
		self.cards = [c for c in self.cards if c not in hand]
		return hand


d1 = Deck()
print(d1)
d1.shuffle()

print(d1.deal_hand(8))
print(d1.deal_card())
print(d1)
