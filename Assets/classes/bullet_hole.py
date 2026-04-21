class bullet_hole:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def draw(self, screen):
        screen.blit(self.image, self.imagerect)