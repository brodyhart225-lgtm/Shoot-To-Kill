from random import randint
class special_gun_trigger:
    def __init__(self, image):
        self.image = image
        self.x = randint(200, 1300)
        self.y = randint(200, 800)
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.timer = 0
    def is_dead(self):
        self.limit = 120
        self.timer += 1
        if self.timer >= self.limit:
            return(True)
        else:
            return(False)