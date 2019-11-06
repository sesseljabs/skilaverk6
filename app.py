import pygame
import random
from os import path
from pygame.locals import (
    QUIT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    RLEACCEL
)

# Fastar fyrir location, nafnið á myndunum og fleira
img_location = "img/"
img_name = "Dice-%s.png"
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Dice:
    def __init__(self):
        self.number = 0
        self.surf = pygame.image.load(path.join(img_location,img_name % self.number))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)  # Gerir það transparent fyrir png mynd
        self.surf = pygame.transform.scale(self.surf,(100,100))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(100,50)

    def __str__(self):
        return f"{self.number}"

    def throw(self):
        self.number = random.randint(1,6)
        self.image = img_name % self.number
        self.surf = pygame.image.load(path.join(img_location, img_name % self.number))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)  # Gerir það transparent fyrir png mynd
        self.surf = pygame.transform.scale(self.surf, (50, 50))

class DiceThrower:
    def __init__(self, total=5):
        self.dice_count = total
        self.dice = Dice()
        self.dice_list = [Dice() for i in range(self.dice_count)]

    def __str__(self):
        li = [i.number for i in self.dice_list]
        return str(li)

    def throw(self, howmany=5): # full throw = 5,  all but one throw = 4
        if howmany > len(self.dice_list): # if this is bullshit make it the length of dice list
            howmany = len(self.dice_list)

        for i in range(0, howmany):
            self.dice_list[i].throw()

    def throwlast(self):
        self.dice_list[-1].throw()

    def counttotal(self):
        total = 0
        for i in self.dice_list:
            total += i.number

        return total


uwu = DiceThrower()
print(uwu)

uwu.throw(4)
print(uwu)
uwu.throwlast()
print(uwu)
print(uwu.counttotal())
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[K_SPACE]:
        uwu.dice_list[2].throw()

    screen.fill((0, 255, 255))

    #for i in uwu.dice_list:
     #   screen.blit(i.surf,i.rect)
    screen.blit(uwu.dice_list[2].surf,uwu.dice_list[2].rect)
    pygame.display.flip()

    clock.tick(30)