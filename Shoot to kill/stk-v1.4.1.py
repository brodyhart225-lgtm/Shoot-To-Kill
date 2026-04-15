#shoot to kill
#pre-game stuff
version = 'v1.4.1'
print(f'this game is in version {version}\nhave fun!')
#TODO: [] add wave advance screen similar to the losing screen, can unlock new guns and stuff here, examples below:
"""
    (amt) bullets of (gun)

    Damage resistance by (amt)%

    Second wind - extra life

    Adrenaline boost - time slowed by (amt)% when health below 25%

    25% chance to deflect hits

    LEGENDARY PERK - Thorns - damages enemies when hit

    3 Sentry bots
"""
#TODO: [] add health boosts using trig class
#TODO: [] add sentry bots
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
fontBIG = pygame.font.Font(None, 200)
youlose = fontBIG.render('YOU LOSE!', True, 'red')
loserect = youlose.get_rect(center = (750, 400))
menu_or_pgain = font.render('S - Play again... W - Menu...', True, 'Red')
menu_pgainrect = menu_or_pgain.get_rect(center = (750, 600))
pausemenutext = fontBIG.render('PAUSED', True, 'black')
pausemenutextrect = pausemenutext.get_rect(center = (750, 400))
#pygame img vars
gun_ani = pygame.image.load('Assets/img/reload.png').convert_alpha()
idle_gun = pygame.image.load('Assets/img/gun_idle_01.png').convert_alpha()
idle_gun_2 = pygame.image.load('Assets/img/gun_idle_02.png').convert_alpha()
idle_gun_3 = pygame.image.load('Assets/img/gun_idle_03.png').convert_alpha()
testicles_placeholder = pygame.image.load('Assets/img/testicles_s.png').convert_alpha()
target = pygame.image.load('Assets/img/target.png').convert_alpha()
target_diameter = 64
bad_guy = pygame.image.load('Assets/img/bad_guy.png').convert_alpha()
ar_target = pygame.image.load('Assets/img/AR_target.png').convert_alpha()
ar_01 = pygame.image.load('Assets/img/ar_idle_01.png').convert_alpha()
ar_02 = pygame.image.load('Assets/img/ar_idle_02.png').convert_alpha()
ar_03 = pygame.image.load('Assets/img/ar_idle_03.png').convert_alpha()
good_guy = pygame.image.load('Assets/img/good_guy.png').convert_alpha()
score_img = pygame.image.load('Assets/img/gun_score_img.png').convert_alpha()
score1 = pygame.image.load('Assets/img/score_guns/01.png').convert_alpha() #red
score2 = pygame.image.load('Assets/img/score_guns/02.png').convert_alpha() #orange
score3 = pygame.image.load('Assets/img/score_guns/03.png').convert_alpha() #yellow
score4 = pygame.image.load('Assets/img/score_guns/04.png').convert_alpha() #supreme
score5 = pygame.image.load('Assets/img/score_guns/05.png').convert_alpha() #bad
title_card = pygame.image.load('Assets/img/title_card.png').convert_alpha()
quit_button = pygame.image.load('Assets/img/quit.png').convert()
freeplay_button = pygame.image.load('Assets/img/freeplay.png').convert()
training_button = pygame.image.load('Assets/img/train.png').convert()
glossary_button = pygame.image.load('Assets/img/glossary.png').convert()
gloss_big = pygame.image.load('Assets/img/gloss_big.png').convert_alpha()
wave_button = pygame.image.load('Assets/img/wave.png').convert()
shotty_01 = pygame.image.load('Assets/img/shotgun_idle_01.png').convert_alpha()
shotty_02 = pygame.image.load('Assets/img/shotgun_idle_02.png').convert_alpha()
shotty_03 = pygame.image.load('Assets/img/shotgun_idle_03.png').convert_alpha()
shotty_tar = pygame.image.load('Assets/img/BIG_target.png').convert_alpha()
shotty_clicker = pygame.image.load('Assets/img/SG_target.png').convert_alpha()
bullet_hole_sheet = pygame.image.load('Assets/img/bullet_holes.png').convert_alpha()
grunt_sheet = pygame.image.load('Assets/img/grunt.png').convert_alpha()
grunt_frames = []
columnsgru = 2
rowsgru = 1
gruwid = 125
gruhei = 160
for row in range(rowsgru):
    for col in range(columnsgru):
        frame = grunt_sheet.subsurface(col*gruwid, row*gruhei, gruwid, gruhei)
        grunt_frames.append(frame)
