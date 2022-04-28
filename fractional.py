def fractionalKS(W, wt, val, n):
    F=[val[i]/wt[i] for i in range(n)]
    K = [0]*n
    total_w=0
    P=[]
    maxProfit=max(F)
    if total_w+wt[F.index(maxProfit)]<=W:
        total_w+=wt[F.index(maxProfit)]
        P.append(val[F.index(maxProfit)])
        prev=wt[F.index(maxProfit)]
        for i in range(1,n):
            if(total_w<W):
                if wt[i]+total_w<=W:
                    total_w+=wt[i]
                else:
                    f=(W-prev)/wt[i]
                    P.append(f*val[i])
                    total_w+=wt[i]
    return (sum(P))
            
    
val = [7,9,6,1]
wt = [3,5,4,1] #Profit

W = 5 #Capacity
n = len(val)
print(fractionalKS(W, wt, val, n))