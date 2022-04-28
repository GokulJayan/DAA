A  = [ 2.00, 2.10, 3.00, 3.20, 3.50, 5.00 ]
D  = [ 2.30, 3.40, 3.20, 4.30, 4.00, 5.20 ]

n=6
noOfPlatforms=1
maxcount=1

for i in range(n-1):
    noOfPlatforms=1
    for j in range(i+1,n):
        if((A[i]>=A[j] and A[i]<=D[j]) or (A[i]<=A[j] and D[i]>=A[j])):
            noOfPlatforms+=1
    print(noOfPlatforms)
    maxcount=max(maxcount,noOfPlatforms)

print("Max:",maxcount)