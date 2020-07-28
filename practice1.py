n=int(input())
a="B"
x=a.center(n,'*')
for i in range (0,n):
    for j in range (0,i+1):
        print(x,end='  ')
    print("\n")
