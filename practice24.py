n=int(input())
a={int(i) for i in input().split()}
m=int(input())
b={int(j) for j in input().split()}
x=a.difference(b)
t=list(x)
print(t)
y=b.difference(a)
u=list(y)
print(u)



