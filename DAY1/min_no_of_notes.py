N=int(input("Enter  a n0:"))
c100=N//100
N=N%100
c50=N//50
N=N%50
c20=N//20
N=N%20
c10=N//10
N=N%10
c2=N//2
N=N%2
notes=c100+c50+c20+c10+c2
print("Total no of notes:",notes)