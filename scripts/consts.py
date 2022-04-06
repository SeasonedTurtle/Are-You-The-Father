import pygame, paths
from sys import exit

started = False

class Constants(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Create Performance Task")
        self.width, self.height = 810, 810
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.purple = (106, 13, 173)
        self.colors = [(216,191,216), (221,160,221), (40, 0, 255), (85, 0, 255), (128, 0, 255), (175, 0, 255), (238,130,238), (255, 0, 255)]
        self.font = paths.styles + "Inconsolata-Regular.ttf"
        self.textboxSize = int(125 * 0.25)
        self.textboxFont = pygame.font.Font(self.font, self.textboxSize)
        self.icon = pygame.image.load(paths.styles + "ICON.png")
        self.window = pygame.display.set_mode((self.width, self.height)) 
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(self.icon)
        pygame.mouse.set_visible(False)
        self.cursor = pygame.image.load(paths.styles + "download.png").convert()
        self.frames = []

    def quit(self):
        pygame.font.quit()
        pygame.quit()
        exit()

    def createText(self, text, font, color, target, posX, posY):
        text = font.render(text, 1, color)
        textBox = text.get_rect()
        textBox.topleft = (posX, posY)
        target.blit(text, textBox)             

    def gameCursor(self):
        cursorRect = self.cursor.get_rect()
        cursorRect.center = pygame.mouse.get_pos()
        self.window.blit(self.cursor, cursorRect)
        pygame.display.flip()
    
    # Path will need to change once more directories are added
    def initScenes(self, frames, fileAmount):
        for i in range(0, fileAmount):
            frames.append(pygame.image.load(paths.scenes + "images" + str(i) + ".jpg").convert())
        return frames