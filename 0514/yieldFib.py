def fib(max):
	a, b, c = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1


print fib(6)

