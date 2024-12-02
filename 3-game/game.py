# Data Initialization
digitSum = 0

# Player round declaration
numberOfTurns = int(input())

# Game
for turn in range(numberOfTurns):
	# Player turn
	playerDigit = int(input())
	digitSum += playerDigit

	# CPU turn
	cpuDigit = 9 - (digitSum % 9)
	print(cpuDigit, flush=True)
	digitSum += cpuDigit
