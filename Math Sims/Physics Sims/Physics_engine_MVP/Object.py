import time
TOTAL_LAYERS = 5
TIME_STEP = 1/60  # Time step in seconds (1/FPS)


class Object:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.force = [0, 0]
        self.acceleration = [self.force[0]/mass, self.force[1]/mass]
    def apply_force(self, force, dt):
        self.force += force
    def update_position(self, dt):
        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt


def update(self, dt = TIME_STEP):
    time.sleep(dt)