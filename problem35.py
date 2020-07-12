def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def getCircles(num):
  temp = []
  word = str(num)
  temp.append(num)
  for i in range(len(str(num))):
    word = word[1:]+word[0]
    if word != str(num):
      temp.append(int(word))
  return temp

def allPrime(arr):
  for j in arr:
    if not is_prime(j):
      return False
  return True

count = 0
for i in range(1000000):
  temp = getCircles(i)
  if allPrime(temp):
    count += 1
print(count)
