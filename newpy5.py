a=input()
n=int(input())
at=a.split()
c=0

for i in range (len(at)):
    if at[i]=='he':
        c=c+1
        if n==c:
            at[i]='john'

print(listToString(at))





