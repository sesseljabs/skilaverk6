from dicethrower import DiceThrower
import pygame
from pygame.locals import *

pygame.init()

img_location = "img/"
img_name = "Dice-%s.png"
img = img_location+img_name

dice = [pygame.image.load(img % i) for i in range(7)]
for i in range(7):
    dice[i] = pygame.transform.scale(dice[i],(90,90))

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Teningar")

class Player:
    def __init__(self, dice=5):
        self.dicelist = [0 for i in range(dice)]

    def result(self):
        return sum(self.dicelist)

def font_render(text):
    return font.render(text, 1, ((255,255,255)))

computer = Player()
player = Player()

throwerComp = DiceThrower()
throwerPlayer = DiceThrower()

font = pygame.font.Font("freesansbold.ttf", 25)

playButton = Rect(10,300,140,30)
playText = font.render("Play", 1, ((255,255,255)))

throwAllButton = Rect(100,300,140,30)
throwAllText = font.render("Throw all", 1, ((255,255,255)))

throwOneButton = Rect(250,300,140,30)
throwOneText = font.render("Throw one", 1, ((255,255,255)))

resultText = font.render("uwu", 1, ((255,255,255)))
resultTextBox = Rect(10,400,600,30)

game = False
gameOver = False

def endGame(computer, player):
    result = f"Computer {computer.result()}, You: {player.result()}"
    winner = ""
    if computer.result() > player.result():
        winner = "The computer wins"
    elif computer.result() < player.result():
        winner = " You win"
    elif computer.result() == player.result():
        winner = "Tie"

    return result+". "+winner

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and playButton.collidepoint(event.pos):
            if game == False:
                player.dicelist = throwerPlayer.throw()
                computer.dicelist = throwerComp.throw()
                gameOver = False

            game = True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and throwAllButton.collidepoint(event.pos) and game:
            player.dicelist = throwerPlayer.throw()
            resultText = font_render(endGame(computer,player))
            gameOver = True
            game = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and throwOneButton.collidepoint(event.pos) and game:
            resultText = font_render(endGame(computer,player))
            gameOver = True
            game = False

        screen.fill((255,255,255))

        for i in range(5):
            screen.blit(dice[computer.dicelist[i]], ((i*100+10), (10)))

        for i in range(0,4):
            screen.blit(dice[player.dicelist[i]], ((i*100+10), (110)))

        if gameOver:
            screen.blit(dice[player.dicelist[i]], ((410), (110)))
        else:
            screen.blit(dice[0], ((410), (110)))

        pygame.draw.rect(screen, (255,0,0), playButton)
        screen.blit(playText, playButton)

        pygame.draw.rect(screen, (255,0,0), throwAllButton)
        screen.blit(throwAllText, throwAllButton)

        pygame.draw.rect(screen, (255,0,0), throwOneButton)
        screen.blit(throwOneText, throwOneButton)

        if gameOver:
            pygame.draw.rect(screen, (60,200,150), resultTextBox)
            screen.blit(resultText, resultTextBox)

        pygame.display.update()
