#n=int(input("enter the no : "))
#items=[]
#for i in range(n):
    #name=input("Enter the name ")
    #value=int(input("Enter the value "))
    #items.append([name,value])
#sortby=input("Enter the sort type(key/price)")
#if sortby=="key":
 #       items.sort()
#else:
 #     items.sort(key=lambda x: x[1])
#print(items)              


#Another code
products=eval(input("Enter the dictionary : "))
choice=input("KEY/PRICE")
def get_value(item):
      return item[1]

if choice=='KEY':
      sorted_dic=dict(sorted(products.items()))
      print("Sorted Dictionary: ",sorted_dic)

elif choice=="PRICE":
      sorted_dic=dict(sorted(products.items(),key=get_value))
      print(sorted_dic)

else:
      print("Invalid Choice")      
