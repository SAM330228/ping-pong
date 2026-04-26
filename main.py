#1. Подключи игровую библиотеку pygame.
from pygame import*
#2. Создай окно игры размером 700x500, дай ему название.
finish = False
x = 700
y = 500
window = display.set_mode((x, y))
display.set_caption('Ping pong')
background = transform.scale(image.load("111.png"), (x, y))
font.init()
font1 = font.SysFont('Arial', 36)
#3. Музыка
mixer.init()
#!mixer.music.load('')
#!mixer.music.play()
#4. Создай и отобрази спрайты для игрока и врага.
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#player
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y < y - 5:
            self.rect.y -= self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y < y - 5:
            self.rect.y -= self.speed

speed_x = 3
speed_y = 3

class Ball(GameSprite):
    def balls(self):
        self.rect.x + speed_x
        self.rect.y + speed_y
        if self.rect.x <= 0:
            loser1 = font1.render('Игрок 1 проиграл', True, (255, 0, 0))
            finish = True
        if self.rect.x >= 700:
            loser2 = font1.render('Игрок 2 проиграл', True, (255, 0, 0))
            finish = True
        if self.rect.colliderect(Racket1):
            self.rect.x *= -1
            self.rect.y *= -1
        if self.rect.colliderect(Racket2):
            self.rect.x *= -1
            self.rect.y *= -1
#! id diktui!1!!1! daniil kolbacenko! kto kto?
#Alt + f4
Racket1 = Player('Raket1.jpg', 600, 200, 5)
Racket2 = Player('Raket1.jpg', 50, 200, 5)
bball = Ball('OIP.webp', 150, 350, None)
#5. Создай игровой цикл с выходом при нажатии на «Закрыть окно».
game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))

    Racket1.update_l()
    Racket1.reset()

    Racket2.update_r()
    Racket2.reset()

    bball.balls()
    bball.reset()

    display.update()
    clock.tick(fps)
