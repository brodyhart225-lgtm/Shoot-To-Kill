class explosion:
    def __init__(self, x, y, frames):
        self.x = x
        self.y = y
        self.frames = frames
        self.index = 5
        self.image = self.frames[self.index]
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.timer = 0
        self.limit = 6
    def adv(self):
        self.timer += 1
        self.con = self.timer >= self.limit
        if self.con:
            self.index += 1
            self.timer = 0
    def is_adv(self):
        return(self.index>=len(self.frames))
    def draw(self, screen):
        self.image = self.frames[self.index]
        screen.blit(self.image, self.imagerect)