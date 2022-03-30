import pygame 
import consts as const

class Game():
    def __init__(self):
        self.playing, self.clicked = const.started, False

    def gameLoop(self):
        while self.playing:
            const.window.fill(const.black)
            const.gameCursor()
            self.events()
            pygame.display.update()
            const.clock.tick(const.fps)
            self.clicked = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                const.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked = True