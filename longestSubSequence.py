def LCS(S1, S2, l1, l2):
    
    L = [[0 for x in range(l2+1)] for x in range(l1+1)]

    for i in range(l1):
        for j in range(l2):
            if S1[i] == S2[j]:
                L[i+1][j+1] = L[i][j] + 1
            else:
                L[i+1][j+1] = max(L[i][j+1], L[i+1][j])  #Top Adjascent: L[i][j+1]   Left Adjascent: L[i+1][j] 
                
    #Matrix Printing
    for i in range(l1+1):
        for j in range(l2+1):
            print(L[i][j], end=" ")
        print()

    sequence = []

    i = l1
    j = l2
    
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            sequence.append(S1[i-1])
            i -= 1
            j -= 1

        elif L[i-1][j] > L[i][j-1]:    #Top Adjascent: L[i-1][j]   Left Adjascent: L[i][j-1] 
            i -= 1
        else:
            j -= 1
            
            
    print("\nS1 : " + S1 + "\nS2 : " + S2)
    
    sequence.reverse()
    print("\nLongest Common Subsequence: " + "".join(sequence))


# S1 = "gestures"
# S2 = "tangesedptures"
S1="BCDAACD"
S2="ACDBAC"
m = len(S1)
n = len(S2)
LCS(S1, S2, m, n)