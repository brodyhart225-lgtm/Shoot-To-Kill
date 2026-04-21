class perk_image:
    def __init__(self, image, pos, images, font2):
        self.image = image
        self.images = images
        self.pos = pos
        self.y = 800
        match self.pos:
            case 1:
                self.x = 375
            case 2:
                self.x = 750
            case 3:
                self.x = 1125
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        if self.image == self.images[0]:
            self.effect = 'Damage multiplier'
        elif self.image == self.images[1]:
            self.effect = 'Extra life'
        elif self.image == self.images[2]:
            self.effect = 'Enemies slowed 0.75x'
        elif self.image == self.images[3]:
            self.effect = '1.5x ammo capacity'
        elif self.image == self.images[4]:
            self.effect = '1.5x target size'
        elif self.image == self.images[5]:
            self.effect = '1.5x max HP'
        self.text = font2.render(self.effect, True, 'white')
        self.textrect = self.text.get_rect(midright = (self.imagerect.left - 10, self.imagerect.centery))
    def draw(self, screen):
        screen.blit(self.image, self.imagerect)
        screen.blit(self.text, self.textrect)
    def increase(self, var, amt):
        var *= amt
        return(var)
#   __________________________
    def should_increase(self):
        pass
#   __________________________
#   ^^^^^^^^^^^^^^^^^^^^^^^^^^ example block
    def should_increase_damage(self):
        return(self.effect == 'Damage multiplier')
    def should_increase_ammo(self):
        return(self.effect == '1.5x ammo capacity')
    def should_increase_lives(self):
        return(self.effect == 'Extra life')
    def should_increase_slow(self):
        return(self.effect == 'Enemies slowed 0.75x')
    def should_increase_size(self):
        return(self.effect == '1.5x target size')
    def should_increase_health(self):
        return(self.effect == '1.5x max HP')