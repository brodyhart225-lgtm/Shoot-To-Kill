class score_indicator:
    def __init__(self, image, text):
        self.image = image
        self.x = 1000
        self.y = 30
        self.alpha = 255
        self.text = text
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
    def fade(self):
        self.y += 3
        self.alpha -= 3
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
    def push(self):
        self.y += 80
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
