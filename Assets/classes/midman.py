from random import randint
class midman:
    def __init__(self, frames):
        self.frames = frames
        self.image = frames[0]
        self.x = randint(300, 1200)
        self.y = 0
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.health = 2
        self.gru_index = 0
        self.gru_frames = 2
        self.ani_timer = 0
        self.ani_limit = 20
    def move(self, speed):
        if self.imagerect.centery < 1000:
            self.imagerect.centery += speed - 1
        if self.imagerect.centery >= 1000:
            self.imagerect.centery = 1000
    def attacking(self):
        return(self.imagerect.centery >= 1000)
    def draw(self, screen):
        screen.blit(self.image, self.imagerect)
    def hit(self, damage):
        self.damage = damage
        self.health -= self.damage
    def dead(self):
        return(self.health <= 0)
    def image_update(self):
        self.gru_index += 1
        if self.gru_index > self.gru_frames:
            self.gru_index = 0
        match self.gru_index:
            case 0:
                self.image = self.frames[0]
            case 1:
                self.image = self.frames[1]
    def timed_ani(self):
        self.ani_timer += 1
        if self.ani_timer >= self.ani_limit:
            self.ani_timer = 0
            return(True)