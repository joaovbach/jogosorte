from tracemalloc import start
import pygame, sys
from startMenu import startMenuClass as stMenu
from dez_numeros import dezNumeros
pygame.init()


def atualizaTela():
    pygame.display.update()


screenSize = [500,500]
screen = pygame.display.set_mode(screenSize)

startMenu_screen = stMenu(pygame, screen, atualizaTela, screenSize) 
jogando = False
tela = "start_menu"
minigames = [dezNumeros(pygame,screen,screenSize,atualizaTela)]
minigameDaVez = 0





while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                startMenu_screen.acaoTeclado(chr(event.key))

            if jogando:
                try:
                    minigames[minigameDaVez].acaoTeclado(chr(event.key))

                except:
                    print("erro")
            if event.key == pygame.K_1:
                if startMenu_screen.seleciona() == "JOGAR":
                    startMenu_screen.apagaTela()
                    jogando = True
                    minigameDaVez = 0
                    
    if jogando:
        minigames[minigameDaVez].tick()

  
