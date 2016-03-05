def false_recursion(n, val):
	if n == 1:
		return val
	return false_recursion(n-1,  n * val)

print false_recursion(5, 1)

