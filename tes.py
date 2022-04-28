def merge(A,L,M,R):
    i=L
    j=M+1
    k=L
    temp=[0]*100
    
    while(i<=M and j<=R):
        if A[i]<=A[j]:
            temp[k]=A[i]
            i+=1
        else:
            temp[k]=A[j]
            j+=1
        k+=1
    
    while(i<=M):
        temp[k]=A[i]
        i+=1
        k+=1
        
    while(j<=R):
        temp[k]=A[j]
        j+=1
        k+=1
    
    for i in range(L,R+1):
        A[i]=temp[i]
    
    
def mergeSort(A,L,R):
    if L<R:
        M=L+(R-L)//2
        mergeSort(A,L,M)
        mergeSort(A,M+1,R)
        merge(A,L,M,R)
    



A=[9,3,1,6]
mergeSort(A,0,len(A)-1)
print(A)
