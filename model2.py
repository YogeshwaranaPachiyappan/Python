t=int(input())
for q in range(t):
    s=input()
    tr=''
    e=0
    tra=0
    trb=0
    for x in s:
        if(x=='A'):
            if(tr=='A'):
                tra+=e
            tra+=1
            tr='A'
            e=0
        if(x=='B'):
            if(tr=='B'):
                trb+=e
                e=0
            trb+=1
            tr='B'
            e=0
        if(x=='.'):
            e+=1
    print(tra,trb,sep=' ')
