#Thitiwat Sungkhao
#6809700039
#34

base = str(input()) #input string
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # make string to compare
digit = "1234567890" # make string to compare 
answer1 = "" #make string. variable
answer2 = ""#make string variable
for i in base: # loop string in base
    if i in alphabet: # if i is alphabet 
        answer1 += i #add that character to answer1 variable
    elif i in digit: # if i is digit
        answer2 += i # add that character to answer2 variable    
print(f"Alphabet: {answer1}\nDecimal digit: {answer2}") #output result