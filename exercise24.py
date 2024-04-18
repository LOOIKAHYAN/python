def checkVowel(char):
    if len(char) != 1:
        print("Insert one letter only")
    elif (char.lower() in 'aeiou'):
        print(char, "is vowel")
    else:
        print(char, "is not vowel")

checkVowel(input())