#prac_isprobability Chris Park

def isprobability(your_number):
	if your_number >= 0 and your_number <= 1:
		return True
	else:
		return False

print(isprobability(0.5))