middleman_sheet = pygame.image.load('Assets/img/middleman.png').convert_alpha()
midman_frames = []
columnsmid = 2
rowsmid = 1
midwid = 125
midhei = 240
for row in range(rowsmid):
    for col in range(columnsmid):
        frame = middleman_sheet.subsurface(col*midwid, row*midhei, midwid, midhei)
        midman_frames.append(frame)
fatso = pygame.image.load('Assets/img/fatso.png').convert_alpha()
fatso_frames = []
for col in range(2):
    for row in range(1):
        fat_frame = fatso.subsurface(col*220, row*270, 220, 270)
        fatso_frames.append(fat_frame)
explosion_sheet = pygame.image.load('Assets/img/EXPLOSION.png').convert_alpha()
explosion_sheet = pygame.transform.scale(explosion_sheet, (1024, 2560))
explo_frames = []
columnsexp = 2
rowsexp = 5
for row in range(rowsexp):
    for col in range(columnsexp):
        ex_frame = explosion_sheet.subsurface(col*512, row*512, 512, 512)
        explo_frames.append(ex_frame)
smoke = pygame.image.load('Assets/img/smoke.png').convert_alpha()
smoke = pygame.transform.scale(smoke, (700, 700))
rpg_tar = pygame.image.load('Assets/img/rpg_tar.png').convert_alpha()
rpg_tar = pygame.transform.scale(rpg_tar, (512, 512))
rpg_trg = pygame.image.load('Assets/img/rpg_trig.png').convert_alpha()
rp_01 = pygame.image.load('Assets/img/rp_01.png').convert_alpha()
rp_02 = pygame.image.load('Assets/img/rp_02.png').convert_alpha()
rp_03 = pygame.image.load('Assets/img/rp_03.png').convert_alpha()
waves_bg = pygame.image.load('Assets/img/wave_bg.png').convert()
waves_bg = pygame.transform.scale(waves_bg, (1500, 1000))
pause_bg = pygame.image.load('Assets/img/pause_bg.png').convert()
pause_bg = pygame.transform.scale(pause_bg, (1500, 1000))
waveadv_bg = pygame.image.load('Assets/img/waveadv_bg.png').convert()
waveadv_bg = pygame.transform.scale(waveadv_bg, (1500, 1000))
perksheet = pygame.image.load('Assets/img/perk_sheet.png').convert()
perk_images = []
perkcol = 2
perkrow = 3
for col in range(perkcol):
    for row in range(perkrow):
        frame = perksheet.subsurface(col * 160, row * 160, 160, 160)
        perk_images.append(frame)
#pygame sfx vars
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
        self.alpha -= 3
        self.imagerect_text = self.image.get_rect(topleft = (self.x, self.y))
        self.imagerect_img = self.image.get_rect(topright = (self.x, self.y))
    def push(self):
        self.y += 80
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
class grunt:
    def __init__(self, frames):
        self.frames = frames
        self.image = frames[0]
        self.x = randint(300, 1200)
        self.y = 0
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.health = 1
        self.gru_index = 0
        self.gru_frames = 2
        self.ani_timer = 0
        self.ani_limit = 20
    def move(self, speed):
        if self.imagerect.centery < 1000:
            self.imagerect.centery += speed
        if self.imagerect.centery >= 1000:
            self.imagerect.centery = 1000
    def attacking(self):
        return(self.imagerect.centery >= 1000)
    def draw(self):
        screen.blit(self.image, self.imagerect)
    def hit(self, damage):
        self.damage = damage
        self.health -= self.damage
    def dead(self):
        return(self.health <= 0)
    def image_update(self):
        self.gru_index += 1
        if self.gru_index > self.gru_frames:
            self.gru_index = 0
        match self.gru_index:
            case 0:
                self.image = self.frames[0]
            case 1:
                self.image = self.frames[1]
    def timed_ani(self):
        self.ani_timer += 1
        if self.ani_timer >= self.ani_limit:
            self.ani_timer = 0
            return(True)
