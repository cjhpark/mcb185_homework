#prac_temperaturefunction Chris Park

def celsiustofahrenheit(celsius):
	return 9/5*(celsius)+32
print(round(celsiustofahrenheit(25), ndigits=2), "F")

def fahrenheittocelsius(fahrenheit):
	return 5/9*(fahrenheit-32)
print(round(fahrenheittocelsius(77), ndigits=2), "C")