n=int(input("Enter a number: "))
square=n*n
digits=len(str(n))
right=square%(10**digits)
left=square//(10**digits)

if left+right==n:
    print("Keprekar number")
else:
    print("Not Keprekar")    