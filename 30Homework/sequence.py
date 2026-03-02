# sequence.py Chris Park

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rev = []
	for nt in dna[::-1]:
		if 		nt == 'A': 	rev.append('T')
		elif	nt == 'C': 	rev.append('G')
		elif 	nt == 'T': 	rev.append('A')
		elif	nt == 'G': 	rev.append('C')
		else:				rev.append('N')
	return ''.join(rev)

# Barebones translation suing the list.index() method. Extend the 'codons' and 'aminos' list to get all translations
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	TL = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			aa = aminos[codons.index(codon)]
			TL.append(aa)
		else:
			TL.append('X')
	return ''.join(TL)
