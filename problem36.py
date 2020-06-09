

def isPalindrome(str):
  temp = str[::-1]
  if temp == str:
    return True
  return False
temp = 0
for i in range(1, 1000001):
  if isPalindrome(str(i)):
    if isPalindrome(str('{0:08b}'.format(i))):
      temp += i

print(temp)
