n1,n2=input().split(',')
k1=len(n1)
k2=len(n2)
s=''
if k1>k2:
    for i in range(k2):
        s=s+n1[i]
        s=s+n2[i]
else:
    for i in range(k1):
        s=s+n1[i]
        s=s+n2[i]
print(s)
        
