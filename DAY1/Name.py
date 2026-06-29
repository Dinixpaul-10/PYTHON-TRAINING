name=input("enter the string : ")
mid=len(name)//2
firstpart=name[:mid]
secondpart=name[mid:]
#reverse
revfirstpart=firstpart[::-1]
revsecondpart=secondpart[::-1]
result=revfirstpart+revsecondpart
print(result)