# 33ntcomp.py Chris Park

import sys
import mcb185

# Iterating through and assigning index to variables 
for defline, seq in mcb185.read_fasta(sys.argv[1]):
# Breaking apart into name and description
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	T = 0
	G = 0
	N = 0
	for nt in seq:
		if 		nt == 'A': A += 1
		elif 	nt == 'C': C += 1
		elif	nt == 'T': T += 1
		elif 	nt == 'G': G += 1
		else: 	N += 1
	print(name, A/len(seq), C/len(seq), T/len(seq), G/len(seq), N/len(seq))

# You can use a list with each entry being a different nucleotide. Iterate through and print the count/length

# This method doesn't use a bunch of if, elif, else. Go through each nt, index it to a reference string using str.find() and update a count list
# nts = 'ACTGN'
# counts = [0] * len(nts)
# for nt in seq:
#	idx = nts.find(nt)
# 	counts[idx] += 1
# print(name, end=' ')
# for n in counts: print(n/len(seq), end=' ')
# print()
