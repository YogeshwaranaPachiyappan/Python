from collections import OrderedDict
a=input()
n=int(input())
for i in range(0,len(a),n):
    x=a[i:i+3]
    print("".join(OrderedDict.fromkeys(x)))
