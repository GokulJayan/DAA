def search(pattern, text, d, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    count=0

    for i in range(m-1):
        h = (h*d) % q

    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    #print("Hash Value of Pattern: ",p)
    #print("Hash Value of Text   : ",t)

    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j != m:
                count+=1

        if(i<n-m):
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            #if t < 0:
             #   t = t+q
    print ("\nNo:of Spurious Hit:",end=" ")
    print(count)
    
# text = "ABCCDDAEFG"
# pattern = "CDD"
text = "2359023141526739921"
pattern = "31415"
q = 13
d=10
search(pattern, text, d, q)