from visual import *

class Plane(box):
    class_id = 2
    def __init__(self, pos, size, axis=(1, 0, 0)):
        super(Plane,self).__init__(pos=pos, length=size[0], height=size[1], width=size[2], axis=axis)
        self.color = color.green
        self.boundary = []
        self.reaction = []

        #To do: Calculate plane faces i.e. Top, Bottom, Left ... etc
        #Then append boundary coordinates to the face

    def add_boundary(self, boundary):
        self.boundary.append(boundary)

    def add_reaction(self, arg):
        pass
