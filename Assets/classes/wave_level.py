class wavelevel:
    def __init__(self):
        self.wave = 1
        self.max_en = 5
        self.enemies = 50
        self.enemies_killed = 0
        self.chance = 100
    def add_enemy(self):
        self.enemies_killed += 1
    def reseed(self):
        self.enemies = self.enemies + 10
        self.wave += 1
        self.max_en = int(self.max_en * 1.5)
        self.enemies_killed = 0
    def is_ready_to_reseed(self):
        return(self.enemies_killed >= self.enemies)
if __name__ == '__main__':
    print('It appears you loaded this game from somewhere that isn\'t main.py')
    input('press enter to quit --->')