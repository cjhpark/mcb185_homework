#17deathsaves.py Chris Park

import random

for i in range(25):
	successes = 0
	failures = 0
	rolls = 0
	while successes < 3 and failures < 3:
		roll = random.randint(1,20)
		rolls += 1
		if roll == 1:
			failures += 2
		elif roll <= 9:
			failures += 1

		if roll == 20:
			status = 'revived and are at 1 hit point. This outcome has a probability of 5%!'
			break
		elif roll >= 10:
			successes += 1

	if failures >= 3:
			status = 'died.This outcome has a probability of 45%.'

	if successes == 3:
			status = 'are stable but unconscious. This outcome has a probability of 55%.'

	print('You rolled', rolls, 'time(s) and', status)
