#prac_isinteger Chris Park
def is_integer(your_number):
	if your_number%1 == 0:
		return True
	else:
		return False

print(is_integer(0.1*10))

#Why do floats give 'True'?