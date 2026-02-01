#16savingthrows.py Chris Park

import random

for i in range(25):
	difficulty_class = random.randint(1, 3)
	first_roll = random.randint(1, 20)
	second_roll = random.randint(1, 20)
	advantage_status = random.randint(1, 3)

	if advantage_status == 1:
		kept_roll = first_roll
		advantage_str = 'no advantage'
	if advantage_status == 2:
		kept_roll = max(first_roll, second_roll)
		advantage_str = 'advantage'
	if advantage_status == 3:
		kept_roll = min(first_roll, second_roll)
		advantage_str = 'disadvantage'

	if kept_roll >= 5*difficulty_class: character_status = 'lived.'
	if kept_roll <= 5*difficulty_class: character_status = 'died.'

	print('You had', advantage_str, 'and rolled', kept_roll, 'against difficulty class', 5*difficulty_class, 'and', character_status)

#Another fun one, but slightly challenging. Not necessarily because I didn't know where to complete it, but rather complete it in a way that was somewhat efficient. I wanted to keep the 'if' statements to a minimum.
