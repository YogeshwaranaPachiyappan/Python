m=int(input())
ta=0
tb=0
tc=0
for p in range(0,m):
    n=int(input())
    x=[int(i) for i in(input()).split()]
    y=[int(j) for j in(input()).split()]
    for q in range(len(x)):
        if(x[q]>y[q]):
            ta=ta+1
        elif(x[q]==y[q]):
            tc=tc+1
        else:
            tb=tb+1
    if(p%2!=0 or m==1):
        if(ta>tb):
            print("LOSE")
        elif(tb>ta):
            print("WIN")
        else:
            print("DRAW")
    elif(p%2==0):
        if(ta>tb):
            print("WIN")
        elif(tb>ta):
            print("LOSE")
        else:
            print("DRAW")
