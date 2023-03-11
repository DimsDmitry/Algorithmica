from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')

#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))

#создай 2 спрайта и размести их на сцене
x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
speed = 10

#создаём игровой цикл

run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    '''движения спрайта calc get-запрос'''
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 595:
        y1 += speed

    '''движения спрайта 2'''
    if keys_pressed[K_a] and x1 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x1 < 595:
        x2 += speed
    if keys_pressed[K_w] and y1 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y1 < 595:
        y2 += speed

    if keys_pressed[K_p]:
        speed = 0
        background = transform.scale(image.load('pause.png'), (700, 500))
    if keys_pressed[K_l]:
        speed = 10
        background = transform.scale(image.load('background.png'), (700, 500))

    display.update()
    clock.tick(FPS)
#обработай событие «клик по кнопке "Закрыть окно"»