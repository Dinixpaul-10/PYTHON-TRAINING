n=list(map(int,input("Enter nums : ").split()))
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even : ",even)
print("Odd : ",odd)            