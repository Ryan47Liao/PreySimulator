# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    perception = 200 
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self, x, y, 
                width = 5, height=5, angle = None, speed = 5)
        self.randomize_angle()
        self._CD = Pulsator.counter 
        
        
    def seen(self, model, predict):
        PREYs = model.find(predict)
        SEEN = [s for s in PREYs if self.distance((s._x,s._y)) < self.perception]
        SEEN = [s for s in SEEN if s is not self]
        return SEEN 
    
    def update(self, model):
        SEEN = self.seen(model, lambda s: isinstance(s, Prey))
        if len(SEEN) > 0:
            target = min(SEEN, key = lambda s: self.distance((s._x,s._y)))
            self.set_angle(atan2(target._y - self._y,target._x - self._x))
        self.move()
        Pulsator.update(self, model)
        