class midman:
    def __init__(self, frames):
        self.frames = frames
        self.image = frames[0]
        self.x = randint(300, 1200)
        self.y = 0
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.health = 2
        self.gru_index = 0
        self.gru_frames = 2
        self.ani_timer = 0
        self.ani_limit = 20
    def move(self, speed):
        if self.imagerect.centery < 1000:
            self.imagerect.centery += speed - 1
        if self.imagerect.centery >= 1000:
            self.imagerect.centery = 1000
    def attacking(self):
        return(self.imagerect.centery >= 1000)
    def draw(self):
        screen.blit(self.image, self.imagerect)
    def hit(self, damage):
        self.damage = damage
        self.health -= self.damage
    def dead(self):
        return(self.health <= 0)
    def image_update(self):
        self.gru_index += 1
        if self.gru_index > self.gru_frames:
            self.gru_index = 0
        match self.gru_index:
            case 0:
                self.image = self.frames[0]
            case 1:
                self.image = self.frames[1]
    def timed_ani(self):
        self.ani_timer += 1
        if self.ani_timer >= self.ani_limit:
            self.ani_timer = 0
            return(True)
class fatguy:
    def __init__(self, frames):
        self.frames = frames
        self.image = frames[0]
        self.x = randint(300, 1200)
        self.y = 0
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.health = 3
        self.gru_index = 0
        self.gru_frames = 2
        self.ani_timer = 0
        self.ani_limit = 30
    def move(self, speed):
        if self.imagerect.centery < 1000:
            self.imagerect.centery += speed - 2
        if self.imagerect.centery >= 1000:
            self.imagerect.centery = 1000
    def attacking(self):
        return(self.imagerect.centery >= 1000)
    def draw(self):
        screen.blit(self.image, self.imagerect)
    def hit(self, damage):
        self.damage = damage
        self.health -= self.damage
    def dead(self):
        return(self.health <= 0)
    def image_update(self):
        self.gru_index += 1
        if self.gru_index > self.gru_frames:
            self.gru_index = 0
        match self.gru_index:
            case 0:
                self.image = self.frames[0]
            case 1:
                self.image = self.frames[1]
    def timed_ani(self):
        self.ani_timer += 1
        if self.ani_timer >= self.ani_limit:
            self.ani_timer = 0
            return(True)
class explosion:
    def __init__(self, x, y, frames):
        self.x = x
        self.y = y
        self.frames = frames
        self.index = 5
        self.image = self.frames[self.index]
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
        self.timer = 0
        self.limit = 6
    def adv(self):
        self.timer += 1
        self.con = self.timer >= self.limit
        if self.con:
            self.index += 1
            self.timer = 0
    def is_adv(self):
        return(self.index>=len(self.frames))
    def draw(self):
        self.image = self.frames[self.index]
        screen.blit(self.image, self.imagerect)
class smokehole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alpha = 255
        self.image = smoke
        self.imagerect = self.image.get_rect(center = (self.x, self.y))
    def fade(self):
        self.alpha -= 5
        self.image.set_alpha(self.alpha)
    def draw(self):
        screen.blit(self.image, self.imagerect)
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
        self.enemies = int(self.enemies * 1.5)
        self.wave += 1
        self.max_en = int(self.max_en * 1.5)
        self.enemies_killed = 0
    def is_ready_to_reseed(self):
        return(self.enemies_killed >= self.enemies)
class perk_image:
    def __init__(self, image, pos, images = list):
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
    def draw(self):
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
ar_trigger_powerup = special_gun_trigger(ar_target)
ar_timer = 0
ar_end = 120
ar_active = False
ar_bullet_timer = 0
ar_bullet_limit = 10
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
max_trigs = 1000
bullet_holes = []
#game loop
while running:
    text = font.render(version, True, 'white')
