# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
import random
import math 
from prey import Prey

class Floater(Prey): 
    radius = 5 # used in this class only; never changes
    _color = 'red'
    def __init__(self,x,y):
        self.ufo_img = PhotoImage(file='ufo.gif')#'achai.png'
        def random_angle():
            # between 0 and 2pi
            return random.random()*math.pi*2
        Prey.__init__(self,x = x,y = y,
                      width=self.ufo_img.width(),height= self.ufo_img.height(),
                      angle = random_angle(),speed = 5)
        
    def update(self,model):
        temp = random.random()
        if temp < 0.3: #Change
            self._speed = self._speed+ random.uniform(-0.5, 0.5)
            if self._speed < 3:
                self._speed = 3
            elif self._speed > 7:
                self._speed = 7
            #Change angle 
            self._angle += random.uniform(-0.5, 0.5)
        self.move()
    
    # def display(self,canvas): #The object is displayed as a ball 
        # canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                           # self._x+Floater.radius, self._y+Floater.radius,
                                # fill=self._color)
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self.ufo_img)
