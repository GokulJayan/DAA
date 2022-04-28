def isSafe(i, j):
    for k in range(0,N):
        if A[i][k]==1 or A[k][j]==1:
            return True

    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if A[k][l]==1:
                    return True
    return False

def N_queen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(isSafe(i,j))) and (A[i][j]!=1):
                A[i][j] = 1
                if N_queen(n-1)==True:
                    return True
                A[i][j] = 0

    return False

print ("Enter the number of queens")
N = int(input())

A = [[0]*N for i in range(N)]

N_queen(N)
for i in A:
    print (i)