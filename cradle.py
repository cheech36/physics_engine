from __future__ import division
from manager import *
from event_handler import *
from ball import *
from arena import *

class World(object):
    def __init__(self):
        self.scene1 = self.init_scene()
        self.event_log = []
        self.event = EventHandler(self.scene1, self.event_log)
        self.manager = Manager()
        self.init_player()
        self.dt = .01

    def init_scene(self):
        scene1 = display(x=1600, y=200, width=600, height=600)
        print(scene1.forward)
        #scene1.forward = (0,-.3,-1)
        floor      = Plane(( 0,0, 0), (20, 1, 20))
        back_wall  = Plane(( 0,1,-9.5), (20, 2, 1 ))
        front_wall = Plane(( 0,1, 9.5), (20, 2, 1 ))
        right_wall = Plane(( 9.5,1, 0), (20, 2, 1 ), (0,0,1))
        left_wall  = Plane((-9.5,1, 0), (20, 2, 1 ), (0,0,1))
        return scene1

    def init_player(self):
        b1 = Ball((0, 20, 0), 2)
        b1.apply_constant_force((0,0,0))
        self.manager.add_object(b1)

    def check_log(self):
        if(self.event_log):
            event = self.event_log.pop()
            if( event[0] == 'force'):
                self.manager.apply_constant_force(event[1])
            elif( event[0] == 'impulse'):
                self.manager.apply_impulse(event[1])

    def run(self):
        while true:
            rate(200)
            self.manager.update(self.dt)
            self.check_log()

world1 = World()
world1.run()
