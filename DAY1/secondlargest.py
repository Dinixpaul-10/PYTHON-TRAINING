a=int(input("a : "))
b=int(input("b : "))
c=int(input("c : "))
if a>b and a<c or a<b and a>c:
    n=a
elif b>a and b<c or b<a and b>c:
    n=b
else:
    n=c
print(n," is second largest")        