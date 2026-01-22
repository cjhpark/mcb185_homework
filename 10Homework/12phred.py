#chr() turns ASCII to a letter
#ord() turns letter to ASCII
#Edge cases return none
import math

def phredPtoQ(your_probability):
	if your_probability >=0 and your_probability <=1: return chr(round(-10*math.log10(your_probability)+33))
	else: return None

#Q = -10*math.log10(P)
#ASCII = Q + 33 = -10*math.log10(P)+33
#ASCII 33 = Q 0
#ASCII 41 = Q 8


def phredQtoP(your_letter):
	if ord(your_letter) >= 33: return 10**(-(ord(your_letter)-33)/10)
	else: return None

#Q = ASCII - 33 = ord(your_letter) - 33
#P = 10**(-(ord(your_letter)-33)/10)

print(phredQtoP('A'))
print(phredPtoQ(.001))