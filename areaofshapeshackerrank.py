import math
import os
import random
import re
import sys
class Shapes():
    def area(self):
        self.l=int(input())
        self.w=int(input())
        self.r=int(input())
class Rectangle(Shapes):
    def area_of_Rectamgle(self):
        print(self.l*self.w)
class Circle(Rectangle):
    def area_of_Circle(self):
        print(math.pi*self.r)
o=Shapes()
o=Rectangle()
o=Circle()
o.area()
o.area_of_Rectamgle()
o.area_of_Circle()