############################################# mode change #####################################################
    if state == 'menu':
        cx, cy = pygame.mouse.get_pos()
        cursorrect = target.get_rect(center = (cx, cy))
        title_rect = title_card.get_rect(midtop = (750, 0))
        quit_rect = quit_button.get_rect(center = (750, 700))
        training_rect = training_button.get_rect(center = (750, 600))
        glossary_rect = glossary_button.get_rect(center = (750, 500))
        wave_rect = wave_button.get_rect(center = (750, 400))
        clock.tick(60) #refresh rate, 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                state = 'lostwavemode'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s or event.type == pygame.MOUSEBUTTONDOWN:
                pistol_shoot.play()
                if cursorrect.colliderect(quit_rect):
                    running = False
                elif cursorrect.colliderect(training_rect):
                    state = 'training'
                    score = 0
                    triggers = []
                    enemies = []
                    score_indicators = []
                    explosions = []
                    smokeholes = []
                    gun = 'pistol'
                    bullets = 9
                    kablooey = False
                elif cursorrect.colliderect(glossary_rect):
                    state = 'glossary'
                elif cursorrect.colliderect(wave_rect):
                    state = 'waves'
                    gun = 'pistol'
                    health = 100
                    bullets = 9
                    wave_enemies = []
                    wavelevelindicator = wavelevel()
                    perks = []
                    damage = 1
                    ammo = 9
                    lives = 1
                    enemy_speed = 4
                    max_health = 100
                    target_diameter = 64
                    target = pygame.transform.scale(target, (target_diameter, target_diameter))
                else:
                    bullet_holes.append(bullet_hole(cx, cy, choice(bullet_hole_imgs)))
        screen.fill('grey') # bg first
        screen.blit(title_card, title_rect)
        screen.blit(quit_button, quit_rect)
        screen.blit(training_button, training_rect)
        screen.blit(glossary_button, glossary_rect)
        screen.blit(wave_button, wave_rect)
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
                    reload_noise.play()
                if event.key == pygame.K_SPACE:
                    state = 'menu'
                if event.key == pygame.K_s and not reloading and gun != 'assault rifle':
                    bullets -= 1
                    if combo_level >= 9 and gun == 'pistol':
                        mag_dump = True
                    BAM = True
                    if bullets < 0 and gun == 'pistol':
                        BAM = False
                        reload_noise.play()
                        reloading = True
                    if gun == 'shotty':
                        shotty_shoot.play()
                    if bullets <= 0 and gun == 'shotty':
                        gun = 'pistol'
                        weapon_change.play()
                    if gun == 'rocket launcher':
                        explosions.append(explosion(cx, cy, explo_frames))
                        kablooey = True
                        kablooeysound.play()
                        enemies.clear()
                    if bullets <=0 and gun == 'rocket launcher':
                        gun = 'pistol'
                        weapon_change.play()
                    if gun == 'pistol' and not reloading:
                        pistol_shoot.play()
            if event.type == pygame.MOUSEBUTTONDOWN and not reloading and gun != 'assault rifle':
                bullets -= 1
                if combo_level >= 9 and gun == 'pistol':
                    mag_dump = True
                BAM = True
                if bullets < 0 and gun == 'pistol':
                    BAM = False
                    reload_noise.play()
                    reloading = True
                if gun == 'shotty':
                    shotty_shoot.play()
                if bullets <= 0 and gun == 'shotty':
                    gun = 'pistol'
                    weapon_change.play()
                if gun == 'rocket launcher':
                    explosions.append(explosion(cx, cy, explo_frames))
                    kablooey = True
                    kablooeysound.play()
                    enemies.clear()
                if bullets <=0 and gun == 'rocket launcher':
                    gun = 'pistol'
                    weapon_change.play()
                if gun == 'pistol' and not reloading:
                    pistol_shoot.play()
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
        if cy in range(0, 300) and gun == 'rocket launcher':
            gun_sprite = rp_03
        if cy in range(300, 600) and gun == 'rocket launcher':
            gun_sprite = rp_02
        if cy in range(600, 1000) and gun == 'rocket launcher':
            gun_sprite = rp_01
        screen.fill('grey') #bg first
        for smk in smokeholes:
            smk.draw()
            smk.fade()
            if smk.alpha <=0:
                smokeholes.remove(smk)
        for ex in explosions:
            ex.draw()
            ex.adv()
            if ex.index == 6:
                smokeholes.append(smokehole(ex.x, ex.y))
            if ex.is_adv():
                explosions.remove(ex)
        gunrect = gun_sprite.get_rect(midbottom=(cursorrect.centerx, ty)) #rects next
        reloadrect = gun_frames[gun_ani_index].get_rect(midbottom=(cx, ty))
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if keys[pygame.K_s] and gun == 'assault rifle' or mouse[0] and gun == 'assault rifle': #left click + rifle
            if ar_bullet_timer >= ar_bullet_limit:
                pistol_shoot.play()
                BAM = True
                ar_bullet_timer = 0
                bullets -= 1
                if bullets <= 0:
                    weapon_change.play()
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
        elif gun == 'rocket launcher':
            cursorrect = rpg_tar.get_rect(center = (cx, cy))
            screen.blit(rpg_tar, cursorrect)
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
                        ouch.play()
                        enemies.remove(enemy)
                        goodguydead = True
                    else:
                        choice(screams).play()
                        enemies.remove(enemy)
                        kill = True
                        add_combo = True
            for trig in triggers:
                if trig.imagerect.colliderect(cursorrect):
                    weapon_change.play()
                    if trig.image == ar_target:
                        gun = 'assault rifle'
                        bullets = 30
                        ar_score = True
                    elif trig.image == shotty_clicker:
                        gun = 'shotty'
                        bullets = 6
                    elif trig.image == rpg_trg:
                        gun = 'rocket launcher'
                        bullets = 1
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
        if kablooey:
            for ind in score_indicators:
                ind.push()
            score_mult = 800
            text_display = font.render(f"KABLOOEY!!!, +{score_mult}", True, 'black')
            score += score_mult
            score_indicators.append(score_indicator(score4, text_display))
            kablooey = False
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
            triggers.append(special_gun_trigger(choice((ar_target, shotty_clicker, rpg_trg))))
