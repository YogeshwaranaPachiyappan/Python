from itertools import groupby
for k,c in groupby(input()):
    print(list(c),int(k))
