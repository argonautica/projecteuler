import itertools
o = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a_list = [1, 2, 3]

sorted = list(itertools.permutations(o))
nums = []
for list in sorted:
    temp = ""
    for i in list:
        temp += str(i)
    nums.append(temp)
print(nums[999999])