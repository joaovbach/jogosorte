
from turtle import screensize


class startMenuClass:
 
    def render(self):
        
        for i in range(0,len(self.palavrasBotoes)):
            if self.selecionado[i] == True:
                self.lib.draw.rect(self.telaGame, [0,255,255],[self.posicaoBotoes[i][0],self.posicaoBotoes[i][1],self.tamanhoBotoes[i][0],self.tamanhoBotoes[i][1]])
            else:
                self.lib.draw.rect(self.telaGame, [255,255,255],[self.posicaoBotoes[i][0],self.posicaoBotoes[i][1],self.tamanhoBotoes[i][0],self.tamanhoBotoes[i][1]])    
            font = self.lib.font.Font('freesansbold.ttf', 32)
            text = font.render(self.palavrasBotoes[i], True, [255,0,255])
            self.telaGame.blit(text,self.posicaoBotoes[i])

        self.atualiza()

    def navega(self,direcao):
        print(direcao)
        if direcao == "up":
            print("apertei up")
            posi = 0
            for i in self.selecionado:
                if self.selecionado[i] == True:
                    posi=i
                    self.selecionado[i] = False

            if posi == len(self.selecionado)-1:
                self.selecionado[0]=True
            else:
                self.selecionado[posi+1]=True
        else:
            print("apertei down")
            posi=0
            for i in self.selecionado:
                if self.selecionado[i] == True:
                    posi = i
                    self.selecionado[i] = False

            if posi == 0:
                self.selecionado[int(len(self.selecionado)-1)] = True
            else:
                self.selecionado[posi-1]=True

    
        self.apagaTela()
        self.render()
        
        

    def apagaTela(self):
        self.lib.draw.rect(self.telaGame,[0,0,0],[0,0,1000,1000])
        self.atualiza()
        

    def seleciona(self):
        for i in range(0,len(self.selecionado)):
            if self.selecionado[i] == True:
                return "JOGAR"

            
    def acaoTeclado(self,tecla):
        print("entrei aqui pra ver a tecla")
        print(tecla)
        if tecla == "w":
            self.navega("up")

        if tecla == "s":
            self.navega("down")
        
    
    def __init__(self, lib, tela, atualiza,screenSize):
        self.telaGame = tela
        self.lib = lib
        self.screenSize = screenSize
        self.atualiza = atualiza

        self.palavrasBotoes = ["JOGAR", "SAIR"]
        self.posicaoBotoes = [[(screenSize[0]/2)-100,(screenSize[1]/2)-100] , [(screenSize[1]/2)-75,(screenSize[1]/2)+50]]
        self.tamanhoBotoes = [[200,screenSize[0]/10],[150, screenSize[1]/10]]
        self.selecionado = [True, False]
        
        self.render()