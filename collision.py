
class BP:
    # Incoming direction positive, negative, or both
    direction = {'pos': 1, 'neg': -1, 'bi': 0}
    axis      = {'x': 0, 'y': 1, 'z': 2}
    COLLISION_THRESHOLD = .01

    def __init__(self, axis_name, axis_value, mode='bi'):
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


class CollisionMonitor:
    def __init__(self):
        self.interacting_sets = dict()

    def check(self, set1_id, set2_id=0):
        set1 = self.interacting_sets[set1_id]
        if(set2_id):
            set2 = self.interacting_sets[set2_id]

        #print(set1, set2)

        if(set2_id):
            for obj1 in set1:
                for obj2 in set2:
                    type1 = obj1.class_id
                    type2 = obj2.class_id
                    if(type1 == 1 and type2 == 2):
                        collision = self.check_player_plane(obj1, obj2)
                        if(collision):
                            self.on_player_plane(obj1, obj2)
                    elif(type1 == 2 and type2 == 1):
                        collision = self.check_player_plane(obj2, obj1)
                        if(collision):
                            self.on_player_plane(obj2, obj1)
                            return 1

    def check_player_plane(self, player, plane):
            return plane.boundary[0].check(player)

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


    def addSet(self, newSet):
        newKey = len(self.interacting_sets) + 1
        self.interacting_sets.update({newKey: newSet})
        return newKey