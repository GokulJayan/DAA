def Binomial(n,r):
    L=[[0 for i in range(r+1)] for i in range(n+1)]   
    
    for i in range(n+1):
        for j in range(r+1):
            if(j==0 or i==j):
                L[i][j]=1
            else:
                L[i][j]=L[i-1][j]+L[i-1][j-1]
    
    
    for i in range(n+1):
        for j in range(r+1):
            print(L[i][j], end=" ")
        print()           
    
    return L[n][r]


n=5
r=3
# n=int(input())
# k=int(input())
# Binomial(n,k)
print("\nnCr = ",str(n)+"C"+str(r),"=",Binomial(n,r))