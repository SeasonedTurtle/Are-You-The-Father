import pygame, consts

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked = consts.started, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        self.fps = 10
        self.currentScene = 1
    
    def gameFlow(self):
        self.events()
        pygame.display.update()
        
    def dialogue(self, text, posX, posY, color):
        j = 0
        speed = int(len(text) / self.fps * 100)
        for i in range(0, len(text)):
            j += 10
            self.createText(text[i], self.dialogueFont, color, self.window, posX + j, posY)
            self.gameFlow()
            pygame.time.wait(speed)

    def animate(self, frames, posX, posY):
        for frame in frames:
            frameRect = frame.get_rect()
            frameRect.center = (posX, posY)
            self.window.blit(frame, frameRect)
            self.gameFlow()
            pygame.display.flip()
            pygame.time.wait(300)

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
        self.dialogue("Scene " + str(sceneNumber), 300, 300, self.white)

    def statement(self):
        self.dialogue("Gulp Gulp Gulp", 0, 100, self.purple)
        self.dialogue("Move Move Please", 100, 200, self.purple)
        self.dialogue("Hurt That Mouth", 200, 300, self.purple)

    def gameLoop(self):
        self.initScenes(self.frames)
        self.loadingScreen(self.currentScene)
        count = 0
        while self.playing:
            self.window.fill(self.white)
            self.gameCursor()
            self.gameFlow()
            self.animate(self.frames, 300, 300)
            if not count:
                self.statement()
            count += 1
            self.clock.tick(self.fps)