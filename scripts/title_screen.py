import sys, pygame
import consts as const

class mainMenu(object):
    def __init__(self):
        self.backgroundColor = (200, 200, 200)
        self.textColor = const.black
        self.buttonColor = const.white
        self.titleSize = 125
        self.subtitleSize = int(self.titleSize * 0.3)
        self.textboxSize = int(self.titleSize * 0.25)
        self.bigFont = pygame.font.Font(const.font, self.titleSize)
        self.smallFont = pygame.font.Font(const.font, self.subtitleSize)
        self.textboxFont = pygame.font.Font(const.font, self.textboxSize)
        self.running, self.clicked= True, False
        self.startButton = pygame.Rect(const.width * 0.5 - 100, const.height * 0.5 + 150, const.width * 0.25, const.height * .0625)
        self.quitButton = pygame.Rect(const.width * 0.5 - 100, const.height * 0.5 + 220, const.width * 0.25, const.height * .0625)

    def drawCircles(self):
        circleSize = 25
        now = pygame.time.get_ticks()

        for x in range(0, const.width, circleSize):
            for y in range(0, const.height, circleSize):
                if not now % 2:
                    color = const.red
                else:
                    color = const.blue  
                pygame.draw.circle(const.window, color, (x, y), 2, 2)

    def pollEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
    def main(self): 
        while self.running:
            const.window.fill(self.backgroundColor)
            self.drawCircles()
            const.gameCursor()
            const.createText("Are YOU", self.bigFont, self.textColor, const.window, 100, 50)
            const.createText("The Father?", self.bigFont, self.textColor, const.window, 45, 300)
            const.createText("A Family Game", self.smallFont, self.textColor, const.window, 50, const.height * 0.5 + 75)
            
            mouseX, mouseY = pygame.mouse.get_pos()
            if self.startButton.collidepoint((mouseX, mouseY)):
                if self.clicked:
                    self.running = False
                    break
            elif self.quitButton.collidepoint((mouseX, mouseY)):
                if self.clicked:
                    const.quit()
            else:
                self.clicked = False

            pygame.draw.rect(const.window, self.buttonColor, self.startButton)
            pygame.draw.rect(const.window, self.buttonColor, self.quitButton)
            const.createText("Start Game", self.textboxFont, self.textColor, const.window, const.width * 0.5 - 100, const.height * 0.5 + 150)
            const.createText("Quit Game", self.textboxFont, self.textColor, const.window, const.width * 0.5 - 100, const.height * 0.5 + 220)
            
            self.pollEvent()

            pygame.display.update()
            const.clock.tick(const.fps)