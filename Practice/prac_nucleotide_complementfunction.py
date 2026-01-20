#prac_nuclotide_complementfunction

def nucleotide_complement(your_nucleotide):
	if your_nucleotide == 'A' or your_nucleotide == 'a':
		return 'T'
	elif your_nucleotide == 'C' or your_nucleotide == 'c':
		return 'G'
	elif your_nucleotide == 'T' or your_nucleotide == 't':
		return 'A'
	elif your_nucleotide == 'G' or your_nucleotide == 'g':
		return 'C'
	else:
		return None

print(nucleotide_complement('A'))