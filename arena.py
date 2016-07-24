from visual import *

class Plane(box):
    def __init__(self, pos, size, axis=(1,0,0)):
        super(Plane,self).__init__(pos=pos, length=size[0], height=size[1], width=size[2], axis=axis)
        self.color = color.green