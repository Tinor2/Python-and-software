class Star:
    def __init__ (self, name, mass):
        self.name = name
        self.mass = mass
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
class Planet:
    def __init__ (self, name, mass):
        self.name = name
        self.mass = mass
        self.position = None
def gravitational_attraction(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    return G * m1 * m2 / r**2