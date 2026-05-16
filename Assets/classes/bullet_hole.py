class bullet_hole:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def draw(self, screen):
        screen.blit(self.image, self.imagerect)
if __name__ == '__main__':
    print('It appears you loaded this game from somewhere that isn\'t main.py')
    input('press enter to quit --->')