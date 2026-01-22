#Write out the numbers 1 to 100
#If divisible by 3, write 'Fizz'
#If divisible by 5, write 'Buzz'
#If divisible by 3 and 5, write 'FizzBuzz'

for i in range(1,101):
	if i%5 == 0 and i%3 == 0: print('FizzBuzz')
	elif i%3 ==0: print('Fizz')
	elif i%5 ==0: print('Buzz')
	else: print(i)
