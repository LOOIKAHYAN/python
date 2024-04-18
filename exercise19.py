
def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        print(str)
    else:
        print("Is "+str)

new_string("Hello")
new_string("iss is is kahyan")