nums=[3,2,3]
count=0
candidate=0
for num in nums:
    if count==0:
        candidate=num
    if num==candidate:
        count=count+1
    else:
        count=count-1
print(candidate)                
