def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2),1,-1):
        if x % k == 0 and y %k == 0:
            gcd = k
            break
    return gcd

print(gcd(12,12))
print(gcd(69,94))