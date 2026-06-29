a=int(input("a : "))
b=int(input("b : "))
c=int(input("c : "))
d=int(input("d : "))
if a>b and a>c and a>d:
    print(a," is the largest")
elif b>c and b>d:
    print(b," is the largest")
elif c>d:
    print(c," is the largest")
else:
    print(d," is the largest")            
   

