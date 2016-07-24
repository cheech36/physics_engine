from visual import *

class EventHandler:
    def __init__(self, scene, event_log=None):

        self.scene = scene
        self.scene.bind('_keydown', self.handle_keydown)
        self.scene.bind('keyup', self.handle_keyup)
        self.scene.bind('mousedown', self.grab)
        self.event_log = event_log
        self.head = vector(0,0,0)
        self.tail = vector(0,0,0)
        self.scale = 20

    def handle_keydown(self, evt):
        if evt.key == 'left':
            self.left_keydown()

        if evt.key == 'right':
            self.right_keydown()

        if evt.key == 'up':
            self.up_keydown()

        if evt.key == 'down':
            self.down_keydown()

        if evt.key == " ":     # Jump
            self.space_keydown()

        if evt.key == 's':     # Stop
            self.s_keydown()

        if evt.key == 'f':     # Turn on friction
            self.f_keydown()

        if evt.key == 'o':     # Return to position
            self.o_keydown()

        if evt.key == 'p':     # Print stats
            self.p_keydown()

        if evt.key == '1':      # Don't press
            self.one_keydown()

        if evt.key == '2':      # Don't press
            self.two_keydown()

        if evt.key == '3':      # Don't press
            self.three_keydown()

        if evt.key == 'f1':     # Pause
            self.f1_keydown()

        if evt.key == 't':      # Train - Not working
            self.t_keydown()

        if evt.key == 'j':     # Manual Indicate - Right Decision
            self.j_keydown()

        if evt.key == 'n':    # Manual Indicate - Wrong Decisions
            self.n_keydown()

    def left_keydown(self):
        pass

    def right_keydown(self):
        pass

    def up_keydown(self):
        pass

    def down_keydown(self):
        pass

    def space_keydown(self):
        pass

    def f_keydown(self):
        pass

    def s_keydown(self):
        pass

    def o_keydown(self):
        pass

    def j_keydown(self):
        pass

    def n_keydown(self):
        pass

    def p_keydown(self):
        pass

    def one_keydown(self):
        pass

    def two_keydown(self):
        pass

    def three_keydown(self):
        pass

    def f1_keydown(self):
        pass

    def t_keydown(self):
        pass


# Key Up Functions ##
    def handle_keyup(self, evt):
        if evt.key == " ":
            self.space_keyup()

    def space_keyup(self):
        pass

    def handle_click(self, evt):
        pass

    def grab(self, evt):
        self.tail = vector(self.scene.mouse.pos)
        self.scene.bind('mousemove',self.move)
        self.scene.bind('mouseup', self.drop)
        self.arrow = arrow(pos=self.tail, axis=vector(0,0,0), shaftwidth=1)
        self.arrow.visible = False

    def move(self, evt):
        self.head = self.scene.mouse.project(normal=(0,0,-1))
        self.arrow.axis = self.head - self.tail


    def drop(self, evt):
        self.tail = self.scene.mouse.project(normal=(0,0,-1))
        self.scene.unbind('mousemove', self.move)
        self.scene.unbind('mouseup', self.drop)
        impulse = self.arrow.axis * self.scale
        print(impulse)
        self.event_log.append(('impulse', impulse))



