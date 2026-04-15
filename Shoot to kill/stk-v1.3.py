#shoot to kill
#pre-game stuff
version = 'v1.3.4'
print(f'this game is in version {version}\nhave fun!')
# TODOS:
# TODO add more guns: (Rocket launcher, shotgun, nuke detonator, mines, grenade)
# TODO add enemies with more health
# TODO add wave mode
# thats it
#code
#imports
import pygame #module with screens, and sfx, and imgs and stuff
from random import choice, randint #randint, best god damn thing ever, I love you randint.
#pygame vars (screen, clock, initialize, etc)
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 25)
#pygame img vars
gun_ani = pygame.image.load('Assets\\img\\reload.png').convert_alpha()
idle_gun = pygame.image.load('Assets\\img\\gun_idle_01.png').convert_alpha()
idle_gun_2 = pygame.image.load('Assets\\img\\gun_idle_02.png').convert_alpha()
idle_gun_3 = pygame.image.load('Assets\\img\\gun_idle_03.png').convert_alpha()
testicles_placeholder = pygame.image.load('Assets\\img\\testicles_s.png').convert_alpha()
target = pygame.image.load('Assets\\img\\target.png').convert_alpha()
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
shotty_01 = pygame.image.load('Assets\\img\\shotgun_idle_01.png').convert_alpha()
shotty_02 = pygame.image.load('Assets\\img\\shotgun_idle_02.png').convert_alpha()
shotty_03 = pygame.image.load('Assets\\img\\shotgun_idle_03.png').convert_alpha()
shotty_tar = pygame.image.load('Assets\\img\\BIG_target.png').convert_alpha()
shotty_clicker = pygame.image.load('Assets\\img\\SG_target.png').convert_alpha()
bullet_hole_sheet = pygame.image.load('Assets\\img\\bullet_holes.png').convert_alpha()
#pygame sfx vars
pistol_shoot = pygame.mixer.Sound('Assets\\sfx\\pistol_shoot.mp3')
pistol_shoot.set_volume(0.2)
shotty_shoot = pygame.mixer.Sound('Assets\\sfx\\shotty_shoot.mp3')
#scream1 = pygame.mixer.Sound('Assets\\sfx\\scream1.mp3')
#scream2 = pygame.mixer.Sound('Assets\\sfx\\scream2.mp3')
#scream3 = pygame.mixer.Sound('Assets\\sfx\\scream3.mp3') UNNEEDED ASSETS, ALSO ANNOYING ASF, MAYBE USE LATER IDFK
hit = pygame.mixer.Sound('Assets\\sfx\\hit.mp3')
screams = [
    ###scream1, # BAA-!
    ###scream2, # WAAUHHHUAHHUAHHHH
    ###scream3, # BAAAAAAAAAAAAAAAAAAAH
    hit         # PWAOHHH
]
weapon_change = pygame.mixer.Sound('Assets\\sfx\\weapon_change.mp3')
reload_noise = pygame.mixer.Sound('Assets\\sfx\\reload_noise.mp3')
ouch = pygame.mixer.Sound('Assets\\sfx\\OUCH.mp3')
#other vars
BAM = False
bam_timer = 0
bam_limit = 3
reload_ani_wid = 320
reload_ani_hei = 160
rowsgun = 7
columnsgun = 2
reloading = False
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
gun_ani_index = 0
gun_timer = 0
anim_speed = 5
tx, ty = 750, 1000
gx, gy = 750, 500
gun_sprite = idle_gun
NO_MOUSE_IS_NOT_FUCKING_VISIBLE = False
pygame.mouse.set_visible(NO_MOUSE_IS_NOT_FUCKING_VISIBLE)
bullets = 9
#class
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
class special_gun_trigger:
    def __init__(self, image):
        self.image = image
        self.x = randint(200, 1300)
        self.y = randint(200, 800)
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.timer = 0
    def is_dead(self):
        self.limit = 120
        self.timer += 1
        if self.timer >= self.limit:
            return(True)
        else:
            return(False)
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
        self.alpha -= 1
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
    def push(self):
        self.y += 40
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
class bullet_hole:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def draw(self):
        screen.blit(self.image, self.imagerect)
enemies = []
triggers = []
ar_trigger_powerup = special_gun_trigger(ar_target)
ar_timer = 0
ar_end = 120
ar_active = False
gun = 'pistol'
ar_bullet_timer = 0
ar_bullet_limit = 10
score = 0
score_indicators = []
combo_level = 0
combo_timer = 0
combo_limit = 60 #frames (about a second to continue the combo streak)
add_combo = False
goodguydead = False
ar_score = False
mag_dump = False
kill = False
spawn_trigger = False
trig_spawned = False
spawn_enemy = False
enemy_limit = 5
state = 'menu'
max_trigs = 2
bullet_holes = []
#game loop
while running:
    text = font.render(f'{version}, developer mode', True, 'white')
