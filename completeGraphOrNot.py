v=int(input())
A=[]
D=[]

for i in range(v):
    a=list(map(int,input().split()))
    A.append(a)

d=0

for i in range(v):
    c=0
    for j in range(v):
        if(i==j and A[i][j]==0):
            d+=1
        elif(A[i][j]==1):
            d+=1
            c+=1
    D.append(c)

if(d==v*v):
    print("yes")
else:
    print("no")

for i in D:
    print(i,end=" ")