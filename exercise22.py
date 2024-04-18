list = [1,2,3,4,56,7,67,4,18201,1,2,3,4]
def getcount(list):
    count = 0
    for item in list:
        if item == 4:
            count = count + 1

    return count

print(getcount(list))