# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
import random
import math 

class Ball(Prey): 
    radius = 5 # used in this class only; never changes
    _color = 'blue'
    def __init__(self,x,y):
        def random_angle():
            # between 0 and 2pi
            return random.random()*math.pi*2
        Prey.__init__(self,x = x,y = y,
                      width=5,height= 5,angle = random_angle(),speed = 5)
        
    def update(self,model):
        self.move()
        self.wall_bounce() #model as a nonlocal param
    
    def display(self,canvas): #The object is displayed as a ball 
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                           self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
