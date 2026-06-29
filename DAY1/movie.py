n=int(input("Tickets : "))
price=200
c=int(input("Category : "))
if c==0:
    if n>15:
        total=n*price-n*price*(20/100)
    else:
        total=n*price
else:
    if n>=15:
        total=n*price-n*price*(25/100)
    else:
        total=n*price-n*price*(5/100)
print("Total = ",total)        



