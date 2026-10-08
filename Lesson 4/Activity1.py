num=1
while (num<11):
    print(num)
    num=num+1

num1=int(input("Enter the number : "))
isprime=True
for i in range(2,num1):
    if num1%i==0:
        isprime=False
        print("Not Prime")
        break

if isprime==True:
    print("Prime")




n=int(input("Enter a number : "))

for i in range(1,n+1):
    for j in range(1,i):
        print(j)
    print()