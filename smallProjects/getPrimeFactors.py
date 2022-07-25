
def getPrimeFactors(num):
	primes = []
	i = 2
	while i <= num:
		if(num % i) == 0:
			num = num // i
			primes.append(i)
		else:
			i += 1
	return primes

print(getPrimeFactors(13))
