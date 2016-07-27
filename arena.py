from visual import *
from common import *
from collision import *

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
        self.face_front = None
        self.face_back  = None
        self.__calc_faces__()

    def __calc_faces__(self):
        # Assume for now that axis points in the x-direction
        # Front/Back is positive/negative length extremum
        # Top/Bottom is positve/negative height extremum
        # Right/Left is positive/negative width extemum
            front_offset = .5 * self.length
            self.face_front = self.pos.x + front_offset

            back_offset = .5 * self.length
            self.face_back = self.pos.x - back_offset

            top_offset = .5 * self.height
            self.face_top = self.pos.y + top_offset

            bottom_offset = .5 * self.height
            self.face_bottom = self.pos.y - bottom_offset

            right_offset = .5 * self.width
            self.face_right = self.pos.z - right_offset

            left_offset = .5 * self.width
            self.face_left = self.pos.z + left_offset

    def add_boundary(self, normal, direction, face, offset = 0):

        ct = self.class_type
        ci = self.class_instance

        if(face == 'front'):
            boundary = BP(normal, self.face_front, direction, (ct,ci))
        if(face == 'back'):
            boundary = BP(normal, self.face_back, direction, (ct,ci))
        if(face == 'top'):
            boundary = BP(normal, self.face_top, direction, (ct,ci))
        if(face == 'bottom'):
            boundary = BP(normal, self.face_bottom, direction, (ct,ci))
        if(face == 'right'):
            boundary = BP(normal, self.face_right, direction, (ct,ci))
        if(face == 'left'):
            boundary = BP(normal, self.face_left, direction, (ct,ci))
        self.boundary.append(boundary)

    def add_reaction(self, arg):
        pass
