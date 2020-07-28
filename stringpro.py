S=input()
lst=[]
lst1=[]
for i in range(len(S)):
    lst.append(S[i:])
for i in lst:
    if(len(i)>=2):
        if(i==i[::-1]):
            lst1.append(i)
print(max(lst1))

