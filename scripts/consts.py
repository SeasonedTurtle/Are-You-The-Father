import pygame, sys, paths

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
        self.font = paths.styles + "LeagueSpartan-Bold.otf"
        self.icon = pygame.image.load(paths.styles + "ICON.png")
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(self.icon)
        pygame.mouse.set_visible(False)
        self.cursor = pygame.image.load(paths.styles + "download.png").convert()

    def quit(self):
        pygame.font.quit()
        pygame.quit()
        sys.exit()

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