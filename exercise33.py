

def getsum(n1,n2,n3):
    if (n1 == n2 or n2 == n3 or n1 == n3):
        return (0)
    else:
        return (n1+n2+n3)

print(getsum(2,2,3))