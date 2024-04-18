def getans(n1,n2):
    if n1 == n2 or abs(n1-n2) == 5 or n1+n2 == 5:
        return True
    else:
        return False

print(getans(9,9))
print(getans(12,7))
print(getans(7,12))
print(getans(2,3))
print(getans(12,123))