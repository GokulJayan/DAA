v=int(input())
A=[]
D=[]
flag=0

for i in range(v):
    a=list(map(int,input().split()))
    A.append(a)

for i in range(v):
    c=0
    for j in range(v):
       if (A[i][j]==1):
           c+=1
    if c==0:
        flag=1

if(flag==1):
    print(-1)
else:
    print(1)