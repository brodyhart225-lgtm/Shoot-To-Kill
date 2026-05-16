import pygame

if __name__ == '__main__':
    pygame.init()
    from game import *
    print(f'This game is currently in version {version}\nEnjoy!')
    main()