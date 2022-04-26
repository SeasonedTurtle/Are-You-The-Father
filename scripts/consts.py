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
        self.red = (255, 0, 0)
        self.purple = (106, 13, 173)
        self.colors = [(216,191,216), (221,160,221), (40, 0, 255), (85, 0, 255), (128, 0, 255), (175, 0, 255), (238,130,238), (255, 0, 255)]
        self.font = paths.fonts + "Inconsolata-Regular.ttf"
        self.textboxSize = int(125 * 0.25)
        self.textboxFont = pygame.font.Font(self.font, self.textboxSize)
        self.icon = pygame.image.load(paths.icons + "ICON.png")
        self.window = pygame.display.set_mode((self.width, self.height)) 
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(self.icon)
        pygame.mouse.set_visible(False)
        self.cursor = pygame.image.load(paths.icons + "download.png").convert()
<<<<<<< Updated upstream
        self.frames = []
        self.ZAYM = pygame.image.load(paths.images + "Tyrone ZAMN-1.jpg").convert()
=======
        self.ZAYM = pygame.image.load(paths.images + "Tyrone ZAMNV1.jpg").convert()
>>>>>>> Stashed changes
        self.moniqueIntro = pygame.image.load(paths.images + "Sheniqua Angry.jpg").convert()

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
<<<<<<< Updated upstream
    def initScenes(self, frames, fileAmount, character):
        for i in range(0, fileAmount):
            frames.append(pygame.image.load(paths.scenes + character + ".png").convert())
        return frames
=======
    def initScenes(self, path, character, version, emotion, list):
        for i in range(0, 2):
            img = (pygame.image.load(path + character + version + " talking " + emotion + str(i) + " tr.png").convert_alpha())
            list.append(img)
        return list
>>>>>>> Stashed changes
