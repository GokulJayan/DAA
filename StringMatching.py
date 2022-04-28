T=input()
P=input()

for i in range(len(T)):
    index=-1
    flag=0
    if(T[i]==P[0]):
        for j in range(len(P)):
            if(i+j<len(T)):
                if(T[i+j]!=P[j]):
                    flag=1
        if flag==0:
            index=i
            break
if(index==-1):
    print("Invalid")
else:
    print(index)