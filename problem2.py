num1 = 1
num2 = 2
count = 0
sum = 2
while (num1 < 4000000) and (num2 < 4000000):
    if(count % 2 ==0 ):
        print(2)
        num1 += num2
        count += 1
        if (num1 % 2 == 0 and num2 < 4000000):
            sum += num1
    else:
        num2 += num1

        count += 1
        if (num2 % 2 == 0 and num2 < 4000000):
            sum += num2
print(sum)

