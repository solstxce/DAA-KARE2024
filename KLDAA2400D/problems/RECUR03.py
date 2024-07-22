def Factorial(n):
    # Write your code here
    if n==1 or n==0:
        return 1
    else:
        return n*Factorial(n-1)

n = int(input())
print(Factorial(n))
