from Object import Object, TOTAL_LAYERS

class Hitbox:
    all_hitboxes = {}
    for layer in range(1, TOTAL_LAYERS + 1):
        all_hitboxes[layer] = []
    def __init__(self, object:Object,width, height, layer, perfect_elastic = True):
        if layer not in Hitbox.all_hitboxes.keys():
            raise ValueError(f"Layer {layer} does not exist.")
        Hitbox.all_hitboxes[layer].append(self)
        self.object = object
        self.layer = layer
        self.width = width
        self.height = height
        self.perfect_elastic = perfect_elastic
    def check_collision(self):
        for hitbox in Hitbox.all_hitboxes[self.layer]:
            if hitbox == self:
                continue
            if self.object.position[0] < hitbox.object.position[0] + hitbox.width and \
               self.object.position[0] + self.width > hitbox.object.position[0] and \
               self.object.position[1] < hitbox.object.position[1] + hitbox.height and \
               self.object.position[1] + self.height > hitbox.object.position[1]:
                return hitbox
        return None
    def correct_collision(self) -> list[int]:
        colliding_hitbox = self.check_collision()
        if not colliding_hitbox:
            return [0, 0]  # No collision, no correction needed
        
        # Calculate overlap in both axes
        x_overlap = min(
            abs(self.object.position[0] + self.width - colliding_hitbox.object.position[0]),  # Right edge overlap
            abs(colliding_hitbox.object.position[0] + colliding_hitbox.width - self.object.position[0])  # Left edge overlap
        )
        
        y_overlap = min(
            abs(self.object.position[1] + self.height - colliding_hitbox.object.position[1]),  # Bottom edge overlap
            abs(colliding_hitbox.object.position[1] + colliding_hitbox.height - self.object.position[1])  # Top edge overlap
        )
        
        # Determine which direction requires less movement
        if x_overlap < y_overlap:
            # Correct horizontally
            if self.object.position[0] < colliding_hitbox.object.position[0]:
                return [-x_overlap, 0]  # Move left
            return [x_overlap, 0]  # Move right
        else:
            # Correct vertically
            if self.object.position[1] < colliding_hitbox.object.position[1]:
                return [0, -y_overlap]  # Move up
            return [0, y_overlap]  # Move down