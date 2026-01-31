#14fibonacci.py Chris Park

prev_one = 1
prev_two = -1
for i in range(10
):
	fib = prev_one + prev_two
	print(fib)
	prev_two = prev_one
	prev_one = fib

