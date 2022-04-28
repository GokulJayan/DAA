def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)


def sin(x,beg,end):
    if(beg>end):
        return 0
    if(beg==end):
        return (-1 if (beg%2==0) else 1)*((pow(x,2*beg-1)*1.0)/fact(2*beg-1))
    mid=(beg+end)//2
    return sin(x,beg,mid)+sin(x,mid+1,end)

n=int(input())
x=float(input())

print(sin(x,1,n))

