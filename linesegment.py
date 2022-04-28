x1,y1,x2,y2=input().split()
x,y=input().split()
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
x=int(x)
y=int(y)

cross=((x2-x1)*(y-y1)) - ((x-x1)*(y2-y1))

if(x1<x2):
    left=x1
    right=x2
else:
    left=x2
    right=x1

if(cross==0 and (left<=x and x<=right)):
    print("yes")
else:
    print("no")