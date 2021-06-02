import controller
import model   # Calls to update in update_all are passed a reference to model

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special 

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simultons   = set()
selected = None #text

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons   = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 

#step just one update in the simulation
def step ():
    global running
    if not running:
        start ()
    update_all()
    stop ()
        
    
        
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected
    selected = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selected 
    print(f"{selected}({x},{y})")
    if selected == 'Remove': 
        for sim in find(p = lambda s: s.distance((x,y)) < 5 ):
            remove(sim)
        
    elif selected is not None:
        try:
            add( eval(f"{selected}({x},{y})") )
        except NameError:
            pass


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    return {i for i in simultons if p(i)}


# for each simulton in this simulation, call update (passing model to it) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global simultons,cycle_count
    if running:
        cycle_count += 1
        for sim in list(simultons):
            sim.update(model) 
        
#How to animate: 1st: delete all simultons on the canvas; 2nd: call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; 3rd: update the label defined in the controller for progress 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    global simultons
    # Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in simultons:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")

