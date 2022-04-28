def findNoOfPlatforms(A,D,n): 
    noOfPlatforms=1 
    maxcount=1
    i=1
    j=0

    while(i<n and j<n):
        if(A[i]<=D[j]):
            noOfPlatforms+=1
            i+=1
        elif(A[i]>D[j]):
            noOfPlatforms-=1
            j+=1
    
        if(noOfPlatforms>maxcount):
            maxcount=noOfPlatforms

    return maxcount



n=int(input())
A=[float(input()) for i in range(n)] #Arrival
D=[float(input()) for i in range(n)] #Departure
print(findNoOfPlatforms(A,D,n))