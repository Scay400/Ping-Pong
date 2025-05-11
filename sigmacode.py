from pygame import *
from random import *
import time as geforg 

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed 
        if keys_pressed[K_s] and self.rect.y<380:
            self.rect.y+=self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if keys_pressed[K_DOWN] and self.rect.y<380:
            self.rect.y+=self.speed



        
            
 

win_wight = 700
win_height = 500

window = display.set_mode((win_wight,win_height))
window.fill((0,255,0))
display.set_caption('Ping Pong')

background = transform.scale(image.load('background.png'),(win_wight,win_height))


x=10
y=10
x2 = 640
x1 = 450
y1 = 300
speed = 5


FPS = 120
game = True

clock = time.Clock()

player1 = Player('Player1.png',x,250,speed,40,150)
player2 = Player('Player2.png',x2,250,speed,40,150)

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

counter = 40*FPS
counter1 = 0

finish = False


while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        player1.reset()
        player2.reset()
        player1.update()
        player2.update2()

    clock.tick(FPS)
    display.update()
