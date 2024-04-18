def getsum(n1,n2):
    sum = n1 + n2
    if sum >= 15 and sum <= 20:
        return 20
    else:
        return sum

print(getsum(12,1))
print(getsum(12,6))