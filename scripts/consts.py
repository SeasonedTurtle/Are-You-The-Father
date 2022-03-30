import pygame, time, sys, os

pygame.init()
pygame.font.init()

width = 810
height = 810
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
fps = 10
path = os.getcwd() + os.sep
font = path + "styles/LeagueSpartan-Bold.otf"
icon = pygame.image.load(path + "styles/ICON.png")

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.display.set_caption("Create Performance Task")
pygame.display.set_icon(icon)

cursor = pygame.image.load(path + "styles/download.png").convert()
cursorRect = cursor.get_rect()

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
    cursorRect.center = pygame.mouse.get_pos()
    window.blit(cursor, cursorRect)
    pygame.display.flip()

def talking(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        if (char == "\n"):
            time.sleep(1)
        else:
            time.sleep(0.4)