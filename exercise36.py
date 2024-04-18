def add_numbers(n1,n2):
    if isinstance(n1,int) and isinstance(n2,int):
        return (n1+n2)
    else:
        return "Inputs are not integers"

print(add_numbers(12,12))
print(add_numbers(12,12.199))