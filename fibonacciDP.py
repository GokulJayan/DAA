l=[]

def fib(n):
    if l[n]>0:
        return l[n]
    elif (n==1 or n==2):
        return n-1
    else:
        l[n]=fib(n-1)+fib(n-2)
        return l[n]

n=5
l=[0 for i in range(n+1)]
print(fib(n))