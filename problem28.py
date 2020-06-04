depth = 1
count = 1
pos = 1
while depth < 501:
    for i in range(4):
        pos += 2 * depth
        count += pos
        print("the count is " + str(count))
    depth += 1
print(count)