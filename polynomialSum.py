s=0
print("Enter n:",end=" ")
n=int(input())
print("Enter x:",end=" ")
f=int(input())
x=f

for i in range(1,n+1):
    print("Enter the coefficient a{}:".format(i),end=" ")
    a=int(input())
    s=s+(a*x)
    x=x*f

print("\nSum: {}".format(s))