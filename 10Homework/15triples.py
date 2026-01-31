#15triples.py Chris Park

a = 1
b = 1
for a in range(3, 100):
	while b < 100:
		if (a**2+b**2)**0.5 % 1 == 0 and (a**2+b**2)**0.5 < 100: print(a, b, (a**2+b**2)**0.5)
		b += 1
	b = 1

#This problem was pretty fun. I'm not sure if there are more efficient ways to solve this problem with the tools we have right now, but I knew that we had to do pair-wise comparisons and see if the the square root of their sum of squares was an integer. I decided the best way was to fix a and then run a iteration within it from b = {1, 99}. After running through and finding every pair, it would reset b and then move to the next a. 
