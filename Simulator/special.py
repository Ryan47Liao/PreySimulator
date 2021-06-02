#The Special class is derived from Prey  
#The special is able to change its angel and speed to evade predators 
#When NOT in danger, it's going to Prey on other preys! 
#The color of the Special will represent its status
# Green: Dorminant/ Purple: Pursue Prey / Red: Evade Predator

from prey  import Prey
from blackhole import Black_Hole
from pulsator import Pulsator
from hunter import Hunter
from math import atan2
from simulton import Simulton

class Special(Prey,Hunter):
    colors = {'0':'green','1':'purple','2':'red'}
    perception = 100 
    
    def __init__(self,x,y):
        Prey.__init__(self,x = x,y = y,
                      width=5,height= 5,
                      angle = None,speed = 2)
        self.randomize_angle()
        self._color = 'green'
        self._CD = Pulsator.counter 
         
    def update(self, model):
        ALL_sims = Hunter.seen(self, model,\
                               predict = lambda s: isinstance(s, Simulton) )
        Preys = Hunter.seen(self, model,\
                               predict = lambda s: isinstance(s, Prey) )
        Predators = Hunter.seen(self, model,\
                               predict = lambda s: isinstance(s, Black_Hole ) )
            
        
        #Level 0: Dominant, no prey nor predator in sight 
        if len(ALL_sims) == 0 :
            self._speed = 2 
            self._color = 'green'
            Predator_mode = False
        #Level 1: Safe, only prey in sight
        if len(Preys) > 0:
            Predator_mode = True
            self._color = 'purple'
            self._speed = 6
        #Level 2: Danger, predator in sight 
        if len(Predators) > 0:
            Predator_mode = False
            self._color = 'red'
            target = min(Predators,key = lambda s: self.distance((s._x,s._y)))
            self._speed = min(20,400/self.distance((target._x,target._y)) )
            self.set_angle(atan2(self._y-target._y,self._x - target._x))
        if  Predator_mode:
            Hunter.update(self, model) 
        else:
            if self._color != 'green':
                Pulsator.update(self, model)
            self.move()
        
    def display(self,canvas): #The object is displayed as a ball 
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                           self._x+self.radius, self._y+self.radius,
                                fill=self._color)