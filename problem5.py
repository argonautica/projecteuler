def getNum():
    temp = 0
    while True:
        for i in range(20):
            if(temp % i != 0):
                temp += 1
                break
    return     