n=int(input())
m=[int(n) for n in input().split()]
m=list(dict.fromkeys(m))
print(sum(m)/len(m))
