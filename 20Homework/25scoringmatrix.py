
#25scoringmatrix.py Chris Park

import sys
import math

#To make the print nicer
alphabet = sys.argv[1]
split_alph = []
for l in range(len(alphabet)):
	split_alph.append(alphabet[l])
print('   '.join(split_alph))

matchscore = int(sys.argv[2])
mismatchscore = int(sys.argv[3])

score = 0
for i in range(len(alphabet)):
	matrixscores = []
	for j in range(len(alphabet)):
		if alphabet[i] == alphabet[j]:	matrixscores.append(matchscore)
		if alphabet[i] != alphabet[j]:	matrixscores.append(mismatchscore)
	print(alphabet[i], matrixscores)
