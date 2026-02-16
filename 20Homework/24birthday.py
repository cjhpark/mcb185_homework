#24birthday.py Chris Park

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for t in range(trials):
	calendar = []
	for date in range(0, days):
		calendar.append(0)

	for ppl in range(people):
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1

		if 2 in calendar:
			matches += 1
			break

probability = matches/trials

print(probability)
