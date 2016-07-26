from visual import *
from common import *

class Plane(box):
    class_type = PLANE
    class_instance = 0
    def __init__(self, pos, size, axis=(1, 0, 0)):
        super(Plane,self).__init__(pos=pos, length=size[0], height=size[1], width=size[2], axis=axis, opacity=.1)
        Plane.class_instance += 1
        self.id = (Plane.class_type, Plane.class_instance, Plane.class_type, Plane.class_instance)
        self.color = color.green
        self.boundary = []
        self.reaction = []

        #To do: Calculate plane faces i.e. Top, Bottom, Left ... etc
        #Then append boundary coordinates to the face

    def add_boundary(self, boundary):
        self.boundary.append(boundary)
        self.boundary.register(self.id)

    def add_reaction(self, arg):
        pass
