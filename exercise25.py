def checkExists(group_values, n):
    for num in group_values:
        if n == num:
            return True
    return False

print(checkExists([1,2,3,4],13))