#21entropy.py Chris Park

import sys
import math

p = []
for prob in sys.argv[1:]:
	if float(prob) >= 0 and float(prob) <= 1:
		p.append(float(prob))

sum = 0
for prob in p: sum += prob

entropy = 0
if math.isclose(sum, 1.0):
	for probs in p:
		entropy -= probs*math.log2(probs)

print(f'{entropy:.4f}')
