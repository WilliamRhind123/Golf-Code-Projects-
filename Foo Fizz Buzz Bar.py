for i in range(1,1001):
	if i%2 == 0:
		print("Foo", end = "")
	if i%3 == 0:
		print("Fizz", end = "")
	if i%5 == 0:
		print("Buzz", end = "")
	if i%7 == 0:
		print("Bar", end = "")
	if i%7 > 0 and i%5 > 0 and i%3 > 0 and i%2 > 0:
		print(i)
	else:
		print("")