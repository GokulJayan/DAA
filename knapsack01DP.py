def knapSack(W, wt, val, n):
    K = [[0]*(W + 1) for x in range(n + 1)]   # K[n+1][W+1]
   
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1])
            else:
                K[i][j] = K[i-1][j]
    
    for i in range(n+1):
        for j in range(W+1):
            print(K[i][j],end=" ")
        print()
    return K[n][W]
  
  
wt = [5,5,4,5,1]
val = [4,1,2,1,3] #Profit

W = 6 #Capacity
n = len(val)
print(knapSack(W, wt, val, n))