import pygame, pygame_menu

pygame.init()
pygame.display.set_caption("Settings")
WINDOW = pygame.display.set_mode((440, 280))

def setResolution():
    pass

def setFPS():
    pass

def saveSettings():
    print("hello")
    pass

menu = pygame_menu.Menu("Settings", 440, 280)
menu.add.selector("Screen Res: ", [("440x280",1), ("880x560",2), ("1760x1120",3)])
menu.add.selector("FPS: ", [(" 30 ", 1), (" 60 ", 2), ("120", 3)])
menu.add.button("Save", saveSettings())

menu.mainloop(WINDOW)