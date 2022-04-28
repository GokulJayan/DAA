def InsSort(A,B,n):
    for i in range(1,n):
        key1=A[i]
        key2=B[i]
        j=i-1
        
        while(A[j]>key1 and j>=0):
            A[j+1]=A[j]
            B[j+1]=B[j]
            j-=1
        A[j+1]=key1
        B[j+1]=key2


n=int(input())
L=[int(input()) for i in range(n)]
flag=1

for i in range(1,len(L)):
    if(L[i]==L[0]):
        flag+=1

if(flag==n):
    print(0)
    print(1)
    print(L[0])
    print(L[1])
    exit()
    
D=[]
pairs=[]
dist=[]
distpairs=[]

for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        if(L[i]<L[j]):
            D.append(L[j]-L[i])
            pairs.append((L[i],L[j]))
        else:
            D.append(L[i]-L[j])
            pairs.append((L[j],L[i]))
            
for i in range(len(D)-1):
    for j in range(i+1,len(D)):
        if(D[i]==D[j]):
            dist.append(D[i])
            distpairs.append([pairs[i],pairs[j]])

InsSort(dist,distpairs,len(dist))


for i in range(len(dist)):
    print(dist[i])
    print(len(distpairs[i]))
    for j in range(len(distpairs[i])):
        print(distpairs[i][j][0])
        print(distpairs[i][j][1])