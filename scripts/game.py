import pygame 
import consts as const

class Game():
    def __init__(self):
        self.playing, self.clicked = const.started, False
        self.dialogueFont = pygame.font.Font(const.font, 25)
        self.fps = 10

    def dialogue(self, text):
        j = 0
        speed = int(len(text) / 10 * 300)
        posY = int(const.height * 0.5)
        posX = int(const.width * 0.5 - 30)
        for i in range(0, len(text)):
            j += 15
            if text[i] == "\n":
                const.createText(text[i], self.dialogueFont, const.white, const.window, posX + j, posY + j)
            else:
                const.createText(text[i], self.dialogueFont, const.white, const.window, posX + j, posY)
            pygame.display.update()
            pygame.time.wait(speed)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                const.quit()
            elif event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    const.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
    
    def gameLoop(self):
        const.window.fill(const.black)
        pygame.time.delay(500)
        self.dialogue("Scene 1")
        while self.playing:
            const.window.fill(const.white)
            const.gameCursor()
            self.events()
            pygame.display.update()
            const.clock.tick(self.fps)
            self.clicked = False