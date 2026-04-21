#shoot to kill
#code
import pygame #module with screens, and sfx, and imgs and stuff
import sys
from random import choice, randint #randint, best god damn thing ever, I love you randint.
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
pygame.init()
from Assets.img.surfaces import *
from Assets.img.texts import *
from Assets.sfx.sounds import *
version = 'v1.4.5'
def main():
    global target
    global version
    #pygame.init()
    clock = pygame.time.Clock()
    running = True
    #other vars
    BAM = False
    bam_timer = 0
    bam_limit = 3
    reloading = False
    gun_ani_index = 0
    gun_timer = 0
    anim_speed = 5
    tx, ty = 750, 1000
    gx, gy = 750, 500
    gun_sprite = idle_gun
    NO_MOUSE_IS_NOT_FUCKING_VISIBLE = False
    pygame.mouse.set_visible(NO_MOUSE_IS_NOT_FUCKING_VISIBLE)
    bullets = 9
    ar_trigger_powerup = special_gun_trigger(ar_target)
    ar_timer = 0
    ar_end = 120
    ar_active = False
    ar_bullet_timer = 0
    ar_bullet_limit = 10
    combo_level = 0
    combo_timer = 0
    combo_limit = 60
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
    text = font.render(version, True, 'white')
    while running:
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
                hole.draw(screen)
            screen.blit(target, cursorrect) # target last
    ############################################# mode change #####################################################
        if state == 'training':
            clock.tick(60) #refresh rate, 60 fps
            bullet_display = font.render(f"{bullets} bullets", True, 'black')
            gun_display = font.render(f"gun: {gun}", True, 'black')
            score_display = font.render(f"score: {score}", True, 'black')
            screen.fill('grey') #bg first
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
                    if event.key == pygame.K_s and not reloading and gun != 'assault rifle' or event.type == pygame.MOUSEBUTTONDOWN and not reloading and gun != 'assault rifle':
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
                        if gun == 'rocket launcher':
                            explosions.append(explosion(cx, cy, explo_frames))
                            kablooey = True
                            kablooeysound.play()
                            BAM = True
                        if gun == 'pistol' and not reloading:
                            pistol_shoot.play()
                        if bullets <= 0 and gun != 'pistol':
                            gun = 'pistol'
                            weapon_change.play()
                """if event.type == pygame.MOUSEBUTTONDOWN and not reloading and gun != 'assault rifle':
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
                        pistol_shoot.play()""" # Ancient Dev code preserved in amber!!!
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
            for smk in smokeholes:
                smk.draw(screen)
                smk.fade()
                if smk.alpha <=0:
                    smokeholes.remove(smk)
            for ex in explosions:
                ex.draw(screen)
                ex.adv()
                if ex.index == 6:
                    smokeholes.append(smokehole(ex.x, ex.y, smoke))
                if ex.is_adv():
                    explosions.remove(ex)
            gunrect = gun_sprite.get_rect(midbottom=(cursorrect.centerx, ty)) #rects next
            reloadrect = gun_frames[gun_ani_index].get_rect(midbottom=(cx, ty))
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()
            if keys[pygame.K_s] and gun == 'assault rifle' or any(mouse) and gun == 'assault rifle': #left click + rifle
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
                                            perks.append(perk_image(choice(perk_images), i, perk_images, font2))
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
                enem.draw(screen)
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
                perk.draw(screen)
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
    sys.exit()
