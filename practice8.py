ip=int(input())
for i in range(0,ip):
    ip1=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=sorted(a)
    b=sorted(b)
    c1=0
    while len(a)>0:
        if a[0]>b[0]:
            c1=c1+1
            a.remove(a[0])
            b.remove(b[0])
        else:
            b.remove(b[0])
print(c1)
