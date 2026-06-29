n=int(input())
cnt=1
for i in range(1,n+1):
    for j in range (i):
        print(chr(65+j),end=" ")
        cnt=cnt+1
    print()