from Object import Object, TOTAL_LAYERS

class Hitbox:
    all_hitboxes = {}
    for layer in range(1, TOTAL_LAYERS + 1):
        all_hitboxes[layer] = []
    def __init__(self, object:Object,width, height, layer, perfect_elastic = False):
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
                return True
        return False