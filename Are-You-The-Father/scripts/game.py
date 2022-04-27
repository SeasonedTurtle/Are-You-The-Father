import pygame, consts, paths

class Game(consts.Constants):
    def __init__(self):
        consts.Constants.__init__(self)
        self.playing, self.clicked = consts.started, False
        self.dialogueFont = pygame.font.Font(self.font, 25)
        pygame.mouse.set_visible(True)
        self.fps = 10
        self.currentScene = 0
        self.points = 0
        self.leftButton = pygame.Rect(0, self.height - 220, self.width, self.height - 400)
        self.rightButton = pygame.Rect(0, self.height - 100, self.width, self.height - 200)
        self.textBackground = pygame.Rect(0, self.height - 100, self.width, self.height - 200)
        self.on, self.right, self.left = True, False, False
        self.mauryStage = pygame.image.load(paths.images + "MauryStage.png").convert()
        self.daBabyBody = pygame.image.load(paths.images + "DaBaby-with-DaBody.png").convert()
        self.ZAYM = pygame.image.load(paths.images + "Tyrone ZAMNV1.jpg").convert()
        self.moniqueIntro = pygame.image.load(paths.images + "Sheniqua Angry.jpg").convert()
        self.option1 = "I was at this party passing out my mixtape, when Monique started talking about how my music is fire."
        self.option2 = "I was at a party, doing my spiritual routine, taking my prescribed narcotics and she approached me."
        self.playerCharacter = True

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

    def options(self, Option1, Option2):
        pygame.draw.rect(self.window, self.pink, self.leftButton)
        self.createText(Option1, self.choiceFont, self.black, self.window, 0, 650)
        pygame.draw.rect(self.window, self.purple, self.rightButton)
        self.createText(Option2, self.choiceFont, self.black, self.window, 0, 750)

    def mouseInput(self, correctChoice):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.leftButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            self.right = True
            if self.currentScene == 1:
                self.playerCharacter = False
            if correctChoice == "left":
                self.points += 2
            else:
                self.points -= 1
        elif self.rightButton.collidepoint((mouseX, mouseY)) and self.clicked:
            self.clicked = False
            self.left = True
            if self.currentScene == 1:
                self.playerCharacter = True
            if correctChoice == "right":
                self.points += 2
            else:
                self.points -= 1
        else:
            self.clicked = False
            self.left = False
            self.right = False

    def getList(self):
        if self.playerCharacter:
            newList = self.tyroneV2
        else:
            newList = self.tyroneV1
        return newList

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
            self.dialogue("I know he's the father!", 0, 750, self.purple, 125)
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

    def gameResult(self):
        if self.points > 8 or self.points < 0:
            result = True
        else:
            result = False
        return result

    def talking(self, text, posX, posY, color, offset, pos1X, pos1Y, list, font):
        j = 0
        frame = 0
        offset *= 1.25
        caption = ""
        if self.on:
            self.window.fill(self.white)
            speed = int(len(text) / self.fps * 100) - int(offset)
            for i in range(0, len(text)):
                self.mauryStage.get_rect().center = (self.width, self.height)
                self.window.blit(self.mauryStage, self.mauryStage.get_rect())
                pygame.display.flip()
                pygame.draw.rect(self.window, (220, 220, 220), self.textBackground)
                caption += text[i]
                self.createText(caption, font, color, self.window, posX, posY) 
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

    def characterCheck(self, option1, option2, option3, option4):
        self.option1 = ""
        self.option2 = ""
        if not self.playerCharacter:
            self.option1 = option1
            self.option2 = option2
        else:
            self.option1 = option3
            self.option2 = option4

    def sequence(self, option1, option2):
        self.currentScene += 1
        self.window.fill(self.white)
        self.mauryStage.get_rect().center = (self.width, self.height)
        self.window.blit(self.mauryStage, self.mauryStage.get_rect())
        frameRect = self.mauryV1[0].get_rect()
        frameRect.center = (200, 300)
        self.window.blit(self.mauryV1[0], frameRect)
        self.clock.tick(30)
        self.options(option1, option2)
        self.pointSystem()

    def background(self):
        self.talking("Welcome to are you the father!", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        #self.talking("Today we will be discussing the relationship", 0, 750, self.purple, 250, 200, 300, self.mauryV1, self.dialogueFont)
        #self.talking("of Tyrone, Monique and their offspring Kevin.", 0, 750, self.purple, 250, 200, 300, self.mauryV1, self.dialogueFont)
        #self.talking("He's definitely the father!", 0, 750, self.purple, 150, 200, 300, self.moniqueV1, self.dialogueFont)
        #self.talking("Just look at them! They look identical", 0, 750, self.purple, 220, 200, 300, self.moniqueV1, self.dialogueFont)
        #self.talking("Well. Let's take a look everybody!", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        characters = [self.ZAYM, self.daBabyBody]
        for character in characters:
            self.window.fill(self.white)
            character.get_rect().center = (300, 400)
            self.window.blit(character, character.get_rect())
            pygame.display.flip()
            pygame.time.delay(2000)
        self.talking("They got the same nose, eyes, and everything", 0, 750, self.purple, 300, 200, 300, self.moniqueV1, self.dialogueFont)
        self.talking("Okay, let's give Tyrone a chance to speak.", 0, 750, self.purple, 300, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)
        self.currentScene += 1
        
    def scene1(self):
        self.talking("What were you doing on the night you met?", 0, 750, self.purple, 300, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)

    def scene2(self):
        if self.currentScene == 2:
            self.talking("How do you feel about Kevin?", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)
    
    def scene3(self):
        if self.currentScene == 3:
            self.talking("How did your relationship with Monique worsen?", 0, 750, self.purple, 250, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)

    def scene4(self):
        if self.currentScene == 4:
            self.talking("So, why did you seperate?", 0, 750, self.purple, 100, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)

    def scene5(self):
        if self.currentScene == 5:
            self.talking("How do you feel about Monique now?", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(250)

    def outro(self, result, characters):
        self.talking("In the case of five month old Kevin...", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        pygame.time.delay(500)
        for character in characters:
            self.window.fill(self.white)
            character.get_rect().center = (300, 400)
            self.window.blit(character, character.get_rect())
            pygame.display.flip()
            pygame.time.delay(500)
        if result:
            self.talking("YOU ARE THE FATHER!", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
        else:
            self.talking("YOU ARE NOT THE FATHER!", 0, 750, self.purple, 150, 200, 300, self.mauryV1, self.dialogueFont)
    
    def gameLoop(self):
        self.initScenes(paths.tyroneV1, "Tyrone", "V1", "smug ", self.tyroneV1)
        self.initScenes(paths.tyroneV2, "Tyrone", "V2", "happy ", self.tyroneV2)
        self.initScenes(paths.maury, "Maury", "V1", "neutral ", self.mauryV1)
        self.initScenes(paths.monique, "Monique", "V1", "angry ", self.moniqueV1)
        #self.tutorial()
        #self.intro(50, 800, self.moniqueIntro)
        #self.intro(50, 800, self.ZAYM)
        while self.playing:
            if self.currentScene == 0:
                self.background()

            elif self.currentScene == 1:
                self.loadingScreen(self.currentScene)
                self.scene1()
                self.sequence(self.option1, self.option2)

            elif self.currentScene == 2 and self.clicked:
                print(self.playerCharacter)
                if self.right:
                    self.talking(self.option2, 0, 750, self.purple, 750, 200, 300, self.getList(), self.choiceFont)
                else:
                    self.talking(self.option1, 0, 750, self.purple, 750, 200, 300, self.getList(), self.choiceFont)
                pygame.time.delay(300)
                self.loadingScreen(self.currentScene)
                self.scene2()
                self.characterCheck("Pull up to the block right now he ain’t want no smoke.",
                                    "I let my money talk",
                                    "I love that child, and even if he’s not my son or father, I’ll support him.",
                                    "He’s not mine, I gave my soul to Jah, not to the kid or that darn hippo!")
                self.sequence(self.option1, self.option2)

            elif self.currentScene == 3 and self.clicked:
                if self.right:
                    self.talking(self.option1, 0, 750, self.purple, 550, 200, 300, self.getList(), self.choiceFont)
                if self.left:
                    self.talking(self.option2, 0, 750, self.purple, 700, 200, 300, self.getList(), self.choiceFont)
                pygame.time.delay(300)
                self.loadingScreen(self.currentScene)
                self.scene3()
                self.characterCheck("She was listening to another rapper who dissed me.",
                                    "I released some new music, and Monique thought it was trash.",
                                    "Whenever we would go out on dates, the spiritual vibes of the activity were questionable.",
                                    "She got mad that I was a chainsmoker.")
                self.sequence(self.option1, self.option2)

            elif self.currentScene == 4 and self.clicked:
                if self.right:
                    self.talking(self.option1, 0, 750, self.purple, 550, 200, 300, self.getList(), self.choiceFont)
                if self.left:
                    self.talking(self.option2, 0, 750, self.purple, 650, 200, 300, self.getList(), self.choiceFont)
                pygame.time.delay(400)
                self.loadingScreen(self.currentScene)
                self.scene4()
                self.characterCheck("I heard rumors that Monique was cheating on me with my twin brother.",
                                    "She didn’t like how I was kickin it with my other concubines.",
                                    "I heard rumors that Monique was cheating on me with my twin brother.",
                                    "We had a mutual determination that our futures were not aligned in the eyes of Jah. And that’s on Jah.")
                self.sequence(self.option1, self.option2)

            elif self.currentScene == 5 and self.clicked:
                if self.right:
                    self.talking(self.option1, 0, 750, self.purple, 650, 200, 300, self.getList(), self.choiceFont)
                if self.left:
                    self.talking(self.option2, 0, 750, self.purple, 650, 200, 300, self.getList(), self.choiceFont)
                pygame.time.delay(300)
                self.loadingScreen(self.currentScene)
                self.scene5()
                self.characterCheck("Four out of ten.",
                                    "She went from Nicki Minaj to Lizzo.",
                                    "Monique is another woman who needs to be enlightened.",
                                    "Monique is a liar and a sinner in the eyes of Jah. Her lust knows no bounds.")
                self.sequence(self.option1, self.option2)

            elif self.currentScene == 6 and self.clicked:
                if self.right:
                    self.talking(self.option1, 0, 750, self.purple, 550, 200, 300, self.getList(), self.choiceFont)
                if self.left:
                    self.talking(self.option2, 0, 750, self.purple, 650, 200, 300, self.getList(), self.choiceFont)
                pygame.time.delay(500)
                characters = [self.moniqueIntro, self.ZAYM, self.daBabyBody]
                self.window.fill(self.black)
                pygame.time.delay(500)
                self.outro(self.gameResult(), characters)
                pygame.time.delay(15000)
                self.quit()
            self.gameFlow()
            self.clock.tick(self.fps)