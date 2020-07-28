from itertools import permutations
n=input()
x=int(input())
y=permutations(n,x)
z=sorted(y)
for i in z:
    print(''.join(i))
print("\n")
