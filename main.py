import pygame, sys
from startMenu import startMenuClass as stMenu
from dez_numeros import dezNumeros
from corCerta import Cor_certa
import random

pygame.init()


class mainController:
    def __init__(self):
        self.screenSize = [500,500]
        self.screen = pygame.display.set_mode(self.screenSize)

        self.startMenu_screen = stMenu(pygame, self.screen, self.atualizaTela, self.screenSize) 
        self.jogando = False
        self.tela = "start_menu"
        self.minigames = [dezNumeros(pygame,self.screen,self.screenSize,self.atualizaTela,self.endMinigame),Cor_certa(pygame,self.screen,self.screenSize,self.atualizaTela,self.endMinigame)]
        self.minigameDaVez = 0

        


    def atualizaTela(self):
        pygame.display.update()

    def endMinigame(self):
        self.startMenu_screen.apagaTela()
        self.jogando=False
        #self.startMenu_screen.render()
        mainGameControler.jogando = True
        mainGameControler.minigameDaVez = random.randint(0,1)


mainGameControler = mainController()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mainGameControler.startMenu_screen.acaoTeclado(chr(event.key))
            if event.key == pygame.K_s:
                mainGameControler.startMenu_screen.acaoTeclado(chr(event.key))
            
            if mainGameControler.jogando:
                try:
                    mainGameControler.minigames[mainGameControler.minigameDaVez].acaoTeclado(chr(event.key))

                except:
                    print("erro")
            if event.key == pygame.K_1:
                if mainGameControler.startMenu_screen.seleciona() == "JOGAR":
                    mainGameControler.startMenu_screen.apagaTela()
                    mainGameControler.jogando = True
                    #mainGameControler.minigameDaVez = random.randint(0,1)
                    mainGameControler.minigameDaVez = 1                    
           
                    
    if mainGameControler.jogando:

        mainGameControler.minigames[mainGameControler.minigameDaVez].tick()

  
