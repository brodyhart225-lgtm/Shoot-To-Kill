import pygame
screen = pygame.display.set_mode((1500, 1000))
gun_ani = pygame.image.load('Assets\\img\\reload.png').convert_alpha()
idle_gun = pygame.image.load('Assets\\img\\gun_idle_01.png').convert_alpha()
idle_gun_2 = pygame.image.load('Assets\\img\\gun_idle_02.png').convert_alpha()
idle_gun_3 = pygame.image.load('Assets\\img\\gun_idle_03.png').convert_alpha()
testicles_placeholder = pygame.image.load('Assets\\img\\testicles_s.png').convert_alpha()
target = pygame.image.load('Assets\\img\\target.png').convert_alpha()
target_diameter = 64
bad_guy = pygame.image.load('Assets\\img\\bad_guy.png').convert_alpha()
ar_target = pygame.image.load('Assets\\img\\AR_target.png').convert_alpha()
ar_01 = pygame.image.load('Assets\\img\\ar_idle_01.png').convert_alpha()
ar_02 = pygame.image.load('Assets\\img\\ar_idle_02.png').convert_alpha()
ar_03 = pygame.image.load('Assets\\img\\ar_idle_03.png').convert_alpha()
good_guy = pygame.image.load('Assets\\img\\good_guy.png').convert_alpha()
score_img = pygame.image.load('Assets\\img\\gun_score_img.png').convert_alpha()
score1 = pygame.image.load('Assets\\img\\score_guns\\01.png').convert_alpha() #red
score2 = pygame.image.load('Assets\\img\\score_guns\\02.png').convert_alpha() #orange
score3 = pygame.image.load('Assets\\img\\score_guns\\03.png').convert_alpha() #yellow
score4 = pygame.image.load('Assets\\img\\score_guns\\04.png').convert_alpha() #supreme
score5 = pygame.image.load('Assets\\img\\score_guns\\05.png').convert_alpha() #bad
title_card = pygame.image.load('Assets\\img\\title_card.png').convert_alpha()
quit_button = pygame.image.load('Assets\\img\\quit.png').convert()
freeplay_button = pygame.image.load('Assets\\img\\freeplay.png').convert()
training_button = pygame.image.load('Assets\\img\\train.png').convert()
glossary_button = pygame.image.load('Assets\\img\\glossary.png').convert()
gloss_big = pygame.image.load('Assets\\img\\gloss_big.png').convert_alpha()
wave_button = pygame.image.load('Assets\\img\\wave.png').convert()
shotty_01 = pygame.image.load('Assets\\img\\shotgun_idle_01.png').convert_alpha()
shotty_02 = pygame.image.load('Assets\\img\\shotgun_idle_02.png').convert_alpha()
shotty_03 = pygame.image.load('Assets\\img\\shotgun_idle_03.png').convert_alpha()
shotty_tar = pygame.image.load('Assets\\img\\BIG_target.png').convert_alpha()
shotty_clicker = pygame.image.load('Assets\\img\\SG_target.png').convert_alpha()
bullet_hole_sheet = pygame.image.load('Assets\\img\\bullet_holes.png').convert_alpha()
grunt_sheet = pygame.image.load('Assets\\img\\grunt.png').convert_alpha()
grunt_frames = []
columnsgru = 2
rowsgru = 1
gruwid = 125
gruhei = 160
for row in range(rowsgru):
    for col in range(columnsgru):
        frame = grunt_sheet.subsurface(col*gruwid, row*gruhei, gruwid, gruhei)
        grunt_frames.append(frame)
middleman_sheet = pygame.image.load('Assets\\img\\middleman.png').convert_alpha()
midman_frames = []
columnsmid = 2
rowsmid = 1
midwid = 125
midhei = 240
for row in range(rowsmid):
    for col in range(columnsmid):
        frame = middleman_sheet.subsurface(col*midwid, row*midhei, midwid, midhei)
        midman_frames.append(frame)
fatso = pygame.image.load('Assets\\img\\fatso.png').convert_alpha()
fatso_frames = []
for col in range(2):
    for row in range(1):
        fat_frame = fatso.subsurface(col*220, row*270, 220, 270)
        fatso_frames.append(fat_frame)
explosion_sheet = pygame.image.load('Assets\\img\\EXPLOSION.png').convert_alpha()
explosion_sheet = pygame.transform.scale(explosion_sheet, (1024, 2560))
explo_frames = []
columnsexp = 2
rowsexp = 5
for row in range(rowsexp):
    for col in range(columnsexp):
        ex_frame = explosion_sheet.subsurface(col*512, row*512, 512, 512)
        explo_frames.append(ex_frame)
smoke = pygame.image.load('Assets\\img\\smoke.png').convert_alpha()
smoke = pygame.transform.scale(smoke, (700, 700))
rpg_tar = pygame.image.load('Assets\\img\\rpg_tar.png').convert_alpha()
rpg_tar = pygame.transform.scale(rpg_tar, (512, 512))
rpg_trg = pygame.image.load('Assets\\img\\rpg_trig.png').convert_alpha()
rp_01 = pygame.image.load('Assets\\img\\rp_01.png').convert_alpha()
rp_02 = pygame.image.load('Assets\\img\\rp_02.png').convert_alpha()
rp_03 = pygame.image.load('Assets\\img\\rp_03.png').convert_alpha()
waves_bg = pygame.image.load('Assets\\img\\wave_bg.png').convert()
waves_bg = pygame.transform.scale(waves_bg, (1500, 1000))
pause_bg = pygame.image.load('Assets\\img\\pause_bg.png').convert()
pause_bg = pygame.transform.scale(pause_bg, (1500, 1000))
waveadv_bg = pygame.image.load('Assets\\img\\waveadv_bg.png').convert()
waveadv_bg = pygame.transform.scale(waveadv_bg, (1500, 1000))
perksheet = pygame.image.load('Assets\\img\\perk_sheet.png').convert()
perk_images = []
perkcol = 2
perkrow = 3
for col in range(perkcol):
    for row in range(perkrow):
        frame = perksheet.subsurface(col * 160, row * 160, 160, 160)
        perk_images.append(frame)
reload_ani_wid = 320
reload_ani_hei = 160
rowsgun = 7
columnsgun = 2
gun_frames = []
for row in range(rowsgun):
    for col in range(columnsgun):
        gunframe = gun_ani.subsurface(col*reload_ani_wid, row*reload_ani_hei, reload_ani_wid, reload_ani_hei)
        gun_frames.append(gunframe)
rowshole = 2
columnshole = 4
hole_height, hole_width = 20, 20
bullet_hole_imgs = []
for row in range(rowshole):
    for col in range(columnshole):
        holeframe = bullet_hole_sheet.subsurface(col*hole_width, row*hole_height, hole_width, hole_height)
        bullet_hole_imgs.append(holeframe)