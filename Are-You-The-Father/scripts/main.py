import game
import title_screen

def main():
    titleScreen = title_screen.mainMenu().main()
    mainGameplay = game.Game().gameLoop()

main()
