# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
# from model import find,remove

class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, width=10, height=10)
        
        
    def __contains__(self,xy):
        return self.distance( xy ) < self.radius 
        
    def update(self,model):
        edible = model.find(lambda s: isinstance(s, Prey))
        EATEN = [s for s in edible if (s._x , s._y ) in self and s is not self]
        for s in EATEN:
            model.remove(s)
        return EATEN
                
    def display(self,canvas): #The object is displayed as a ball 
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                           self._x+self.radius, self._y+self.radius,
                                fill= "black")
