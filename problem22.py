names = open("files/names.txt", 'r')
name = names.readline().replace("\"", "").replace(",", " ")
list = name.split(' ')
list = sorted(list)
chars = [chr(i) for i in range(ord('a'),ord('z')+1)]
nums = [i for i in range(1,27)]
map = {a: b for a, b in zip(chars, nums)}

def split(word):
    return [char for char in word]

total = 0

for i in range(len(list)):
    temp = 0
    for a in split(list[i].lower()):
        temp += map[a]
    total += (i+1) * temp

print(total)