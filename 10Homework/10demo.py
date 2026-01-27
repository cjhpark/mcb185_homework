#10demo.py Chris Park
import math
import random
print("hello, again")

#Scientific Notation
print(1.5e-2)

#Math Operators
print(1+2)
print(1-2)
print(2*2)
print(2/1)
print(2**2)
print(5//4)
print(10%4)
print(3*(1+2))
print(math.ceil(5.2))
print(math.log2(8))
print(math.sqrt(9))
print(math.factorial(5))
print(math.e)

#Variables and Functions
a = 3
b = 4
c = (a**2 + b**2)**0.5
print(c)

print(type(a), type(b), type(c), sep=', ', end='!\n')

def right_hypotenuse(sidea, sideb):
	return math.sqrt(sidea**2 + sideb**2)
print(right_hypotenuse(3, 4))

#Conditionals
a = 2.0
b = 2*1.0
if a == b:
	print('Apple')

c = a == b
print(c)
print(type(c))

if a < b or a > b: print('Cool')
if a < b and a > b: print('How')
if not False: print(True)

if math.isclose(a, b): print('close')

#None
def banana(m, x, b):
	y = m * x + b 
print(banana(2, 3, 4))

#While
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 5: break

#For and Range
for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(10):
	print(i)

#Random
for i in range(5):
	print(random.random())

for i in range(3):
	print(random.randint(1, 6))