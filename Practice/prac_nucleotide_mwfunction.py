#prac_nucleotide_MW Chris Park

def nucleotide_MW(your_nucleotide):
	if your_nucleotide == 'A' or your_nucleotide == 'a':
		return '331.2 g/mol'
	elif your_nucleotide == 'C' or your_nucleotide == 'c':
		return '307.2 g/mol'
	elif your_nucleotide == 'T' or your_nucleotide == 't':
		return '322.2 g/mol'
	elif your_nucleotide == 'G' or your_nucleotide == 'g':
		return '347.2 g/mol'
	else:
		return None

print(nucleotide_MW('A'))

#Using the MW of deoxyribonucloetide monophosphates from ThermoFisher