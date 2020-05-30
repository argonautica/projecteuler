temp = 1
for i in range(1, 101):
    temp *= i
digits = [int(char) for char in str(temp)]
sum = 0
for a in digits:
    sum += int(a)
print(sum)