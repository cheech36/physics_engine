from __future__ import division
from manager import *
from event_handler import *
from ball import *
from arena import *
from collision import *


class World(object):
    def __init__(self):
        self.scene1, arena_set = self.init_scene()
        self.event_log = []
        self.event = EventHandler(self.scene1, self.event_log)
        self.manager = Manager()
        player_set = self.init_players()
        self.monitor = CollisionMonitor()
        self.ARENA_SET = self.monitor.addSet(arena_set)
        self.PLAYER_SET = self.monitor.addSet(player_set)

        self.dt = .01

    def init_scene(self):
        scene1 = display(x=1600, y=200, width=600, height=600)
        arena = []
        print(scene1.forward)
        # scene1.forward = (0,-.3,-1)

        l = 20
        t = -1
        h = 40

        floor      = Plane(( 0, -(h-1)/2, 0), (40, 1, 40))
        ceiling    = Plane(( 0, (h+1)/2, 0),(40, 1, 40))
        back_wall  = Plane(( 0,1,-19.5), (40, h, 1))
        front_wall = Plane(( 0,1, 19.5), (40, h, 1))
        right_wall = Plane(( 19.5,1, 0), (1, h, 40))
        left_wall  = Plane((-19.5,1, 0), (1, h, 40))

        floor.boundary.append(BP('y', -h/2, 'neg'))
        ceiling.boundary.append(BP('y', h/2, 'pos'))
        back_wall.boundary.append(BP('z',  19,'pos'))
        front_wall.boundary.append(BP('z', -19,'neg'))
        right_wall.boundary.append(BP('x',  19,'pos'))
        left_wall.boundary.append(BP('x', -19,'neg'))

        #ceiling.visible = False
        arena.append(floor)
        arena.append(ceiling)
        arena.append(back_wall)
        arena.append(front_wall)
        arena.append(right_wall)
        arena.append(left_wall)

        return scene1, arena

    def init_players(self):
        b1 = Ball((0, 10, 0), 2)
        self.manager.add_object(b1)

        b2 = Ball((4, 15, 1), 2)
        self.manager.add_object(b2)
        b2.color = color.red
        b2.radius = 3
        b2.mass *= 3

        b3 = Ball((0, 15, 10), 2)
        self.manager.add_object(b3)
        b3.color = color.yellow
        b3.radius = 4
        b3.mass *= 10

        b4 = Ball((0, -15, 10), 2)
        self.manager.add_object(b4)
        b4.color = color.orange

        player_set = self.manager.active_objects
        return player_set

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
            self.monitor.check(self.PLAYER_SET, self.ARENA_SET)
            self.monitor.check(self.PLAYER_SET, self.PLAYER_SET)
            self.check_log()

world1 = World()
world1.run()
