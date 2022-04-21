import time
import random

class Cor_certa():

    def __init__(self, lib, telaGame, telaSize, atualiza, funcaoEndGame):

        self.lib = lib
        self.telaGame = telaGame
        self.telaSize = telaSize
        self.atualizaTela = atualiza
        self.avisaQueAcabou = funcaoEndGame
        self.posicaoTexto_numeroCorreto = [200,200]
        self.posicaoTexto_resultadoFinal = [200,400]
        self.acabou = False
        self.cadenciaFinaliza = 50000
        self.contadorCadencia = 0
        self.jaSorteou = False
        self.coresDoJogo = []
        self.corSelecionada = 0
        self.indiceCorCerta = 0
        print("comecou o jogo 2")

    def setCores(self):
        self.indiceCorCerta = random.randint(0,2)
        cores = []
        for i in range(3):
            naoTem = True
            cor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            while naoTem==True:
                for i in self.coresDoJogo:
                    if cor == i:
                        naoTem=False
                
                if naoTem==False:
                    cor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                else:
                    naoTem=True
                    self.coresDoJogo.append(cor)
        self.jaSorteou = True

        

    def render(self):
        posx = 75
        for i in range(3):
            self.lib.draw.rect(self.telaGame,self.coresDoJogo[i],[posx,50,50,50])
            if i == self.corSelecionada:
                self.lib.draw.rect(self.telaGame,[255,255,255],[posx+15,150,20,20])
            posx+=150    
        self.atualizaTela()

    def apagaTela(self):
        self.lib.draw.rect(self.telaGame,[0,0,0],[0,0,1000,1000])


    def acaoTeclado(self,tecla):
        print("alo tecla do jogo")
        if tecla == " ":
            self.setResult()
        
        if tecla == "d":
            self.setCorSelecionada("direita")

        if tecla == "a":
            self.setCorSelecionada("esquerda")

    def setResult(self):
        font = self.lib.font.Font('freesansbold.ttf', 32)

        if self.corSelecionada == self.indiceCorCerta:
             text = font.render("acertou", True, [255,0,255])
             self.telaGame.blit(text,self.posicaoTexto_resultadoFinal)
        else:
            text = font.render("errou", True, [255,0,255])
            self.telaGame.blit(text,self.posicaoTexto_resultadoFinal)

        #self.lib.draw.rect(self.telaGame,[255,255,255],[300,100,20,20])

        self.atualizaTela()
        self.acabou=True
            
    def setCorSelecionada(self,acao):
        if acao == "direita":
            if self.corSelecionada>=2:
                self.corSelecionada=1
            else:
                self.corSelecionada+=1
            
        elif acao == "esquerda":
            if self.corSelecionada<=0:
                self.corSelecionada = 2
            else:
                self.corSelecionada-=1

    def tick(self):
        if self.acabou == False:
            if self.jaSorteou == False:
                self.setCores()

            self.render()
            self.apagaTela()
        else:
            time.sleep(2)
            self.acabou=False
            self.contadorCadencia=0
            self.coresDoJogo.clear()
            self.jaSorteou = False
            self.apagaTela()
            self.avisaQueAcabou()
            self.atualizaTela()
            
    