############################################# mode change #####################################################
    if state == 'glossary':
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 'menu'
        screen.fill('grey')
        kill_text = font2.render('\'KILL\': an enemy character is killed, 50 points.', True, 'black')
        good_guy_down_text = font2.render('\'GOOD GUY DOWN\': a surrendered/\'good\' character is killed, -200 points + stops killstreak.', True, 'black')
        mag_dump_text = font2.render('\'MAG DUMP\': streak of nine while using pistol, means that every shot in the magazine hit an enemy, 400 points', True, 'black')
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
############################################# mode change #####################################################
    if state == 'waves':
        clock.tick(60)
        wave_display = font.render(f'WAVE {wavelevelindicator.wave}', True, 'red')
        bullet_display = font.render(f"{bullets} bullets", True, 'black')
        reloadrect = gun_frames[gun_ani_index].get_rect(midbottom=(cx, ty))
        enemies_left_display = font.render(f'Enemies left this wave: {wavelevelindicator.enemies - wavelevelindicator.enemies_killed}', True, 'black')
        if reloading:
            bullet_display = font.render('reloading...', True, 'black')
        health_text = font.render(f'health: {int(health)}', True, 'red')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = 'pausewavemode'
                    pause_sft.play()
                if event.key == pygame.K_SPACE:
                    state = 'menu'
                    target_diameter = 64
                    target = pygame.transform.scale(target, (target_diameter, target_diameter))
                if event.key == pygame.K_r and not reloading:
                    reloading = True
                    reload_noise.play()
            if event.type == pygame.MOUSEBUTTONDOWN and gun != 'assault rifle' and not reloading or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                bullets -= 1
                BAM = True
                if bullets < 0 and gun == 'pistol' and not reloading:
                    BAM = False
                    reload_noise.play()
                    reloading = True
                if gun == 'pistol' and not reloading:
                    for enem in wave_enemies:
                        if cursorrect.colliderect(enem.imagerect):
                            enem.hit(damage)
                            if enem.dead():
                                wave_enemies.remove(enem)
                                wavelevelindicator.add_enemy()
                                if wavelevelindicator.is_ready_to_reseed():
                                    wave_enemies.clear()
                                    wavelevelindicator.reseed()
                                    wave_advance.play()
                                    state = 'wavemodeadvance'
                                    perks.clear()
                                    for i in range(1, 4):
                                        perks.append(perk_image(choice(perk_images), i, perk_images))
                                    waveadv_text = font.render(f'You advanced to wave {wavelevelindicator.wave}!', True, 'white')
                                    waveadv_text_pick = font.render('Pick a perk!', True, 'white')
                                    waveadv_textrect = waveadv_text.get_rect(center = (750, 200))
                                    waveadv_text_pickrect = waveadv_text_pick.get_rect(midtop = (750, 215))
                    pistol_shoot.play()
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
        screen.blit(waves_bg, (0, 0))
        screen.blit(bullet_display, (cx - 50, cy - 60))
        for enem in wave_enemies:
            enem.move(enemy_speed)
            if enem.attacking():
                health -= 0.01
            if enem.timed_ani():
                enem.image_update()
            enem.draw()
        if len(wave_enemies) < wavelevelindicator.max_en and randint(1, 20) == 1:
            wave_enemies.append(choice((grunt(grunt_frames), grunt(grunt_frames), grunt(grunt_frames), midman(midman_frames), grunt(grunt_frames), grunt(grunt_frames), grunt(grunt_frames), midman(midman_frames), fatguy(fatso_frames))))
        cursorrect = target.get_rect(center = (cx, cy))
        screen.blit(target, cursorrect)
        gunrect = idle_gun.get_rect(midbottom=(cx, ty)) #rects next
        if reloading:
            screen.blit(gun_frames[gun_ani_index], reloadrect)
            gun_timer += 1
            if gun_timer >= anim_speed:
                gun_ani_index += 1
                gun_timer = 0
            if gun_ani_index >= len(gun_frames):
                gun_ani_index = 0
                bullets = ammo
                reloading = False
        if not reloading:
            screen.blit(gun_sprite, gunrect)
        if BAM:
            screen.fill('white') #bam flash
            bam_timer += 1
            if bam_timer >= bam_limit:
                BAM = False
                bam_timer = 0
        screen.blit(health_text, (110, 880))
        screen.blit(wave_display, (110, 920))
        screen.blit(enemies_left_display, (110, 960))
        if health <= 0:
            lives -= 1
            health = max_health
            if lives <= 0:
                state = 'lostwavemode'
                death_sft.play()
                target_diameter = 64
                target = pygame.transform.scale(target, (target_diameter, target_diameter))
            else:
                ahh.play()
