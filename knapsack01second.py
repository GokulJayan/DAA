# def knapSack(W, wt, val, n):
      
#     if n == 0 or W == 0 :
#         return 0

#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)

#     else:
#         return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
#                    knapSack(W, wt, val, n-1))
  

def knapSack(values, weights, cap, n):
    
    knapsack = []
    Weight = 0

    while(True):
        best = max(values)
        i = values.index(best)

        if Weight + weights[i] > cap:
            break

        knapsack.append(i)
        Weight = Weight + weights[i]

        del values[i]
        del weights[i]

    return knapsack, Weight

values = [4, 3, 2, 1]
weights  = [5, 1, 4, 5]
cap = 5
n = len(values)
print(knapSack(values, weights, cap, n))