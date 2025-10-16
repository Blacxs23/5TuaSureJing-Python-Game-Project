#Thitiwat Sungkhao
#6809700039
#34

base = int(input("Enter a positive integer : ")) #input data
print(f"Factors of [{base}] are",end=" ") #print a text before answer
for i in range(1,base+1): #loop form 1 to base
    if base % i == 0: #. find a factors
        print(i,end=" ") #print factors