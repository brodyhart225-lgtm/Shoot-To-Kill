from random import randint
class guy:
    def __init__(self, image):
        self.x = randint(300, 1200)
        self.y = 0
        self.image = image
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def move(self):
        self.y += 15
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def passed_cam(self):
        if self.y >= 1500:
            return(True)
        else:
            return(False)