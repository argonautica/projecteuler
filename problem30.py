
nums = []
for i in range(2, 1000000):
    ints = [int(x) for x in str(i)]
    temp = 0
    for num in ints:
        temp += num ** 5
    if temp == i:
        nums.append(temp)

sum = 0
for i in nums:
    sum += i
print(sum)