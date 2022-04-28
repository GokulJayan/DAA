def pascal(n):
    l1=[1]
    l2=[0]
    for i in range(n):
        print('   '*(n-i-1),end='')
        for j in l1:
            print(j,end=' '*(n))
        print()
        l3=[i for i in l1+l2]
        l1=[l3[i]+l3[i-1] for i in range(len(l3))]
        
N=int(input())
pascal(N)

            
    
