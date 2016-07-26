from __future__ import division
from common import *

class BP:
    # Incoming direction positive, negative, or both
    direction = {'pos': 1, 'neg': -1, 'bi': 0}
    axis      = {'x': 0, 'y': 1, 'z': 2}
    COLLISION_THRESHOLD = .01
    class_id = BOUNDING_PLANE
    class_instance = 0

    def __init__(self, axis_name, axis_value, mode='bi'):
        BP.class_instance += 1
        self.id = (0, 0, BP.class_id, BP.class_instance)
        self.axis_name = axis_name
        self.norm_axis = self.axis[axis_name]
        self.axis_mode = self.direction[mode]
        self.axis_value = axis_value
        self.player_pos = 0
        self.collision_data = [0]
        self.type = 'BP'

    def check(self, player):
        # Check either the x, y, or z component of the players position
        pos = player.position[self.norm_axis]
        if self.axis_mode == 0 and False:
            pass
        elif self.axis_mode == -1 and pos - player.radius < self.axis_value:
            self.collision_data[0] = self.norm_axis
            return 1
        elif self.axis_mode == 1 and pos + player.radius > self.axis_value:
            self.collision_data[0] = self.norm_axis
            return 1
        else:
            self.collision_data[0] = self.norm_axis
            return 0

    def getdata(self):
        return self.collision_data

    def gettype(self):
        return self.type

    def register(self, super_id):
        self.id[0:1] = super_id[0:1]


class CollisionMonitor:
    def __init__(self):
        self.interacting_sets = dict()

    def check(self, set1_id, set2_id):
        set1 = self.interacting_sets.get(set1_id)
        set2 = self.interacting_sets.get(set2_id)
        collision_list = []

        # Check for collision between sets
        if(set1_id != set2_id):
            for obj1 in set1:
                for obj2 in set2:
                    collision = 0
                    type1 = obj1.class_type
                    type2 = obj2.class_type
                    set = (type1, type2)
                    if( set == (BALL, PLANE) or set == (PLANE, BALL)):
                        if(self.check_player_plane(obj1, obj2)):
                            collision_list.append((COLL_BALL_PLANE, obj1, obj2))

        # A more efficient routine for collisions within the same set
        elif(set1_id == set2_id):
            for j in range(0, len(set1)):
                obj1 = set1[j]
                for i in range(j + 1, len(set1)):
                    obj2 = set1[i]
                    collision = 0
                    if(obj1.class_type == BALL):
                        collision = self.check_player_player(obj1, obj2)
                    if(collision):
                        collision_list.append((COLL_BALL_BALL, obj1, obj2))

        if (len(collision_list)):
            self.handle_collisions(collision_list)


    def handle_collisions(self, list):
        for collision in list:
            coll_type = collision[0]
            obj1 = collision[1]
            obj2 = collision[2]
            # To do check again after handling to make sure collisions were resolved
            if (coll_type == COLL_BALL_PLANE):
                self.on_player_plane(obj1, obj2)
                #check again here
            if (coll_type == COLL_BALL_BALL):
                self.on_player_player(obj1, obj2)
                #check again here


    def check_player_plane(self, obj1, obj2):
        if (obj1.class_type == BALL and obj2.class_type == PLANE):
            return obj2.boundary[0].check(obj1)
        elif (obj2.class_type == BALL and obj1.class_type == PLANE):
            return obj1.boundary[0].check(obj2)
        else:
            print('Error: BALL and/or PLANE missing from collision set')
            return 0


    def check_player_player(self,obj1, obj2):
        distance = obj1.position - obj2.position
        min_distance = obj1.radius + obj2.radius
        if (distance.mag <= min_distance):
            return 1
        else:
            return 0

    def on_player_plane(self, plr, plane):
        vel_norm = plane.boundary[0].getdata()

        if (len(plane.reaction)):
            # Execute specialized boundary if available
            pass
        else:
            # Default is to bounce of planes elastically
            plr.velocity[vel_norm[0]] *= -1

    def on_player_player(self,objX, objY):
        m1               = objX.mass
        m2               = objY.mass
        r1Norm           = objX.position
        r2Norm           = objY.position
        u1_vec           = objX.velocity
        u2_vec           = objY.velocity
        u                = m1*m2/(m1+m2)
        rNorselfvec      = r1Norm - r2Norm
        vRel_vec         = u1_vec - u2_vec
        dv1 = 2*(u/m1)*vRel_vec.proj(rNorselfvec)
        dv2 = 2*(u/m2)*vRel_vec.proj(rNorselfvec)
        v1_vec           = u1_vec - dv1
        v2_vec           = u2_vec + dv2
        objX.velocity = v1_vec
        objY.velocity = v2_vec

    def addSet(self, newSet):
        newKey = len(self.interacting_sets) + 1
        self.interacting_sets.update({newKey: newSet})
        return newKey