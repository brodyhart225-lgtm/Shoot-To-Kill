import pygame
pistol_shoot = pygame.mixer.Sound('Assets/sfx/pistol_shoot.mp3')
pistol_shoot.set_volume(0.1)
shotty_shoot = pygame.mixer.Sound('Assets/sfx/shotty_shoot.mp3')
#scream1 = pygame.mixer.Sound('Assets/sfx/scream1.mp3')
#scream2 = pygame.mixer.Sound('Assets/sfx/scream2.mp3')
#scream3 = pygame.mixer.Sound('Assets/sfx/scream3.mp3') #UNNEEDED ASSETS, ALSO ANNOYING ASF, MAYBE USE LATER IDFK
hit = pygame.mixer.Sound('Assets/sfx/hit.mp3')
screams = [
    #scream1, # BAA-!
    #scream2, # WAAUHHHUAHHUAHHHH
    #scream3, # BAAAAAAAAAAAAAAAAAAAH
    hit         # PWAOHHH
]
weapon_change = pygame.mixer.Sound('Assets/sfx/weapon_change.mp3')
reload_noise = pygame.mixer.Sound('Assets/sfx/reload_noise.mp3')
ouch = pygame.mixer.Sound('Assets/sfx/OUCH.mp3')
kablooeysound = pygame.mixer.Sound('Assets/sfx/kablooey.mp3')
wave_advance = pygame.mixer.Sound('Assets/sfx/wave_advance.mp3')
death_sft = pygame.mixer.Sound('Assets/sfx/lose.mp3')
pause_sft = pygame.mixer.Sound('Assets/sfx/pause.mp3')
unpause_sft = pygame.mixer.Sound('Assets/sfx/unpause.mp3')
ahh = pygame.mixer.Sound('Assets/sfx/ahh.mp3')