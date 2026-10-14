def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

num= int(input("Enter the number : "))
ans=factorial(num) 
print(ans)