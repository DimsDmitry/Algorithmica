#Создай собственный Шутер!
from pygame import *
from random import randint

from time import time as timer


'''создаём окно'''
win_width = 700
win_height = 500
display.set_caption('Космическая баталия')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))


'''фоновая музыка'''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

'''шрифты и надписи'''
font.init()
font1 = font.SysFont(None, 80)
win = font1.render('ПОБЕДА', True, (255, 255, 255))
lose = font1.render('ПОРАЖЕНИЕ', True, (180, 0, 0))
font2 = font.SysFont(None, 36)

score = 0  # сбито кораблей
lost = 0  # пропущено кораблей
max_lost = 3  # проиграли, если пропустили столько кораблей
goal = 30  # столько кораблей нужно сбить для победы
life = 3  # здоровье


class GameSprite(sprite.Sprite):
    '''класс-родитель для других спрайтов'''
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        '''каждый спрайт хранит изображение'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        '''каждый спрайт - прямоугольник rectangle'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        '''отрисовка героя на окне'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс главного игрока'''
    def update(self):
        '''метод для управления спрайтом'''
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        '''стрельба'''
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    '''класс спрайта-врага'''
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Asteroids(GameSprite):
    '''класс для астероидов'''
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(30, win_width - 30)
            self.rect.y = 0


class Bullet(GameSprite):
    '''класс спрайта-пули'''
    def update(self):
        '''движение пули'''
        self.rect.y += self.speed
        '''исчезает, дойдя до края экрана'''
        if self.rect.y < 0:
            self.kill()



'''создаём спрайты'''
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)
#player_image, player_x, player_y, size_x, size_y, player_speed

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)


asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Asteroids('asteroid.png', randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)


bullets = sprite.Group()


'''переменная "игра закончилась"'''
finish = False
'''Основной цикл игры:'''
run = True

num_fire = 0  #переменная для подсчёта количества выстрелов
rel_time = False #флаг, отвечающий за перезарядку

while run:
    for e in event.get():
        '''нажатие кнопки "закрыть":'''
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                '''проверим, сколько выстрелов сделано'''
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

    if not finish:
        '''обновляем фон'''
        window.blit(background, (0, 0))

        '''пишем текст на экране'''
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        '''движения спрайтов'''
        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()
        '''обновляем местоположение спрайтов'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        '''перезарядка'''
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                '''если не прошло 3 секунды, выводим сообщение о перезарядке'''
                reload = font2.render('Подождите, перезарядка...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False


        '''проверка столкновения пули и монстров'''
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)


        '''если спрайт коснулся врага, уменьшаем жизнь'''
        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
            sprite.spritecollide(ship, monsters, True)
            sprite.spritecollide(ship, asteroids, True)
            life -= 1


        '''поражение'''
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))


        '''победа'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))


        display.update()
    time.delay(50)