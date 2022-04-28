def matrixProduct(A,B):
    m1=len(A)
    n1=len(A[0])
    m2=len(B)
    n2=len(B[0]) 
    C = [[0]*n2 for i in range(m1)]
    
    for i in range(0,m1):
        for j in range(0,n2):
            sum=0;
            for k in range(m2):
                sum+=A[i][k]*B[k][j]
            C[i][j]=sum;
    return C

print("Enter row size of Matrix-1: ",end="")
m1=int(input())
print("Enter col size of Matrix-1: ",end="")
n1=int(input())
print("Enter row size of Matrix-2: ",end="")
m2=int(input())
print("Enter col size of Matrix-2: ",end="")
n2=int(input())

if(n1==m2):
    A = [[0]*n1 for i in range(m1)]
    B = [[0]*n2 for i in range(m2)]
    print("Enter ",m1,"x",n1," Matrix-1 elements: ")
    for i in range(0,m1):
        for j in range (0,n1):
            A[i][j]=int(input())
    print()
    print("Enter ",m2,"x",n2," Matrix-2 elements: ")
    for i in range(0,m2):
        for j in range (0,n2):
            B[i][j]=int(input())
    print()
    print("Matrix-1 elements: ")
    for i in range(0,m1):
        for j in range(0,n1):
            print(A[i][j],end=" ")
        print()
    print()
    print("Matrix-2 elements: ")        
    for i in range(0,m2):
        for j in range (0,n2):
            print(B[i][j],end=" ")
        print()
    print()
    print("Matrix Product: ")   
    C=matrixProduct(A,B)
    for i in range(0,m1):
        for j in range (0,n2):
            print(C[i][j],end=" ")
        print()


else:
    print("Multiplication isn't possible")