import pygame
pygame.init()
from random import choice, randint
from Assets.classes.guy import *
from Assets.classes.special_gun_trigger import *
from Assets.classes.score_indicator import *
from Assets.classes.bullet_hole import *
from Assets.classes.grunt import *
from Assets.classes.midman import *
from Assets.classes.fatguy import *
from Assets.classes.explosion import *
from Assets.classes.smokehole import *
from Assets.classes.wave_level import *
from Assets.classes.perk_image import *
from Assets.img.surfaces import *
from Assets.img.texts import *
from Assets.sfx.sounds import *
from game import *
print(f'This game is currently in version {version}\nEnjoy!')
if __name__ == '__main__':
    main()