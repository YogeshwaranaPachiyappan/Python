pi=3.142
class shapes():
    def area(self):
        self.a=int(input())
        self.b=int(input())
        self.h=int(input())
        self.l=int(input())
        self.w=int(input())
class circle(shapes):
    def area_of_circle(self):
        print("The area of circle:",pi*(self.a*self.a))
class rectangle(circle):
    def area_of_rectangle(self):
        print("The area of rectangle:",self.l*self.w)
class trapezoid(rectangle):
    def area_of_trapezoid(self):
        print("The area of trapezoid:",((self.a+self.b)/2)*self.h)
o=shapes()
o=circle()
o=rectangle()
o=trapezoid()
o.area()
o.area_of_circle()
o.area_of_rectangle()
o.area_of_trapezoid()



