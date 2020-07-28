a=input()
n=list(a)
list1=[]
lst=[]
lst2=[]
alpha='a'
a=1
for i in range(0,26):
    list1.append(alpha)
    alpha=chr(ord(alpha)+1)
for j in n:
    if j in list1:
        b=list1.index(j)+1
        lst.append(b)
for k in range(len(lst)-1,-1,-1):
    if(k==len(lst)-1):
        lst2.append(str(lst[k]))
    else:
        lst[k]=lst[k]+a
        a=a+1
        lst2.append(str(lst[k]))
print("".join(lst2))

