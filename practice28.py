import collections, statistics
print('%.2f' % statistics.mean(next((int(student(*row).MARKS) for row in (input().split() for i in range(size))) for size, student in [[int(input()), collections.namedtuple('Student', input())]])))

#Input
#5
#ID         MARKS      NAME       CLASS     
#1          97         Raymond    7         
#2          50         Steven     4         
#3          91         Adrian     9         
#4          72         Stewart    5         
#5          80         Peter      6 
