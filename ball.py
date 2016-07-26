from visual import *

class Ball(sphere):
    REST_THRESHOLD = .01
    class_id = 1
    def __init__(self,pos, size):
        super(Ball, self).__init__(pos=pos,radius=size, color=color.blue)
        self.net_force = vector(0,0,0)
        self.acceleration = vector(0,0,0)
        self.velocity = vector(0,0,0)
        self.position = vector(pos)
        self.mass = 20
        self.restitution = 1

    def apply_constant_force(self, new_force):
        self.net_force += vector(new_force)
        if self.net_force.mag < self.REST_THRESHOLD:
            self.net_force = vector(0,0,0)



    def apply_variable_force(self):
        ## This will create an instance of a force class with
        ## callback functionality to check conditions and value each itteration
        ## Changing in time or by location and Turning off when necessary
        pass

    def update(self, dt):

        self.acceleration = self.net_force/self.mass
        self.velocity     += self.acceleration * dt
        self.position     += self.velocity * dt
        self.render()

    def render(self):
        self.pos = self.position.astuple()