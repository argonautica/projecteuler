def getLength(a):
    temp = 1
    while a != 1:
        temp += 1
        if a%2 == 0:
            a = a/2
        else:
            a = 3 * a + 1
    return temp


temp = 0
for i in range(1,1000001):
    cur = getLength(i)
    if cur > temp:
        temp = cur
        print(i)
print(temp)