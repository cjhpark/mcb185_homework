# 30demo.py Chris Park
import sys
import random
import math

#maximum length= int
#window length = list? or int?
# Is this method horribly inefficient/taxing?
#You can note the starting index and 'starting index + length' and return the slice of the original.
# it is redundant since you have a string of polyAs, length at i+1 is just length of i-1.Consider a while look where you update the value of the index position at the end. 'new starting index = run length'.


#iterate using a conditional that is only active when the string starts with an A and ends with != A. At the end of each iteration, have an if statement compaing maximum length and the current window length. If it's longer, update the variable maxmimum length and reset window length.

for i in range(100):
	is_prime = False
	c = ''
	if i == 0 or i == 1 or i == 2: is_prime = True
	elif i % 2 == 0: is_prime = False
	elif i % 2 != 0:
		for j in range(2, i):
			is_prime = True
			if i % j == 0:
				is_prime = False
				break
	if is_prime == True: c = 'Fizz*'
	print(i, c)

#Dust
def entropy(s):
	pa = s.count('A') / len(s)
	pc = s.count('C') / len(s)
	pg = s.count('G') / len(s)
	pt = s.count('T') / len(s)
	h = 0
	if s.count('A') != 0: h -= math.log2(pa)
	if s.count('C') != 0: h -= math.log2(pc)
	if s.count('G') != 0: h -= math.log2(pg)
	if s.count('T') != 0: h -= math.log2(pt)
	return h

seq = 'ACGTAAAAAGCGATCG'
k = 5
seqlist = list(seq)
for a in range(len(seq) - k + 1):
	window = seq[a: a + k]
	if entropy(window) < 1.0:
		for j in range(a, a+k):
			seqlist[j] = 'N'
print(''.join(seqlist))

# Birthday Paradox
calendar = int(sys.argv[1])
birthdays = int(sys.argv[2])
trials = int(sys.argv[3])

matches = 0
for k in range(trials):
	classroom = []
	for i in range(birthdays):
		bday = random.randint(0, calendar-1)
		if bday in classroom:
			print('Match')
			matches += 1
			break
		classroom.append(bday)
print(matches/trials)
