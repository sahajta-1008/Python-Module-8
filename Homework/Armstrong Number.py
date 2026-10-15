num=int(input("Enter a number : "))
temp=num
sum=0   

while num>0:
    rem=num%10
    sum = sum + rem*rem*rem
    num=num//10

if sum==temp:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")