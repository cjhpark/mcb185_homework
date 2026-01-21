#prac_threemaximumfunction Chris Park

def threemaximum(x, y, z):
	if x >= y and x >= z: return x 
	if y >= z: return y
	else: return z

print(threemaximum(5, 1, 3))