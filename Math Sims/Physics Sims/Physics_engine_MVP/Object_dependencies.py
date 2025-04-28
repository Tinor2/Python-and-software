from enum import Enum
from math import sqrt
from constants import Shape, Color, TOTAL_LAYERS


class Renderer:
    def __init__(self, parent, shape, dimensions):
        self.parent = parent
        self.shape = shape
        if self.shape == Shape.RECTANGLE:
            if len(dimensions) != 2:
                raise ValueError("Rectangle shape requires 2 parameters for dimensions.")
            self.dimensions = (dimensions[0], dimensions[1])
        elif self.shape == Shape.CIRCLE:
            if len(dimensions) != 1:
                raise ValueError("Circle shape requires 1 parameter for dimensions.")
            self.dimensions = (dimensions[0],)
        self.dimensions = dimensions
        self.color = Color.WHITE
        self.layer = 0
        pass
    def render(self):
        position = self.parent.position
        render_result = {
            "position": position,
            "color": self.color,
            "layer": self.layer,
            "result":[]}
        if self.shape == Shape.RECTANGLE:
            if len(self.dimensions) != 2:
                raise ValueError("Rectangle shape requires 2 parameters for dimensions.")
            width = [render_result["color"]]*int(self.dimensions[0])
            render_result["result"] = [width]*int(self.dimensions[1])
        elif self.shape == Shape.CIRCLE:
            if len(self.dimensions) != 1:   
                raise ValueError("Circle shape requires 1 parameter for dimensions.")
            radius = self.dimensions[0]
            circle = [[0]*int(radius*2)]*int(radius*2)
            for i in range(int(radius*2)):
                for j in range(int(radius*2)):
                    if (i - radius)**2 + (j - radius)**2 <= radius**2:
                        circle[i][j] = render_result["color"]
                    else:
                        circle[i][j] = 0
            render_result["result"] = circle
        return render_result
    def __str__(self):
        description =f"Renderer(shape={self.shape}, dimensions={self.dimensions}, color={self.color}, layer={self.layer})\n"
        render = self.render()
        description += f"Position: {render['position']}\n"
        matrix = render["result"]
        # Replace nested loop with list comprehension
        matrix = [[1 if pixel != 0 else 0 for pixel in row] for row in matrix]
        for x, row in enumerate(matrix):
            for y,pixel in enumerate(row):
                if pixel == 0:
                    pixel = 0
                else:
                    pixel = 1
                matrix[x][y] = pixel
        # Add rows to description
        description += f"Matrix:\n"
        for row_num, row in enumerate(matrix):
            description += f"   {row}\n"
        description += f"color: {self.color}\n"
        return description

class Hitbox:
    all_hitboxes = {}
    for layer in range(1, TOTAL_LAYERS + 1):
        all_hitboxes[layer] = []
        
    def __init__(self, parent, width, length, layer):
        self.parent = parent
        if layer not in Hitbox.all_hitboxes.keys():
            raise ValueError(f"Layer {layer} does not exist.")
        Hitbox.all_hitboxes[layer].append(self)
        self.layer:int = layer
        self.width = width
        self.height = length
        self.shape_type = Shape.RECTANGLE
        self.perfect_elastic:bool = True
        self.radius= width/2 if self.shape_type == Shape.CIRCLE else None

    def check_collision(self):
        for hitbox in Hitbox.all_hitboxes[self.layer]:
            if hitbox == self:
                continue
                
            if self.shape_type == Shape.RECTANGLE and hitbox.shape_type == Shape.RECTANGLE:
                if self._check_box_collision(hitbox):
                    return hitbox
            elif self.shape_type == Shape.CIRCLE and hitbox.shape_type == Shape.CIRCLE:
                if self._check_circle_collision(hitbox):
                    return hitbox
            elif self.shape_type == Shape.CIRCLE:
                if self._check_circle_box_collision(hitbox):
                    return hitbox
            else:  # self is box, other is circle
                if hitbox._check_circle_box_collision(self):
                    return hitbox
        return None

    def _check_box_collision(self, other: 'Hitbox') -> bool:
        return (self.parent.position[0] < other.parent.position[0] + other.width and
                self.parent.position[0] + self.width > other.parent.position[0] and
                self.parent.position[1] < other.parent.position[1] + other.height and
                self.parent.position[1] + self.height > other.parent.position[1])

    def _check_circle_collision(self, other: 'Hitbox') -> bool:
        dx = self.parent.position[0] - other.parent.position[0]
        dy = self.parent.position[1] - other.parent.position[1]
        distance = sqrt(dx * dx + dy * dy)
        if self.radius is None or other.radius is None:
            raise ValueError("Circle radius not set.")
        return distance < (self.radius + other.radius)

    def _check_circle_box_collision(self, box: 'Hitbox') -> bool:
        closest_x = max(box.parent.position[0], 
                       min(self.parent.position[0], 
                           box.parent.position[0] + box.width))
        closest_y = max(box.parent.position[1], 
                       min(self.parent.position[1], 
                           box.parent.position[1] + box.height))
        
        dx = self.parent.position[0] - closest_x
        dy = self.parent.position[1] - closest_y
        if self.radius is None:
            raise ValueError("Circle radius not set.")
        return float(sqrt(dx * dx + dy * dy)) < self.radius

    def correct_collision(self) -> list[int]:
        colliding_hitbox = self.check_collision()
        if not colliding_hitbox:
            return [0, 0]

        if self.shape_type == Shape.RECTANGLE and colliding_hitbox.shape_type == Shape.RECTANGLE:
            return self._correct_box_collision(colliding_hitbox)
        elif self.shape_type == Shape.CIRCLE and colliding_hitbox.shape_type == Shape.CIRCLE:
            return self._correct_circle_collision(colliding_hitbox)
        else:
            # For mixed collisions, use box correction as approximation
            return self._correct_box_collision(colliding_hitbox)

    def _correct_box_collision(self, other: 'Hitbox') -> list[int]:
        x_overlap = min(
            abs(self.parent.position[0] + self.width - other.parent.position[0]),
            abs(other.parent.position[0] + other.width - self.parent.position[0])
        )
        
        y_overlap = min(
            abs(self.parent.position[1] + self.height - other.parent.position[1]),
            abs(other.parent.position[1] + other.height - self.parent.position[1])
        )
        
        if x_overlap < y_overlap:
            if self.parent.position[0] < other.parent.position[0]:
                return [-x_overlap, 0]
            return [x_overlap, 0]
        else:
            if self.parent.position[1] < other.parent.position[1]:
                return [0, -y_overlap]
            return [0, y_overlap]

    def _correct_circle_collision(self, other: 'Hitbox') -> list[int]:
        dx = self.parent.position[0] - other.parent.position[0]
        dy = self.parent.position[1] - other.parent.position[1]
        distance = sqrt(dx * dx + dy * dy)
        if self.radius is None or other.radius is None:
            raise ValueError("Circle radius not set.")
        if distance == 0:  # Avoid division by zero
            return [self.radius, 0]
            
        overlap = self.radius + other.radius - distance
        if overlap <= 0:
            return [0, 0]
            
        # Calculate correction vector
        correction_x = (dx / distance) * overlap
        correction_y = (dy / distance) * overlap
        return [correction_x, correction_y]