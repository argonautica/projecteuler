def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes



num = 600851475143
primes = get_primes(100000)
num = 2
for i in primes:
    if ( num % i == 0 ):
        num = i
print(num)
