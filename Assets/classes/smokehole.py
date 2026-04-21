class smokehole:
    def __init__(self, x, y, smoke):
        self.x = x
        self.y = y
        self.alpha = 255
        self.image = smoke
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def fade(self):
        self.alpha -= 5
        self.image.set_alpha(self.alpha)
    def draw(self, screen):
        screen.blit(self.image, self.imagerect)