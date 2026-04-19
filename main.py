#1. Подключи игровую библиотеку pygame.
from pygame import*
#2. Создай окно игры размером 700x500, дай ему название.
x = 700
y = 500
window = display.set_mode((x, y))
display.set_caption('Ping pong')
background = transform.scale(image.load("Minecraft.jpg"), (x, y))
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.x += self.speed
        if keys[K_s] and self.rect.y < y - 80:
            self.rect.x -= self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < y - 80:
            self.rect.x -= self.speed
#Alt + f4
Racket1 = Player('Racket1.png', 600, 400, 5)
Racket2 = Player('Racket2t.png', 50, 400, 5)
#5. Создай игровой цикл с выходом при нажатии на «Закрыть окно».
game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))

    Racket1.update()
    Racket1.reset()

    Racket2.update()
    Racket2.reset()

    display.update()
    clock.tick(fps)
