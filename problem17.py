from num2words import num2words

n2w = num2words
sum = 0
for i in range(1, 1001):
    temp = n2w(i).replace('-', "").replace(" ", "")
    sum += len(temp)
print(sum)