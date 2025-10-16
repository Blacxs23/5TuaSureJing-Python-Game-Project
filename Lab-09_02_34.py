#Thitiwat Sungkhao
#6809700039
#34

integar1,integer2 = map(int,input().split()) #input data
for a in range(integar1,integer2+1): #get a base
    for i in range(1,13): # make multiply 1 to 12
        answer = a * i #answer of multiply
        print(f"{a} * {i} = {answer}") #output multi
        if i == 12: # make a line between
            print("......................")