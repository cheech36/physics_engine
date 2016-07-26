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
        self.id = [0, 0, BP.class_id, BP.class_instance]
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


        if(set1_id != set2_id):         #Check for collision between sets
            for obj1 in set1:
                for obj2 in set2:
                    collision = 0
                    type1 = obj1.class_type
                    type2 = obj2.class_type
                    if(type1 == BALL and type2 == PLANE):
                        collision = self.check_player_plane(obj1, obj2)
                        if(collision):
                            self.on_player_plane(obj1, obj2)
                    elif(type1 == PLANE and type2 == BALL):
                        collision = self.check_player_plane(obj2, obj1)
                        if(collision):
                            self.on_player_plane(obj2, obj1)

                    if (collision):
                        collision_list.append(obj1.id)
                        collision_list.append(obj2.id)

        elif( set1_id == set2_id):       #Check for collisions within the sets - For now its just players
            for j in range(0, len(set1)):
                obj1 = set1[j]
                for i in range(j + 1, len(set1)):
                    obj2 = set1[i]
                    collision = 0
                    if(obj1.class_type == BALL):
                        collision = self.check_player_player(obj1, obj2)

                    if(collision):
                        collision_list.append(obj1.id)
                        collision_list.append(obj2.id)
                        self.on_player_player(obj1, obj2)



        if (len(collision_list)):
            pass
            #Go to resolve collisions
            #print(collision_list)

    def check_player_plane(self, player, plane):
            return plane.boundary[0].check(player)

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
            pass
            # This will alllow for a custom reaction which can be added to the boundary

        elif (vel_norm == 1):
            plr.getVelocity()[vel_norm] *= -plr.restitution
            # For some reason 2 this threshold needs to be ~ 2 or the balls continue to bounce
            if abs(plr.getVelocity()[vel_norm]) < 2:
                plr.getVelocity()[vel_norm] = 0
            plr.position[1] = 0
            plr.acceleration[1] = 0
        else:
            # Reflect off horizontal planes
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