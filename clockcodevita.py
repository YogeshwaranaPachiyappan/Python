t=int(input())
a=float(input())
x=((t/360)*a)
h,m=divmod(x,1)
hour=int(h)
minutes=int(m*60)
angle = abs(30 * (hour % 12) - 5.5 * minutes)
g=min(angle, 360 - angle)
print('%.2f'%g)