############################################# mode change #####################################################
    if state == 'lostwavemode':
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    state = 'waves'
                    gun = 'pistol'
                    health = 100
                    bullets = 9
                    wave_enemies = []
                    wavelevelindicator = wavelevel()
                    perks = []
                    damage = 1
                    ammo = 9
                    lives = 1
                    enemy_speed = 4
                    max_health = 100
                    target_diameter = 64
                    target = pygame.transform.scale(target, (target_diameter, target_diameter))
                if event.key == pygame.K_w:
                    state = 'menu'
        screen.fill('black')
        screen.blit(youlose, loserect)
        screen.blit(menu_or_pgain, menu_pgainrect)
############################################# mode change #####################################################
    if state == 'wavemodeadvance':
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = 'waves'
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pistol_shoot.play()
                for per in perks:
                    if cursorrect.colliderect(per.imagerect):
                        state = 'waves'
                        wave_advance.play()
                        if per.should_increase_damage():
                            damage = per.increase(damage, 1.5)
                            print(f'damage: {damage}')
                        if per.should_increase_ammo():
                            ammo = per.increase(ammo, 1.5)
                            print(f'ammo: {ammo}')
                        if per.should_increase_lives():
                            lives += 1
                            print(f'lives: {lives}')
                        if per.should_increase_slow():
                            enemy_speed = per.increase(enemy_speed, 0.75)
                            print(f'speed: {enemy_speed}')
                        if per.should_increase_health():
                            max_health = int(max_health*1.15)
                            health += int((max_health - health) / 2)
                            print(f'max health: {max_health}')
                            print(f'health: {health}')
                        if per.should_increase_size():
                            target_diameter = int(target_diameter*1.5)
                            target = pygame.transform.scale(target, (target_diameter, target_diameter))
                        #Here is the part where you do per.apply()
        screen.blit(waveadv_bg, (0, 0))
        screen.blit(waveadv_text, waveadv_textrect)
        screen.blit(waveadv_text_pick, waveadv_text_pickrect)
        for perk in perks:
            perk.draw()
        cx, cy = pygame.mouse.get_pos()
        cursorrect = target.get_rect(center = (cx, cy))
        screen.blit(target, cursorrect)
############################################# mode change #####################################################
    if state == 'pausewavemode':
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    state = 'waves'
                    pause_sft.stop()
                    unpause_sft.play()
        screen.blit(pause_bg, (0, 0))
        screen.blit(health_text, (110, 800))
        screen.blit(wave_display, (110, 840))
        screen.blit(enemies_left_display, (110, 880))
        screen.blit(pausemenutext, pausemenutextrect)
#end
pygame.quit()
quit()