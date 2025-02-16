import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simplified model for Earth and another planet (e.g., Mars)

# Earth's orbital radius (AU)
earth_radius = 1

# Other planet's orbital radius (AU)
planet_radius = 1.5 

# Earth's orbital period (years)
earth_period = 1

# Other planet's orbital period (years)
planet_period = 1.88  # Approximate Martian year

# Create time array
time = np.linspace(0, 10, 1000)  # Simulate 10 years

# Calculate Earth's position
earth_x = earth_radius * np.cos(2 * np.pi * time / earth_period)
earth_y = earth_radius * np.sin(2 * np.pi * time / earth_period)

# Calculate other planet's position
planet_x = planet_radius * np.cos(2 * np.pi * time / planet_period)
planet_y = planet_radius * np.sin(2 * np.pi * time / planet_period)

# Calculate relative positions (from Earth's perspective)
relative_x = planet_x - earth_x
relative_y = planet_y - earth_y

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
ax.set_title("Planetary Orbits from Earth's Perspective")

# Initialize empty lists for animation data
earth_line, = ax.plot([], [], 'bo', label='Earth')
planet_line, = ax.plot([], [], 'ro', label='Other Planet')
relative_line, = ax.plot([], [], 'go', label='Relative Position')

# Animation function
def animate(i):
    earth_line.set_data(earth_x[i], earth_y[i])
    planet_line.set_data(planet_x[i], planet_y[i])
    relative_line.set_data(relative_x[i], relative_y[i])
    return earth_line, planet_line, relative_line

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(time), interval=20, blit=True)

# Show the plot (interactive animation)
plt.legend()
plt.show()