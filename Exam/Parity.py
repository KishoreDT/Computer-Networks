a=int(input("Enter a number:"))
binary=bin(a)
print(binary)
count=0
for i in binary:
    if i == '1':
      count+=1
if count %2 == 0:
     print("Even Parity")
else:
    print("Odd Parity")