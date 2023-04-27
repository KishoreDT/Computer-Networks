l=[]
s=0
for i in range(0,4):
    n=int(input("Enter a number :"))
    l.append(n)
for i in range(0,4):
    s+=l[i]
b=bin(s)
print(s,b)
l.append(15-s)
r=0
for i in range(0,5):
    r+=l[i]
if bin(r)==bin(15):
    print("Code Recived Sucesuffully")