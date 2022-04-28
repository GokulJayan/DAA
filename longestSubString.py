def LCSubString(s1, s2, l1, l2):
 
    maxLen = 0           
    end = l1         
 
    L = [[0 for x in range(l2 + 1)] for y in range(l1 + 1)]
 
    for i in range(l1):
        for j in range(l2):
            
            if s1[i] == s2[j]:
                L[i+1][j+1] = 1 + L[i][j]

                if L[i+1][j+1] > maxLen:
                    maxLen = L[i+1][j+1]
                    end = i+1
                    
    #Matrix Printing
    for i in range(l1+1):
        for j in range(l2+1):
            print(L[i][j], end=" ")
        print()
    
    
                    
    return s1[end - maxLen: end]
 

# print("Enter String-1:",end=" ")
# X=input()
# print("Enter String-2:",end=" ")
# Y=input() 
X = 'student'
Y = 'dentist'
# X = 'abcde'
# Y = 'cfbcd'
print("S1:",X)
print("S2:",Y)
print()
print('\nLongest common substring: ', LCSubString(X, Y, len(X), len(Y)))