
# создай игру "Лабиринт"!
from pygame import *

'''класс для создания спрайтов'''


class GameSprite(sprite.Sprite):
    '''конструктор класса'''

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        '''каждый спрайт вписан в прямоугольник'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс- наследник для спрайта игрока (перемещение стрелками)'''

    def update(self):
        '''движение игрока'''
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    '''класс- наследник для спрайта игрока (перемещается сам)'''
    direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    '''класс-стена'''

    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3),
                  (self.rect.x, self.rect.y, self.width, self.height))


'''Игровая сцена'''
win_width = 700
win_height = 500

'''Окно игры'''
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')

'''Фон сцены'''
background = transform.scale(image.load('background.jpg'), (700, 500))

'''Персонажи игры'''
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(136, 182, 117, 50, 100, 470, 7)
w2 = Wall(136, 182, 117, 50, 100, 350, 7)
w3 = Wall(136, 182, 117, 50, 100, 7, 280)
w4 = Wall(136, 182, 117, 145, 185, 7, 280)
w5 = Wall(136, 182, 117, 50, 100, 220, 7)
w6 = Wall(136, 182, 117, 145, 185, 90, 7)
w7 = Wall(136, 182, 117, 510, 214, 7, 251)
w8 = Wall(136, 182, 117, 230, 315, 185, 7)
w9 = Wall(136, 182, 117, 145, 460, 370, 7)
w10 = Wall(136, 182, 117, 315, 100, 7, 220)
w11 = Wall(136, 182, 117, 227, 190, 7, 45)
w12 = Wall(136, 182, 117, 230, 320, 7, 60)
w13 = Wall(136, 182, 117, 320, 405, 7, 53)
w14 = Wall(136, 182, 117, 410, 320, 7, 67)
w15 = Wall(136, 182, 117, 415, 215, 100, 7)

game = True
clock = time.Clock()
FPS = 60
finish = False

'''подключаем музыку'''
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)

'''текст для победы и поражения'''
win = font.render('Победа!', True, (251, 166, 168))
lose = font.render('Поражение!', True, (254, 0, 1))

'''игровой цикл'''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()

    '''проигрыш'''
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player,
                                                                                                      w2) or sprite.collide_rect(
            player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(
            player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(
            player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(
            player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(
            player, w15):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    '''Выигрыш'''
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)

