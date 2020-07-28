t=int(input())
for i in range(t):
    n=int(input())
    g=list(map(int,input().split()))[:n]
    o=list(map(int,input().split()))[:n]
    g=sorted(g)
    o=sorted(o)
    j=0
    k=0
    count=0
    flag=0
    while j<n:
        k=0
        flag=0
        while k<n:
            if(g[j]>o[k]):
                count+=1
                g.pop(j)
                o.pop(k)
                n-=1
                flag=1
                break
            else:
                k+=1
        if(flag!=1):
            j+=1
    print(count)
    g.clear()
    o.clear()
