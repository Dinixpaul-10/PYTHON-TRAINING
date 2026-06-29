un=int(input("enter units:"))
if 0<un<=100:
    cost=un*1.50
elif 100<un<=200:
    cost=(100*1.50)+(2.50*(un-100))
elif un>200:
    cost=(100*1.50)+(100*2.50)+(4*(un-200))
else:
    print("error")
print(cost)