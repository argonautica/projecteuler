temp = []
for i in range(20000001):
    temp.append(i)

for i in range(3, 1999999):
    if temp[i] % 2 == 0:
        temp[i] = 0
a = 0
for i in range(5, 1999999):
    if a ==5:
        a=0
        temp[i] = 0
    else:
        a += 1
a = 0
for i in range(3, 1999999):
    if a ==3:
        a=0
        temp[i] = 0
    else:
        a += 1


l = 0
for nums in temp:
    l += nums
print(l)