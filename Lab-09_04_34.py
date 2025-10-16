#Thitiwat Sungkhao
#6809700039
#34

base = str(input()) #input String
special_character = "!@#$%^&*()_-=+ \"';:,." # make a special character to compare
answer = "" # make a string in answer variable
activate_upper = False  #this boolean is activate whan found a special character

for i in base: # loop base string variable
    if i in special_character: # if found special character activate a upper function and continue to next string
        activate_upper = True # make this function true(avialable)
        continue #continue to next string
    if activate_upper is True: # if function activating
        answer += i.upper() # make character after special character to upper and add that character to answer varialble
        activate_upper = False # turn off function
    else: #if not enter if above
        answer += i.lower() #add lower character to answer
print(answer[0].lower() + answer[1:]) # output first character is always lower and print next character untill end