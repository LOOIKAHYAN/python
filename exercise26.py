def histogram(list):
    for n in list:
        output = ""
        times = n
        count = 0
        while count < times:
            output += "&"
            count += 1
        print(output)

histogram([1,2,3,4,9])