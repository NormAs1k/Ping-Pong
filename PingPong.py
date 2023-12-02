from random import *
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > -5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > -5:
            self.rect.y += self.speed

rocket1 = Player("rocket.jpg", 25, 200, 30, 150, 5)
rocket2 = Player("rocket.jpg", 550, 200, 30, 150, 5)
ball = GameSprite("ball.png", 200, 200, 50, 30, 5)

speed_x = 4
speed_y = 4

background = (200,200,255)
win_width = 600
win_height = 500
display.set_caption('Ping-Pong')
window = display.set_mode((win_width, win_height))
window.fill(background)

font.init()
font = font.Font(None, 36)
lose_1 = font.render('Левый проиграл', True, (255,100,100))
lose_2 = font.render('Правый проиграл', True, (255,100,100))

game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_2, (200, 200))
            game_over = True

        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(60)