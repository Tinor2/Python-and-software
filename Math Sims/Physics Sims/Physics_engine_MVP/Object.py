import time
from Object_dependencies import Hitbox
TOTAL_LAYERS = 5
TIME_STEP = 1/60  # Time step in seconds (1/FPS)


class Object:
    def __init__(self, mass, position:list[int], velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.force = [0, 0]
        self.acceleration = [self.force[0]/mass, self.force[1]/mass]
        self.col = None
    def add_collider(self, w,l,layer):
        self.col = Hitbox(self,w,l,layer)

    def apply_force(self, force, dt):
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
def update(self, dt = TIME_STEP):
    time.sleep(dt)