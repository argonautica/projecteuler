temp = "0"

for i in range(1,1000000):
  temp += str(i)

array = [char for char in temp ]
total = 1
for i in range(7):
  a = 10 ** i

  total *= int(array[a])

  a = 1
print(total)
