#Thitiwat Sungkhao
#6809700039
#34

base = str(input())
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "1234567890"
answer1 = ""
answer2 = ""
for i in base:
    if i in alphabet:
        answer1 += i
    elif i in digit:
        answer2 += i    
print(f"Alphabet: {answer1}\nDecimal digit: {answer2}")