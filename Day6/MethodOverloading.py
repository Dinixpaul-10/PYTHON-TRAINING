class Demo:
    #def add(self,a):
        #print(a)
    #def add(self,a,b):
        #print(a+b)
    def add(self,*numbers):
        print(sum(numbers))

obj=Demo()
obj.add(8,9,9,0)
obj.add(10)
obj.add(10,5)

