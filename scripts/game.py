<<<<<<< Updated upstream
from numpy import char
import pygame, consts
=======
import pygame, consts, paths
>>>>>>> Stashed changes

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked, self.showOptions = consts.started, False, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        self.fps = 10
        self.currentScene = 0
        self.points = 0
        self.leftButton = pygame.Rect(0, self.height - 100, self.width * 0.5, self.height - 200)
        self.rightButton = pygame.Rect(self.width * 0.5, self.height - 100, self.width, self.height - 200)
        self.textBackground = pygame.Rect(0, self.height - 100, self.width, self.height - 200)
<<<<<<< Updated upstream
    
=======
        self.on = True

        self.mauryStage = pygame.image.load(paths.images + "MauryStage.png").convert()

>>>>>>> Stashed changes
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
            self.on = True
            self.clicked = False
            self.currentScene += 1
            if correctChoice == "left":
                self.points += 2
            else:
                self.points -= 1
        elif self.rightButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            self.on = True
            self.currentScene += 1
            if correctChoice == "right":
                self.points += 2
            else:
                self.points -= 1
        else:
            self.clicked = False
            self.on = False

    def intro(self, posX, posY, character):
        self.window.fill(self.white)
        character.get_rect().center = (posX, posY)
        self.window.blit(character, character.get_rect())
        pygame.display.flip()
        self.window.blit(character, character.get_rect())
        pygame.draw.rect(self.window, (220, 220, 220), self.textBackground)

        if character == self.ZAYM:
            self.dialogue("I am not the father!", 200, 750, self.purple, 125)
            self.dialogue("She just wants my   ", 420, 750, self.purple, 125)
            self.dialogue("money!  ", 600, 750, self.purple, 125)
        else:
            self.dialogue("I know he the father!", 0, 750, self.purple, 125)
            self.dialogue("He just does not want", 220, 750, self.purple, 125)
            self.dialogue("to pay up!  ", 440, 750, self.purple, 100)

        pygame.time.delay(500)
    
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
<<<<<<< Updated upstream
            
    def gameLoop(self):
        #self.initScenes(self.frames, 3, "Baby")
        self.tutorial()
        self.intro(50, 800, self.moniqueIntro)
        self.intro(50, 800, self.ZAYM)
        self.loadingScreen(self.currentScene)
        while self.playing:
            self.window.fill(self.white)
            self.options()
            self.pointSystem()
            self.gameFlow()
            self.clock.tick(self.fps) 
