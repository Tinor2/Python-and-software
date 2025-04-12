from typing import Set
from Object import Object
import os
import math

class GridRenderer:
    def __init__(self, width: int, height: int, resolution: float = 0.1):
        """
        Initialize grid renderer with high resolution support
        Args:
            width: Grid width in world units
            height: Grid height in world units
            resolution: Size of each cell in world units (smaller = higher resolution)
        """
        self.resolution = resolution
        self.grid_width = math.ceil(width / resolution)
        self.grid_height = math.ceil(height / resolution)
        self.tracked_objects: Set['Object'] = set()
        self.grid = [[' ' for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        
    def world_to_grid(self, x: float, y: float) -> tuple[int, int]:
        """Convert world coordinates to grid coordinates"""
        grid_x = int(x / self.resolution)
        grid_y = int(y / self.resolution)
        return grid_x, grid_y
    
    def add_object(self, obj: 'Object') -> None:
        self.tracked_objects.add(obj)
    
    def update_grid(self) -> None:
        """Update grid with current object positions at high resolution"""
        self.grid = [[' ' for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        
        for obj in self.tracked_objects:
            grid_x, grid_y = self.world_to_grid(obj.position[0], obj.position[1])
            
            # Handle objects with hitboxes
            if obj.col:
                # Convert hitbox dimensions to grid cells
                width_cells = math.ceil(obj.col.width / self.resolution)
                height_cells = math.ceil(obj.col.height / self.resolution)
                
                # Fill hitbox area
                for y in range(height_cells):
                    for x in range(width_cells):
                        if (0 <= grid_x + x < self.grid_width and 
                            0 <= grid_y + y < self.grid_height):
                            self.grid[grid_y + y][grid_x + x] = '█'
            else:
                # Single point for objects without hitboxes
                if (0 <= grid_x < self.grid_width and 
                    0 <= grid_y < self.grid_height):
                    self.grid[grid_y][grid_x] = '●'
    
    def render(self) -> None:
        """Render the high-resolution grid"""
        os.system('clear')  # Clear console on Mac
        self.update_grid()
        
        # Print grid with coordinates
        print(f"Resolution: {self.resolution} units/cell")
        print('   ' + '-' * (self.grid_width + 2))
        
        for y in range(self.grid_height):
            # Print y-axis coordinates every 5 cells
            if y % 5 == 0:
                print(f"{y*self.resolution:2.1f}|", end='')
            else:
                print('   |', end='')
                
            print(''.join(self.grid[y]) + '|')
            
        print('   ' + '-' * (self.grid_width + 2))
        
        # Print x-axis coordinates
        print('    ', end='')
        for x in range(0, self.grid_width, 5):
            print(f"{x*self.resolution:2.1f}", end=' ' * 3)
        print()