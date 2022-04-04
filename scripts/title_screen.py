import pygame, random, consts

class mainMenu(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.backgroundColor = (200, 200, 200)
        self.textColor = self.black
        self.buttonColor = self.white
        self.titleSize = 125
        self.subtitleSize = int(self.titleSize * 0.3)
        self.textboxSize = int(self.titleSize * 0.25)
        self.bigFont = pygame.font.Font(self.font, self.titleSize)
        self.smallFont = pygame.font.Font(self.font, self.subtitleSize)
        self.textboxFont = pygame.font.Font(self.font, self.textboxSize)
        self.running, self.clicked = True, False
        self.startButton = pygame.Rect(self.width * 0.5 - 100, self.height * 0.5 + 150, self.width * 0.25, self.height * .0625)
        self.quitButton = pygame.Rect(self.width * 0.5 - 100, self.height * 0.5 + 220, self.width * 0.25, self.height * .0625)
        self.color = self.blue
        self.colors = [(216,191,216), (221,160,221), (40, 0, 255), (85, 0, 255), (128, 0, 255), (175, 0, 255), (238,130,238), (255, 0, 255)]

    def drawCircles(self):
        count = 0
        circleSize = 30
        now = self.clock.tick(30)

        for x in range(25, self.width - 25, circleSize):
            for y in range(25, self.height - 25, circleSize):
                if now % 2:
                    self.color = self.colors[random.randint(0, 7)]
                pygame.draw.circle(self.window, self.color, (x, y), 2, 2)
        pygame.time.wait(75)

    def gui(self):
        self.createText("Are YOU", self.bigFont, self.textColor, self.window, 100, 50)
        self.createText("The Father?", self.bigFont, self.textColor, self.window, 45, 300)
        self.createText("A Family Game", self.smallFont, self.textColor, self.window, 50, self.height * 0.5 + 75)
        
        pygame.draw.rect(self.window, self.buttonColor, self.startButton)
        pygame.draw.rect(self.window, self.buttonColor, self.quitButton)

        self.createText("Start Game", self.textboxFont, self.textColor, self.window, self.width * 0.5 - 100, self.height * 0.5 + 150)
        self.createText("Quit Game", self.textboxFont, self.textColor, self.window, self.width * 0.5 - 100, self.height * 0.5 + 220)
        
    def mouseInput(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.startButton.collidepoint((mouseX, mouseY)) and self.clicked:
                self.running = False
                consts.started = True
        elif self.quitButton.collidepoint((mouseX, mouseY)):
            if self.clicked:
                self.quit()
        else:
            self.clicked = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True

    def main(self): 
        while self.running:
            self.window.fill(self.backgroundColor)
            self.drawCircles()
            self.gui()
            self.gameCursor()
            self.mouseInput()
            self.events()
            pygame.display.update()