import pygame, sys, os

pygame.init()
pygame.font.init()

width = 810
height = 810

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (106, 13, 173)

path = os.getcwd() + os.sep
font = path + "styles/LeagueSpartan-Bold.otf"
icon = pygame.image.load(path + "styles/ICON.png")

started = False

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.display.set_caption("Create Performance Task")
pygame.display.set_icon(icon)

cursor = pygame.image.load(path + "styles/download.png").convert()

def quit():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

def createText(text, font, color, target, posX, posY):
    text = font.render(text, 1, color)
    textBox = text.get_rect()
    textBox.topleft = (posX, posY)
    target.blit(text, textBox)             

def gameCursor():
    _clock = pygame.time.Clock()
    cursorRect = cursor.get_rect()
    cursorRect.center = pygame.mouse.get_pos()
    window.blit(cursor, cursorRect)
    pygame.display.flip()
    _clock.tick(30)