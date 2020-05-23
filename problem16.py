num = 2 ** 1000
list = [char for char in str(num)]
sum= 0
for char in list:
    sum += int(char)
print(sum)