class Manager(object):
    def __init__(self):
        self.active_objects = []

    def add_object(self, object):
        self.active_objects.append(object)

    def update(self, dt):
        for object in self.active_objects:
            object.update(dt)

    def apply_constant_force(self, force):
        for object in self.active_objects:
            object.apply_constant_force(force)

    def apply_impulse(self, impulse):
        #for object in self.active_objects:
        #    object.velocity += impulse/object.mass
        #    print('New velocity: ', object.velocity)
        object = self.active_objects[0]
        object.velocity += impulse/object.mass