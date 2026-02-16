#23birthday.py Chris Park
import sys
import random


trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for t in range(trials):
	status = False
	birthdays = []
	for i in range(people):
		birthdays.append(random.randint(0, days))
	for a in range(0, len(birthdays)):
		for b in range(a+1, len(birthdays)):
			if birthdays[a] == birthdays[b]:
				matches += 1
				status = True
			if status == True: break
		if status == True: break

probability = matches/trials

print(probability)
