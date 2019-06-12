import random
from graphics import *

class Points():
    point = None
    cir = None
    x = 0
    y = 0
    width = 0
    height = 0
    value = 0

    def __init__(self, width, height, x=0, y=0):        
        self.width = width
        self.height = height 
        if (x == 0 and y == 0):       
            random.seed(None, 2)          
            self.x = random.uniform(-1, 1)
            self.y = random.uniform(-1, 1)       
            if(Points.f(self.x) > self.y):
                self.value = 1
            else:
                self.value = -1
        else:               
            self.x = x
            self.y = y
 

    def f(x):
        #y = mx + b
        return 0.7 * x + -1

    def show(self):  
        self.point = Point(self.pixelX(), self.pixelY())    
        cir = Circle(self.point, 3)
        if(self.value > 0):
            cir.setFill('black')
        else:
            cir.setFill('white')
        return cir
    
    def pixelX(self):
        return self.mapping(self.x, -1, 1, 0, self.width)

    def pixelY(self):
        return self.mapping(self.y, -1, 1, self.height, 0)

    def evaluate(self, value):
        self.point = Point(self.pixelX(), self.pixelY())  
        self.cir = Circle(self.point, 3)
        if(value > 0):
            self.cir.setFill('black')
        else:
            self.cir.setFill('white')
        return self.cir

    def mapping(self, x, x0, x1, y0, y1):        
        return ((x-x0)/(x0-x1) * (y1-y0) + y1)