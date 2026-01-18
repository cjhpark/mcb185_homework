#prac_speedfunction Chris Park

def mphtokph(mph):
	return round(mph*1.61, ndigits=2)
print(mphtokph(65), "kph")

def kphtomph(kph):
	return round(kph/1.61, ndigits=2)
print(kphtomph(105), "mph")