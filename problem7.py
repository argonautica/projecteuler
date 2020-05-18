def a(num):
    for i in range(1,20):
        if num%i !=0:
            return False
    print("yes")
    return True

def getNum():
    for i in range(1,20000000000):
        print(i)
        if a(i):
            print("HERE IT IS")
            return i
print("start")
print(getNum())
print("done")

