from Object import Object, TOTAL_LAYERS
from enum import Enum
from math import sqrt

class Shape(Enum):
    BOX = "box"
    CIRCLE = "circle"
class Color(Enum):
    def __new__(cls, r, g, b):
            obj = object.__new__(cls)
            obj._value_ = (r, g, b)
            return obj
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
class Renderer:
    def __init__(self, Object:Object, shape:Shape, size:tuple[float],color:Color, layer):
        self.object = Object  
        self.shape = shape
        if self.shape == Shape.BOX:
            if len(size) != 2:
                raise ValueError("Box shape requires 2 parameters for size.")
            self.size = (size[0], size[1])
        elif self.shape == Shape.CIRCLE:
            if len(size) != 1:
                raise ValueError("Circle shape requires 1 parameter for size.")
            self.size = (size[0],)
        self.size = size
        self.color = color
        self.layer = layer
        pass
    def render(self):
        position = self.object.position
        render_result = {
            "position": position,
            "color": self.color,
            "layer": self.layer,
            "result":[]}
        if self.shape == Shape.BOX:
            pass
        elif self.shape == Shape.CIRCLE:
            pass
        pass
class Hitbox:
    all_hitboxes = {}
    for layer in range(1, TOTAL_LAYERS + 1):
        all_hitboxes[layer] = []
        
    def __init__(self, object:Object, width, height, layer, shape_type: Shape = Shape.BOX, perfect_elastic = True):
        if layer not in Hitbox.all_hitboxes.keys():
            raise ValueError(f"Layer {layer} does not exist.")
        Hitbox.all_hitboxes[layer].append(self)
        self.object: Object = object
        self.layer:int = layer
        self.width = width
        self.height = height
        self.shape_type = shape_type
        self.perfect_elastic:bool = perfect_elastic
        self.radius= width/2 if shape_type == Shape.CIRCLE else None

    def check_collision(self):
        for hitbox in Hitbox.all_hitboxes[self.layer]:
            if hitbox == self:
                continue
                
            if self.shape_type == Shape.BOX and hitbox.shape_type == Shape.BOX:
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
        return (self.object.position[0] < other.object.position[0] + other.width and
                self.object.position[0] + self.width > other.object.position[0] and
                self.object.position[1] < other.object.position[1] + other.height and
                self.object.position[1] + self.height > other.object.position[1])

    def _check_circle_collision(self, other: 'Hitbox') -> bool:
        dx = self.object.position[0] - other.object.position[0]
        dy = self.object.position[1] - other.object.position[1]
        distance = sqrt(dx * dx + dy * dy)
        if self.radius is None or other.radius is None:
            raise ValueError("Circle radius not set.")
        return distance < (self.radius + other.radius)

    def _check_circle_box_collision(self, box: 'Hitbox') -> bool:
        closest_x = max(box.object.position[0], 
                       min(self.object.position[0], 
                           box.object.position[0] + box.width))
        closest_y = max(box.object.position[1], 
                       min(self.object.position[1], 
                           box.object.position[1] + box.height))
        
        dx = self.object.position[0] - closest_x
        dy = self.object.position[1] - closest_y
        if self.radius is None:
            raise ValueError("Circle radius not set.")
        return float(sqrt(dx * dx + dy * dy)) < self.radius

    def correct_collision(self) -> list[int]:
        colliding_hitbox = self.check_collision()
        if not colliding_hitbox:
            return [0, 0]

        if self.shape_type == Shape.BOX and colliding_hitbox.shape_type == Shape.BOX:
            return self._correct_box_collision(colliding_hitbox)
        elif self.shape_type == Shape.CIRCLE and colliding_hitbox.shape_type == Shape.CIRCLE:
            return self._correct_circle_collision(colliding_hitbox)
        else:
            # For mixed collisions, use box correction as approximation
            return self._correct_box_collision(colliding_hitbox)

    def _correct_box_collision(self, other: 'Hitbox') -> list[int]:
        x_overlap = min(
            abs(self.object.position[0] + self.width - other.object.position[0]),
            abs(other.object.position[0] + other.width - self.object.position[0])
        )
        
        y_overlap = min(
            abs(self.object.position[1] + self.height - other.object.position[1]),
            abs(other.object.position[1] + other.height - self.object.position[1])
        )
        
        if x_overlap < y_overlap:
            if self.object.position[0] < other.object.position[0]:
                return [-x_overlap, 0]
            return [x_overlap, 0]
        else:
            if self.object.position[1] < other.object.position[1]:
                return [0, -y_overlap]
            return [0, y_overlap]

    def _correct_circle_collision(self, other: 'Hitbox') -> list[int]:
        dx = self.object.position[0] - other.object.position[0]
        dy = self.object.position[1] - other.object.position[1]
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