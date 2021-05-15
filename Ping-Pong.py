from pygame import *

from random import randint

from time import time as timer

font.init()



class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_width
        self.height = player_height


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
    
    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 445:
            self.rect.y += self.speed


rocket1 = Player("rocket.png", 5, 250, 10, 50, 150)
rocket2 = Player("rocket.png", 645, 250, 10, 50, 150)

ball = GameSprite("ball.png", 330, 230, 5, 40, 40)

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')

background = transform.scale(image.load("Ping-Pong.jpg"),(700, 500))

clock = time.Clock()
FPS = 60 

game = True
finish = False

font = font.SysFont("Arial", 40)

win1 = font.render('Player 1 wins!', True, (255, 0, 0))
win2 = font.render('Player 2 wins!', True, (255, 0, 0))


while game:
    
    for e in event.get():
        
        if e.type == QUIT:
            game = False

    if finish != True:
        
        window.blit(background, (0, 0))
        clock.tick(FPS)

        if ball.rect.x < 0:
            window.blit(win2, (290, 230))
            finish = True

        elif ball.rect.x > 500:
            window.blit(win1, (290, 230))
            finish = True

        rocket1.reset()
        rocket2.reset()
        ball.reset()

        rocket1.update2()
        rocket2.update1()
        ball.update()

        display.update()
