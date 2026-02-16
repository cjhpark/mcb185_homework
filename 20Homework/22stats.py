#22stats.py Chris Park

import sys
import math

inputs = []
for values in sys.argv[1:]:
	inputs.append(float(values))
	inputs.sort()

#mean
total = 0.0
for i in inputs: total += i
mean = total/len(inputs)

#stddev
stddevsum = 0
for i in inputs:
	stddevsum += (i - mean)**2
stddev = (stddevsum/len(inputs))**0.5

#median
if len(inputs) % 2 == 0:
	median = (inputs[len(inputs)//2 - 1] + inputs[len(inputs)//2])/2
if len(inputs) % 2 == 1:
	median = inputs[len(inputs)//2]

#minimum
minimum = float(inputs[0])
for j in range(len(inputs)):
	if float(inputs[j]) < minimum: minimum = float(inputs[j])

#maximum
maximum = float(inputs[0])
for k in range(len(inputs)):
	if float(inputs[k]) > maximum: maximum = float(inputs[k])

print(mean, stddev, median, minimum, maximum)
