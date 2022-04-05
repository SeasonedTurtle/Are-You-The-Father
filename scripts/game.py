import pygame, consts, random

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked = consts.started, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        self.fps = 10
        self.currentScene = 1
        self.points = 0
        self.leftButton = pygame.Rect(0, self.height - 100, self.width * 0.5, self.height - 200)
        self.rigthButton = pygame.Rect(self.width * 0.5, self.height - 100, self.width, self.height - 200)
    
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
    
    def loadingScreen(self, sceneNumber):
        self.window.fill(self.black)
        pygame.time.delay(500)
        self.dialogue("Scene " + str(sceneNumber), 300, 300, self.white)
        pygame.time.delay(250)

    def statement(self):
        self.dialogue("Gulp Gulp Gulp", 0, 100, self.purple)
        self.dialogue("Move Move Please", 100, 200, self.purple)
        self.dialogue("Hurt That Mouth", 200, 300, self.purple)

    def drawLines(self):
        pi = 3.14
        posX, posY = -100, -100
        for i in range(10):
            color = self.colors[random.randint(0, 7)]
            posX += 25
            pygame.draw.arc(self.window, color, [posX, posY, self.width, self.height], pi, pi/3, 10)

    def options(self):
        pygame.draw.rect(self.window, self.purple, self.leftButton)
        self.createText("Option 1", self.textboxFont, self.black, self.window, 0, 750)

    def mouseInput(self, correctChoice):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.leftButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            if correctChoice == "left":
                self.points += 2
            else:
                self.points -= 1
        elif self.leftButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            if correctChoice == "right":
                self.points += 2
            else:
                self.points -= 1
        else:
            self.clicked = False

    def gameLoop(self):
        self.initScenes(self.frames)
        self.loadingScreen(self.currentScene)
        count = 0
        while self.playing:
            self.window.fill(self.white)
            self.gameCursor()
            #if not count:
            #    self.statement()
            if self.points > 0:
                self.animate(self.frames, 300, 300)
                self.drawLines()
            self.options()
            self.mouseInput("left")
            print(self.points)
            self.gameFlow()
            count += 1
            self.clock.tick(self.fps)