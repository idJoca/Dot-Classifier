import perceptron
import random
import training
import time
from graphics import *

height = 400
width = 400   
global neuron
global points
global guesses_points    
cir2 = []
old_weights = [0, 0, 0]

#SETUP
points = []
guesses_points = []
neuron = perceptron.perceptron(3) 
random.seed(None, 2)
win = GraphWin('Expected results', width, height) # give title and dimensions  

global win2
win2 = GraphWin('Actual results', width, height) # give title and dimensions 
p1 = training.Points(width, height, -1, training.Points.f(-1))
p2 = training.Points(width, height, 1, training.Points.f(1))    
line = Line(Point(p1.pixelX(), p1.pixelY()), Point(p2.pixelX(), p2.pixelY()))      
line.draw(win)    

p1 = training.Points(width, height, -1, neuron.guessY(-1))
p2 = training.Points(width, height, 1, neuron.guessY(1)) 
line2 = Line(Point(p1.pixelX(), p1.pixelY()), Point(p2.pixelX(), p2.pixelY())) 
line2.draw(win2)

for i in range(0, 99):
    point = training.Points(width, height)
    points.append(point)
guesses_points = points
for i in range(0, len(points)):        
    cir = points[i].show()
    cir.draw(win)
    result = neuron.train((points[i].x, points[i].y, 1), points[i].value)
    cir2.append(guesses_points[i].evaluate(result))
    cir2[i].draw(win2)   

  

#LOOP
while(True): 
    win2.getMouse()
    line2.undraw()
    for i in range(0, len(points)): 
        result = neuron.train((points[i].x, points[i].y, 1), points[i].value)
        cir2[i].undraw()        
        cir2[i] = guesses_points[i].evaluate(result)
        cir2[i].draw(win2)        
        line2.undraw()
        p1 = training.Points(width, height, -1, neuron.guessY(-1))
        p2 = training.Points(width, height, 1, neuron.guessY(1))    
        line2 = Line(Point(p1.pixelX(), p1.pixelY()), Point(p2.pixelX(), p2.pixelY())) 
        line2.draw(win2) 
    print(neuron.weights)
