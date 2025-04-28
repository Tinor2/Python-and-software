import time
from Object_dependencies import Renderer, Shape, Color, Hitbox
from constants import TIME_STEP, Shape, Color


class Game_Object:
    def __init__(self, mass, position:list[int], velocity, initial_force = [0, 0]):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.force = initial_force
        self.acceleration = [self.force[0]/mass, self.force[1]/mass]
        self.col = None
        self.renderer = None
    def add_collider(self, w,l,layer):
        self.col = Hitbox(self,w,l,layer)
    def add_renderer(self, renderer):
        self.renderer = renderer
    def apply_force(self, force:list[int]):
        self.force += force
    def update_position(self, dt):
        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        
        if self.col:
            colliding_hitbox = self.col.check_collision()
            if colliding_hitbox:
                offset = self.col.correct_collision()
                if offset:
                    self.position = [self.position[0] + offset[0], self.position[1] + offset[1]]
                # Handle collision
                if self.col.perfect_elastic:
                    # Perfectly elastic collision
                    self.velocity[0] = -self.velocity[0]
                    self.velocity[1] = -self.velocity[1]
                else:
                    # Inelastic collision (simple bounce)
                    self.velocity[0] *= -0.5
                    self.velocity[1] *= -0.5

def start():
    new_object = Game_Object(mass= 1, position= [10, 0], velocity= [0, 0], initial_force= [0, 0])
    new_object.col = Hitbox(new_object, 10, 10, 1)
    new_object.apply_force([0,5])
    new_object.add_renderer(Renderer(new_object,Shape.CIRCLE,(3,)))
    print(new_object.renderer)
def update(self, dt = TIME_STEP):
    self.update_position(dt)
    time.sleep(dt)
start()