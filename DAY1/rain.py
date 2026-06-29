n=int(input("Rain in mm : "))
if n<1:
    print("No Rain")
elif 1<=n<5:
    print("Light Rain")
elif 5<=n<10:
    print("Moderate Rain")
else:
    print("Heavy Rain")            