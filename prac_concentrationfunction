#prac_concentrationfunction Chris Park

def od260toconcentrations(od260, dsBPs):
	return round(((1000*od260*50)/(615.94*dsBPs+36.04)), ndigits=3)
print(od260toconcentrations(1.03, 60), "umolar")
#According to NEB, one OD260 unit is equal to 50ug/ml of dsDNA
#One basepair of dsDNA is 615.94 g/mol on average. This number accounts for the two waters lost during polymerization and adds them back for the termini.

#How do I make it so I can print both ug/ml and umolar?