############################################# mode change #####################################################
    if state == 'menu':
        cx, cy = pygame.mouse.get_pos()
        cursorrect = target.get_rect(center = (cx, cy))
        title_rect = title_card.get_rect(midtop = (750, 0))
        quit_rect = quit_button.get_rect(center = (750, 700))
        training_rect = training_button.get_rect(center = (750, 600))
        glossary_rect = glossary_button.get_rect(center = (750, 500))
        clock.tick(60) #refresh rate, 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(pistol_shoot)
                if cursorrect.colliderect(quit_rect):
                    running = False
                if cursorrect.colliderect(training_rect):
                    state = 'training'
                if cursorrect.colliderect(glossary_rect):
                    state = 'glossary'
                else:
                    bullet_holes.append(bullet_hole(cx, cy, choice(bullet_hole_imgs)))
        screen.fill('grey') # bg first
        screen.blit(title_card, title_rect)
        screen.blit(quit_button, quit_rect)
        screen.blit(training_button, training_rect)
        screen.blit(glossary_button, glossary_rect)
        for hole in bullet_holes:
            hole.draw()
        screen.blit(target, cursorrect) # target last
############################################# mode change #####################################################
    if state == 'training':
        clock.tick(60) #refresh rate, 60 fps
        bullet_display = font.render(f"{bullets} bullets", True, 'black')
        gun_display = font.render(f"gun: {gun}", True, 'black')
        score_display = font.render(f"score: {score}", True, 'black')
        if reloading:
            bullet_display = font.render('reloading...', True, 'black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and gun == 'pistol':
                    reloading = True
                    pygame.mixer.Sound.play(reload_noise)
                if event.key == pygame.K_SPACE:
                    state = 'menu'
                if event.key == pygame.K_s:
                    gun = 'shotty'
            if event.type == pygame.MOUSEBUTTONDOWN and not reloading and gun != 'assault rifle':
                bullets -= 1
                if bullets == 0 and combo_level == 9 and gun == 'pistol':
                    mag_dump = True
                BAM = True
                if bullets < 0 and gun == 'pistol':
                    BAM = False
                    pygame.mixer.Sound.play(reload_noise)
                    reloading = True
                if gun == 'shotty':
                    pygame.mixer.Sound.play(shotty_shoot)
                if bullets <= 0 and gun == 'shotty':
                    gun = 'pistol'
                    pygame.mixer.Sound.play(weapon_change)
                if gun == 'pistol' and not reloading:
                    pygame.mixer.Sound.play(pistol_shoot)
        cx, cy = pygame.mouse.get_pos()
        if cy in range(0, 300) and gun == 'pistol':
            gun_sprite = idle_gun_3
        if cy in range(300, 600) and gun == 'pistol':
            gun_sprite = idle_gun_2
        if cy in range(600, 1000) and gun == 'pistol':
            gun_sprite = idle_gun
        if cy in range(0, 300) and gun == 'assault rifle':
            gun_sprite = ar_03
        if cy in range(300, 600) and gun == 'assault rifle':
            gun_sprite = ar_02
        if cy in range(600, 1000) and gun == 'assault rifle':
            gun_sprite = ar_01
        if cy in range(0, 300) and gun == 'shotty':
            gun_sprite = shotty_03
        if cy in range(300, 600) and gun == 'shotty':
            gun_sprite = shotty_02
        if cy in range(600, 1000) and gun == 'shotty':
            gun_sprite = shotty_01
        screen.fill('grey') #bg first
        gunrect = idle_gun.get_rect(midbottom=(cx, ty)) #rects next
        reloadrect = gun_frames[gun_ani_index].get_rect(midbottom=(cx, ty))
        mousebuttons = pygame.mouse.get_pressed()
        if mousebuttons[0] and gun == 'assault rifle': #left click + rifle
            if ar_bullet_timer >= ar_bullet_limit:
                pygame.mixer.Sound.play(pistol_shoot)
                BAM = True
                ar_bullet_timer = 0
                bullets -= 1
                if bullets <= 0:
                    pygame.mixer.Sound.play(weapon_change)
                    gun = 'pistol'
            ar_bullet_timer += 1
        for enemy in enemies:
            screen.blit(enemy.image, enemy.imagerect)
            enemy.move()
            if enemy.passed_cam():
                enemies.remove(enemy)
        if gun == 'pistol' or gun == 'assault rifle':
            cursorrect = target.get_rect(center = (cx, cy))
            screen.blit(target, cursorrect)
        elif gun == 'shotty':
            cursorrect = shotty_tar.get_rect(center = (cx, cy))
            screen.blit(shotty_tar, cursorrect)
        if reloading:
            screen.blit(gun_frames[gun_ani_index], reloadrect)
            gun_timer += 1
            if gun_timer >= anim_speed:
                gun_ani_index += 1
                gun_timer = 0
            if gun_ani_index >= len(gun_frames):
                gun_ani_index = 0
                bullets = 9
                reloading = False
        else:
            screen.blit(gun_sprite, gunrect)#gun on top of target in case of overlap
        if BAM:
            for enemy in enemies:
                if enemy.imagerect.colliderect(cursorrect):
                    if enemy.image == good_guy:
                        pygame.mixer.Sound.play(ouch)
                        enemies.remove(enemy)
                        goodguydead = True
                    else:
                        pygame.mixer.Sound.play(choice(screams))
                        enemies.remove(enemy)
                        kill = True
                        add_combo = True
            for trig in triggers:
                if trig.imagerect.colliderect(cursorrect):
                    pygame.mixer.Sound.play(weapon_change)
                    if trig.image == ar_target:
                        gun = 'assault rifle'
                        bullets = 30
                    elif trig.image == shotty_clicker:
                        gun = 'shotty'
                        bullets = 6
                    triggers.remove(trig)
            screen.fill('white') #bam flash
            bam_timer += 1
            if bam_timer >= bam_limit:
                BAM = False
                bam_timer = 0
        screen.blit(bullet_display, (cx - 50, cy - 60))
        screen.blit(gun_display, (cx - 50, cy - 100))
        screen.blit(score_display, (cx - 50, cy - 140))
        screen.blit(score_img, (1180, 0))
        for ind in score_indicators:
            ind.image.set_alpha(ind.alpha)
            ind.text.set_alpha(ind.alpha)
            screen.blit(ind.image, ind.imagerect_img)
            screen.blit(ind.text, ind.imagerect_text)
            ind.fade()
            if ind.alpha <= 0:
                score_indicators.remove(ind)
        if add_combo:
            combo_timer = 0
            combo_level += 1
            combo_mult = combo_level * 10
            if combo_level >= 2:
                for ind in score_indicators:
                    ind.push()
                match combo_level:
                    case 2:
                        combo_display = font.render(f"DOUBLE KILL, +{combo_mult}", True, 'black')
                        score_indicators.append(score_indicator(score1, combo_display))
                    case 3:
                        combo_display = font.render(f"TRIPLE KILL, +{combo_mult}", True, 'black')
                        score_indicators.append(score_indicator(score2, combo_display))
                    case _:
                        combo_display = font.render(f"COMBO X{combo_level}, +{combo_mult}", True, 'black')
                        score_indicators.append(score_indicator(score3, combo_display))
            if combo_level == 9 and gun == 'pistol':
                mag_dump = True
            add_combo = False
        else:
            combo_timer += 1
            if combo_timer >= combo_limit:
                    combo_level = 0
        if goodguydead:
            for ind in score_indicators:
                ind.push()
            score_mult = 200
            text_display = font.render(f"GOOD GUY DOWN, -{score_mult}", True, 'black')
            score -= score_mult
            score_indicators.append(score_indicator(score5, text_display))
            combo_level = 0
            goodguydead = False
        if ar_score:
            for ind in score_indicators:
                ind.push()
            score_mult = 50
            text_display = font.render(f"ASSAULT RIFLE, +{score_mult}", True, 'black')
            score += score_mult
            score_indicators.append(score_indicator(score1, text_display))
            ar_score = False
        if mag_dump:
            for ind in score_indicators:
                ind.push()
            score_mult = 400
            text_display = font.render(f"MAG DUMP, +{score_mult}", True, 'black')
            score += score_mult
            score_indicators.append(score_indicator(score4, text_display))
            mag_dump = False
        if kill:
            for ind in score_indicators:
                ind.push()
            score_mult = 50
            score += score_mult
            text_display = font.render(f"KILL, +{score_mult}", True, 'black')
            score_indicators.append(score_indicator(score1, text_display))
            kill = False
        if len(enemies) < enemy_limit and not reloading:
            enemies.append(guy(choice([bad_guy, bad_guy, bad_guy, bad_guy, bad_guy, bad_guy, good_guy])))
        for trig in triggers:
            if trig.is_dead():
                triggers.remove(trig)
            else:
                screen.blit(trig.image, trig.imagerect)
        if randint(1, 200) == 1 and len(triggers) < max_trigs:
            triggers.append(special_gun_trigger(choice((ar_target, shotty_clicker))))
############################################# mode change #####################################################
    if state == 'glossary':
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 'menu'
        screen.fill('black')
        kill_text = font2.render('\'KILL\': an enemy character is killed, 50 points.', True, 'white')
        good_guy_down_text = font2.render('\'GOOD GUY DOWN\': a surrendered/\'good\' character is killed, -400 points + stops killstreak.', True, 'white')
        mag_dump_text = font2.render('\'MAG DUMP\': streak of nine while using pistol, means that every shot in the magazine hit an enemy, 400 points', True, 'white')
        killrect = kill_text.get_rect(center = (750, 400))
        goodguyrect = good_guy_down_text.get_rect(center = (750, 500))
        magdumprect = mag_dump_text.get_rect(center = (750, 600))
        glossbigrect = gloss_big.get_rect(center = (750, 200))
        screen.blit(kill_text, killrect)
        screen.blit(good_guy_down_text, goodguyrect)
        screen.blit(mag_dump_text, magdumprect)
        screen.blit(gloss_big, glossbigrect)
    screen.blit(text, (10, 10))
    pygame.display.flip()
#end
quit()