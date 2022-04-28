m1=int(input())
c1=int(input())
m2=int(input())
c2=int(input())

x=(c1-c2)/(m2-m1)
y=m1*x+c1

print("({:.2f}, {:.2f})".format(x,y))