total = []
for i in range(2, 101):
    for j in range(2, 101):
        total.append(i**j)
final = list(set(total))
total.sort()
print(total)

# 618 duplicates