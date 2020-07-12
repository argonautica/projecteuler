def sieve(limit):
	temp = range(limit)
	
	for i in range(3, limit):
		if temp[i] % 2 == 0:
			temp[i] == 0
	for i in range(4, limit):
		if temp[i] % 3 == 0:
			temp[i] == 0 
	for i in range(6, limit):
		if temp[i] % 5 == 0:
			temp[i] == 0
	
	final = []
	for a in temp: 
		if a != 0:
			final.append(a)
	print(final)
			



sieve(20)
