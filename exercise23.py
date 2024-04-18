def new_string(str,n):
    if len(str) < 2:
        print(str)
    else:
        newstr = ""
        for i in range(n):
            str = str[:2]
            newstr = newstr+str
        print(newstr)

new_string("a",2)
new_string("ab",2)