=======

    def talking(self, text, posX, posY, color, offset, pos1X, pos1Y, list):
        j = 0
        frame = 0
        caption = ""
        if self.on:
            self.window.fill(self.white)
            speed = int(len(text) / self.fps * 100) - offset
            for i in range(0, len(text)):
                self.mauryStage.get_rect().center = (self.width, self.height)
                self.window.blit(self.mauryStage, self.mauryStage.get_rect())
                pygame.display.flip()
                pygame.draw.rect(self.window, (220, 220, 220), self.textBackground)
                caption += text[i]
                self.createText(caption, self.dialogueFont, color, self.window, posX, posY) 
                frameRect = list[frame].get_rect()
                frameRect.center = (pos1X, pos1Y)
                self.window.blit(list[frame], frameRect)
                self.gameFlow()
                if i % 2 != 0:
                    frame += 1
                else:
                    frame = 0
                pygame.time.delay(speed)
        pygame.time.delay(500)

    def sequence(self):
        self.mauryStage.get_rect().center = (self.width, self.height)
        self.window.blit(self.mauryStage, self.mauryStage.get_rect())
        frameRect = self.mauryV1[0].get_rect()
        frameRect.center = (200, 300)
        self.window.blit(self.mauryV1[0], frameRect)
        pygame.display.flip()
        self.clock.tick(30)
        self.options()
        self.pointSystem()

    def background(self):
        self.talking("Welcome to are you the father!", 0, 750, self.purple, 150, 200, 300, self.mauryV1)
        self.talking("Today we will be discussing the relationship", 0, 750, self.purple, 250, 200, 300, self.mauryV1)
        self.talking("of Tyrone, Monique and their offspring Kevin.", 0, 750, self.purple, 250, 200, 300, self.mauryV1)

    def scene1(self):
        self.talking("What were you doing on the night you met?", 0, 750, self.purple, 200, 200, 300, self.mauryV1)
        self.talking("I was at this party passing out my mixtape, when this girl Monique started talking about how my music is fire.", 200, 750, self.purple, 125, 500, 1100, self.tyroneV1)
        self.talking("We had a quick conversation, and started messing with each other.", 200, 750, self.purple, 125, 500, 650, self.tyroneV1)
        self.talking("I was at this party; doing my daily spiritual routine. As I was taking my prescribed amount of narcotics, Monique came up to me to ask what’s up.", 200, 750, self.purple, 125, 500, 1450, self.tyroneV2)
        self.talking("We had a quick conversation, and formed a mutual interest.", 200, 750, self.purple, 125, 500, 580, self.tyroneV2)

    def scene2(self):
        self.talking("How do you feel about Kevin?", 0, 750, self.purple, 150, 200, 300, self.mauryV1)
        self.talking("Pull up to the block right now he ain’t want no smoke.", 200, 750, self.purple, 125, 500, 540, self.tyroneV1)
        self.talking("I let my money talk", 200, 750, self.purple, 125, 500, 190, self.tyroneV1)
        self.talking("I love that child, and even if he’s not my son or father, I’ll support him.", 200, 750, self.purple, 125, 500, 750, self.tyroneV2)
        self.talking("He’s not mine, I gave my soul to Jah, not to the kid or that darn hippo!", 200, 750, self.purple, 125, 500, 720, self.tyroneV2)
    
    def scene3(self):
        self.talking("How did your relationship with Monique worsen?", 0, 750, self.purple, 200, 200, 300, self.mauryV1)
        self.talking("I released some new music, and Monique thought it was trash.", 200, 750, self.purple, 125, 500, 600, self.tyroneV1)
        self.talking("She was listening to another rapper who dissed me.", 200, 750, self.purple, 125, 500, 500, self.tyroneV1)
        self.talking("Whenever we would go out on dates, the spiritual vibes of the activity were questionable.", 200, 750, self.purple, 125, 500, 890, self.tyroneV2)
        self.talking("She got mad that I was a chainsmoker.", 200, 750, self.purple, 125, 500, 370, self.tyroneV2)

    def scene4(self):
        self.talking("So, why did you seperate?", 0, 750, self.purple, 150, 200, 300, self.mauryV1)
        self.talking("I heard rumors that Monique was cheating on me with my twin brother.", 200, 750, self.purple, 125, 500, 680, self.tyroneV1)
        self.talking("She didn’t like how I was kickin it with my other concubines.", 200, 750, self.purple, 125, 500, 610, self.tyroneV1)
        self.talking("I heard rumors that Monique was cheating on me with my twin brother.", 200, 750, self.purple, 125, 500, 680, self.tyroneV2)
        self.talking("We had a mutual determination that our futures were not aligned in the eyes of Jah. And that’s on Jah.", 200, 750, self.purple, 125, 500, 1020, self.tyroneV2)

    def scene5(self):
        self.talking("How do you feel about Monique now?", 0, 750, self.purple, 150, 200, 300, self.mauryV1)
        self.talking("Four out of ten.", 200, 750, self.purple, 125, 500, 160, self.tyroneV1)
        self.talking("She went from Nicki Minaj to Lizzo.", 200, 750, self.purple, 125, 500, 350, self.tyroneV1)
        self.talking("Monique is another woman who needs to be enlightened.", 200, 750, self.purple, 125, 500, 530, self.tyroneV2)
        self.talking("Monique is a liar and a sinner in the eyes of Jah. Her lust knows no bounds.", 200, 750, self.purple, 125, 500, 760, self.tyroneV2)

    def outro(self):
        pass
    
    def gameLoop(self):
        self.initScenes(paths.tyroneV1,"Tyrone", "V1", "serious ", self.tyroneV1)
        self.initScenes(paths.tyroneV2,"Tyrone", "V2", "angry ", self.tyroneV2)
        self.initScenes(paths.maury,"Maury", "V1", "neutral ", self.mauryV1)
        self.initScenes(paths.monique,"Monique", "V1", "shocked ", self.moniqueV1)
        #self.tutorial()
        #self.intro(50, 800, self.moniqueIntro)
        #self.intro(50, 800, self.ZAYM)
        while self.playing:
            self.window.fill(self.white)
            if self.currentScene == 0:
                self.background()
                self.sequence()
                self.currentScene += 1
            elif self.currentScene == 1 and self.clicked:
                self.loadingScreen(self.currentScene)
                self.scene1()
                self.sequence()
            elif self.currentScene == 2 and self.clicked:
                self.loadingScreen(self.currentScene)
                self.scene2()
                self.sequence()
            elif self.currentScene == 3 and self.clicked:
                self.loadingScreen(self.currentScene)
                self.scene3()
                self.sequence()
            elif self.currentScene == 4 and self.clicked:
                self.loadingScreen(self.currentScene)
                self.scene4()
                self.sequence()
            elif self.currentScene == 5 and self.clicked:
                self.loadingScreen(self.currentScene)
                self.scene5()
                self.sequence()
            elif self.currentScene == 6:
                self.window.fill(self.black)
                pygame.time.delay(500)
                self.outro()
            self.gameFlow()
            self.clock.tick(self.fps)
>>>>>>> Stashed changes
