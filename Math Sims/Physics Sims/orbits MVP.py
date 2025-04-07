import equations as eq
import time
class Star:
    def __init__ (self, name, mass):
        self.name = name
        self.mass = mass
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
class Planet:
    def __init__(self, name, mass, initial_distance: int):
        self.name = name
        self.mass = mass
        self.position = [initial_distance, 0]  # Fixed duplicate position assignment
        self.velocity = [0, 0]
        self.solar_system = None  # Reference to containing solar system

    def move(self, time_step, star: Star):
        if not self.solar_system:
            raise ValueError(f"Planet {self.name} is not part of any solar system")
        
        # Calculate the gravitational force
        force_on_self = eq.gravitational_attraction(
            self.mass,
            star.mass,
            eq.find_dist(self.position))
        force_on_self = -force_on_self
        # Update acceleration
        self.acceleration = [force_on_self / self.mass, 0]
        
       
class Solar_System:
    def __init__ (self, name, star:Star):
        self.name = name
        self.stars = set()
        self.planets = set()
    def add_planet (self, planet):
        self.planets.add(planet)
        planet.solar_system = self  # Add reference to solar system
def gravitational_attraction(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    return G * m1 * m2 / r**2

sun = Star("Sun", 10)
new_system = Solar_System("Solar System", sun)
earth = Planet("Earth", 1,100)
new_system.add_planet(earth)

TIME_STEP = 1/60 #Time step in seconds (1/FPS)
def Update(): #This function will be called every frame
    time.sleep(TIME_STEP) #Sleep for the time step
