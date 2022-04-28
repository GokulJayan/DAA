def merge(arr, L, M, R):
    i = L
    j = M + 1
    k = L;
    temp=[0]*1000

    while (i <= M and j <= R):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            i+=1
        else:  
            temp[k] = arr[j]
            j+=1
        k+=1

    while (i <= M):
        temp[k] = arr[i]
        k+=1
        i+=1

    while (j <= R):
        temp[k] = arr[j]
        k+=1
        j+=1
        
    for k in range(L,R+1):
        arr[k] = temp[k];
 
 
def mergeSort(arr, L, R):
    if L < R:
        M = L+(R-L)//2
 
        mergeSort(arr, L, M)
        mergeSort(arr, M+1, R)
        merge(arr, L, M, R)
 

n=5
arr=[8,7,5,4,1]
mergeSort(arr, 0, n-1)

print("Sorted array:")
for i in range(n):
    print(arr[i],end=" ")