def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def mul(x,y):
    return x*y


def div(x,y):
    if y==0:
        return "Number 2 can't be 0"
    
    return x/y

num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))

print("Sum = ",add(num1,num2))
print("Difference = ",sub(num1,num2))
print("Product = ",mul(num1,num2))
print("Quotient = ",div(num1,num2))


    