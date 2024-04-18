def concat_into_str(list):
    newstr = ""
    for i in list:
        newstr = newstr + str(i)
    return newstr
print(concat_into_str([1,2,3,4,5,'agasj']))