import pygame, consts

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked = consts.started, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        self.fps = 10
        self.currentScene = 1

    def capitalCheck(self, char):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if char == letter:
                return True
        
    def dialogue(self, text, color):
        j = 0
        speed = int(len(text) / 3 * 100)
        posY = int(self.height * 0.5)
        posX = int(self.width * 0.5 - 30)
        for i in range(0, len(text)):
            if self.capitalCheck(text[i]):
                j += 14
            else:
                j += 15
            self.createText(text[i], self.dialogueFont, color, self.window, posX + j, posY)
            pygame.display.update()
            pygame.time.wait(speed)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
    
    def loadingScreen(self, sceneNumber):
        self.window.fill(self.black)
        pygame.time.delay(500)
        self.dialogue("Scene " + str(sceneNumber), self.white)

    def gameLoop(self):
        self.loadingScreen(self.currentScene)
        while self.playing:
            self.window.fill(self.white)
            self.gameCursor()
            self.events()
            self.dialogue("ldasjfkl;sajdl;fkja;skldfjoiweohjlvcnbdjkupwert", self.purple)
            pygame.display.update()
            self.clock.tick(self.fps)