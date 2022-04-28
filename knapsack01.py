maxW = 6    #Max Weight
W = [5,5,4,5,1]
P = [4,1,2,1,3]
LP = []
LW = []

S=0
totalW=0
i=0

for i in range(len(W)):
    if(totalW+W[i]<=maxW):
        S+=P[i]
        totalW+=W[i]
        LW.append(W[i])
        LP.append(P[i])

print("Weight:",LW)
print("Profit:",LP)
print("\nSum:",S);