#Thitiwat Sungkhao
#6809700039
#34

base = str(input())
special_character = "!@#$%^&*()_-=+ \"';:,."
answer = ""
activate_upper = False 

for i in base:
    if i in special_character:
        activate_upper = True
        continue
    if activate_upper is True:
        answer += i.upper()
        activate_upper = False
    else:
        answer += i.lower()
print(answer[0].lower() + answer[1:])