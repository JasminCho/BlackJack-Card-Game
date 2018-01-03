"""
One player vs Automated dealer
Player can stand or hit
Player must be able to pick betting amount
Keep track of player's total money
Alert win, loss, bust, etc
Classes for: Deck, Player's Hand

BONUS:
Add Double-Down
Card Splits
Multiplayer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Game Objective:
Beat Dealer by:
	Get 21 Points on player's first two cards without a dealer blackjack
	Reach final score higher than dealer without exceeding 21
	Let dealer draw additional cards until their hand exceeds 21

Rules:
	At the beginning of each round, up to 3 players can place bets
	Players dealt 2 cards each
	Dealer dealt two cards, one exposed, one facedown
	Values of cards:
		2-10 = 2-10
		Face cards (Jack, Queen, King) = 10
		Ace = 1 or 11
	Dealer hand not completed if all players busted or received blackjacks
	Dealer hits until hand totals 17+
	Players win by:
		Not busting and having total higher than dealer
		Not busting and having dealer bust
		Getting blackjack without dealer getting blackjack
	If player and dealer have same total not counting blackjacks (push), player 
	doesn't win or lose money  but dealer wins
	If player wins, they win the amount they bet
	If player loses, they lose the amount they bet
	If player wins with a blackjack, they win the amount they bet * 1.5

Player Decisions:
	Hit: take another card from dealer
	Stand/Stay: Take no more cards
	Double Down: Player allowed to increase initial bet by 100% in exchange for 
	committing to stand after receiving exactly one more card
	Split: If first two cards of a hand have the same value, the player can split them
	into two hands by moving a second bet equal to the first. Dealer separates two cards and draws
	additional for each. Hands treated as two individual hands with player winning or losing wager
	separately for each hand
	Surrender: Directly after dealer has checked for blackjack. The house takes half player's bet and
	returns other half to player 
"""

class Card(object):
	values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		return('%s of %s' % (Card.values[self.value], Card.suits[self.suit]))

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for value in range(0,13):
				card = Card(value, suit)
				self.cards.append(card)

	def __str__(self):
		printDeck = [str(card) for card in self.cards]
		return '\n'.join(printDeck)

	def draw_card(self):
		# Get a random Card(value, suit) and make sure it isn't already drawn

class Player(object):
	def __init__(self, totalMoney=1000, hand=[]):
		self.totalMoney = totalMoney
		self.hand = [Card(value, suit)]

	def add_money(self, amount):
		self.totalMoney += amount

	def make_bet(self, betAmount):
		return(betAmount)

	def get_hand(self, card1, card2):
		self.card1 = card1
		self.card2 = card2
		self.totalValue = Card.add_values()

# Test, prints Ace of Diamonds
# card = Card(0,1)
# print(card)

# Test, prints all cards in deck
# deck = Deck()
# print(deck)
