#Thitiwat Sungkhao
#6809700039
#34

base = str(input("Enter a positive integer : "))#input integer
answer = 0 #create variable to add value 
for i in base: #loop base string 
    answer += int(i) #change i(base) to integer and add that value to answer variable
print(f"The sum of the digits was {answer}") #output the result