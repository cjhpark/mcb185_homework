#20demo.py Chris Park
import math
import sys


print(len('Testing'))

#s.upper method syntax
s = 'strawberry'
print(s.upper())

#String formatting
print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print('{} {:.3f}'.format('str.format', math.pi))
print(f'{math.pi}')
print('%s %.3f' % ('printf',  math.pi))

#Indicies
seq = 'Watermelon'

print(seq[0], seq[-2])
for i in seq:
	print(i, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

#Slices
dog = 'ABCDEFGH'
print(dog[0:4])

dna = 'GCGCGAGTAGCGACG'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

#Tuples
car = ('fish', 2, 2.3, math.pi)
print(car[0])
print(car[1])
print(car[::2])

#Enumerate and Zip
nts = 'ACTG'
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

#Lists
nts = ['A', 'C', 'T']
print(nts)
nts.append('G')
print(nts)
nts.pop()
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)


New = nts.copy()
print(New)

alph = 'ABCDEFGHIJKL'
print(alph)
aas = list(alph)
print(aas)


#Splitting and Joining
text = 'hello world                 hello back'
words = text.split()
print(words)

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching
if 'A' in alph: print('Hurrah')
if 'a' in alph: print('Boo')

print('index G?', alph.index('G'))
#print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))

print(sys.argv)


#Crazy
#def crazy(s):
#	for i in range(len(s)):
#		if i % 2 == 0: print(i, s[i].upper())
#		else: print(i, s[i].lower)
#
#filename = sys.argv[1]
#with open(filename) as fp:
#	for line in fp:
#	crazyline = crazy(line)
#	print(crazyline)

#Anti

def anti(dna):
	comp = []
	rev = dna[::-1]
	for nt in rev:
		if nt == 'A': comp.append('T')
		if nt == 'G': comp.append('C')
		if nt == 'C': comp.append('G')
		if nt == 'T': comp.append('A')
	return ''.join(comp)

seq = input('Type sequence')
print(seq)
print(anti(seq))

#maxlenstring
def longest_str(s):
	placeholder = s[0]
	for i in range(len(s)):
		if len(s[i]) > len(placeholder): placeholder = s[i]
	return placeholder

string =  ['ssssssssssssssssssssssss', 'a', '3.414', '34343434']
print(longest_str(string))

#Pairwise Comparison
import sys
import random

classroom = []
people = int(sys.argv[1])
calendar = int(sys.argv[2])

for i in range(people):
	birthday = random.randint(0, calendar-1)
	classroom.append(birthday)

print(classroom)
