for _ in range(int(input())):
    s=input()
    a=0
    b=0
    a1=0
    b1=0
    for i in range(len(s)):
        if s[i]=='A':
            a+=1
            b1=0
            if a1==1:
                a+=count
            else:
                a1=1
            count=0
        elif s[i]=='B':
            b+=1
            a1=0
            if b1==1:
                b+=count
            else:
                b1=1
            count=0
        else:
            if a!=0 or b!=0:
                count+=1
    print(a,b)
