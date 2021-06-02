# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole

class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        self._CD = self.counter 
    
    def update(self, model):
        EATEN = Black_Hole.update(self, model)
        if len(EATEN) > 0:
            self._height += len(EATEN)
            self._width += len(EATEN) 
            self.radius += len(EATEN) 
            self._CD = self.counter 
        else:
            self._CD -= 1 
        if self._CD == 0: 
            self._height -= 1
            self._width -= 1
            self.radius -= 1
            self._CD = self.counter#Reset 
        if self._height == 0: 
            model.remove(self)
        