# Data Initialization
cards = {
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0,
	'7': 0,
	'8': 0,
	'9': 0,
	'10': 0,
	'J': 0,
	'Q': 0,
	'K': 0,
	'A': 0,
}
cardValues = {
	'J': 1,
	'Q': 2,
	'K': 3,
	'A': 4,
}
isCheater = False
points = 0

# Declaration of the number of cards
numberOfCards = int(input())

if numberOfCards != 13:
	isCheater = True

# Reading cards
for i in range(numberOfCards):
	# Read next card
	currentCard = input()

	# If the card does not exist, it is a fraud
	if currentCard not in cards:
		isCheater = True
		continue

	# Increment number of cards
	cards[currentCard] += 1

	# Add points
	points += cardValues.get(currentCard, 0)

# Check if the number of cards is correct
if any(value > 5 for value in cards.values()):
	isCheater = True

# Show result
if isCheater: print('OSZUST!')
else: print(points)