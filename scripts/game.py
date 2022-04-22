import pygame, consts, paths

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked, self.showOptions = consts.started, False, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        self.fps = 10
        self.currentScene = 1
        self.points = 0
        self.leftButton = pygame.Rect(0, self.height - 100, self.width * 0.5, self.height - 200)
        self.rightButton = pygame.Rect(self.width * 0.5, self.height - 100, self.width, self.height - 200)
        self.textBackground = pygame.Rect(0, self.height - 100, self.width, self.height - 200)
        self.on = True

    def gameFlow(self):
        self.events()
        pygame.display.update()

    def dialogue(self, text, posX, posY, color, offset):
        j = 0
        speed = int(len(text) / self.fps * 100) - offset
        for i in range(0, len(text)):
            j += 10
            self.createText(text[i], self.dialogueFont, color, self.window, posX + j, posY)
            self.gameFlow()
            pygame.time.delay(speed)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True

    def loadingScreen(self, sceneNumber):
        self.window.fill(self.black)
        pygame.time.delay(500)
        self.dialogue("Scene " + str(sceneNumber), 300, 300, self.white, 0)
        pygame.time.delay(250)

    def tutorial(self):
        self.dialogue("You play as Tyrone,", 0, 0, self.white, 125)
        self.dialogue("the alleged father.", 200, 0, self.white, 125)
        self.dialogue("To win the game you", 0, 50, self.white, 125)
        self.dialogue("must stall enough  ", 200, 50, self.white, 125)
        self.dialogue("time to have your  ", 380, 50, self.white, 125)
        self.dialogue("friend change the  ", 560, 50, self.white, 125)
        self.dialogue("dna sample so you  ", 0, 75, self.white, 125)
        self.dialogue("are not recognized ", 180, 75, self.white, 125)
        self.dialogue("as the father.     ", 370, 75, self.white, 125)
        self.dialogue("Tip: Stall longer by", 0, 150, self.white, 125)
        self.dialogue("picking reasonable ", 210, 150, self.white, 125)
        self.dialogue("options!", 400, 150, self.white, 125)
        pygame.time.delay(1500)

    def options(self):
        pygame.draw.rect(self.window, self.blue, self.leftButton)
        self.createText("Option 1", self.textboxFont, self.black, self.window, 0, 750)
        pygame.draw.rect(self.window, self.purple, self.rightButton)
        self.createText("Option 2", self.textboxFont, self.black, self.window, self.width * 0.5, 750)

    def mouseInput(self, correctChoice):
        self.gameCursor()
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.leftButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            if correctChoice == "left":
                self.points += 2
            else:
                self.points -= 1
        elif self.rightButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            if correctChoice == "right":
                self.points += 2
            else:
                self.points -= 1
        else:
            self.clicked = False

    def intro(self, posX, posY, character):
        self.window.fill(self.white)
        character.get_rect().center = (posX, posY)
        self.window.blit(character, character.get_rect())
        pygame.display.flip()
        pygame.draw.rect(self.window, (220, 220, 220), self.textBackground)

        if character == self.ZAYM:
            self.dialogue("I am not the father!", 200, 750, self.purple, 125)
            self.dialogue("She just wants my   ", 420, 750, self.purple, 125)
            self.dialogue("money!  ", 600, 750, self.purple, 125)
        else:
            self.dialogue("I know he the father!", 0, 750, self.purple, 125)
            self.dialogue("He just does not want", 220, 750, self.purple, 125)
            self.dialogue("to pay up!  ", 440, 750, self.purple, 100)

        pygame.time.delay(600)

    def pointSystem(self):
        if self.currentScene == 1:
            self.mouseInput("right")
        elif self.currentScene == 2:
            self.mouseInput("right")
        elif self.currentScene == 3:
            self.mouseInput("left")
        elif self.currentScene == 4:
            self.mouseInput("right")
        else:
            self.mouseInput("left")

    def talking(self, text, posX, posY, color, offset, pos1X, pos1Y, list):
        j = 0
        frame = 0
        if self.on:
            speed = int(len(text) / self.fps * 100) - offset
            pygame.draw.rect(self.window, (220, 220, 220), self.textBackground)
            for i in range(0, len(text)):
                j += 10
                frameRect = list[frame].get_rect()
                frameRect.center = (pos1X, pos1Y)
                self.window.blit(list[frame], frameRect)
                self.createText(text[i], self.dialogueFont, color, self.window, posX + j, posY)
                self.gameFlow()
                if i % 2 != 0:
                    frame += 1
                else:
                    frame = 0
                pygame.time.delay(speed)
        pygame.time.delay(500)

    def gameLoop(self):
        self.initScenes(paths.tyroneV1, "Tyrone", "V1", "serious ", self.tyroneV1)
        #self.tutorial()
        #self.intro(50, 800, self.moniqueIntro)
        #self.intro(50, 800, self.ZAYM)
        self.loadingScreen(self.currentScene)
        while self.playing:
            self.window.fill(self.white)
            #self.options()
            self.pointSystem()
            if self.on:
                self.talking("I am not the father!", 200, 750, self.purple, 125, 500, 200, self.tyroneV1)
            self.on = False
            self.gameFlow()
            self.clock.tick(self.fps)
