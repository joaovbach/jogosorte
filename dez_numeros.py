import random
import time


class dezNumeros:
    def __init__(self, lib, telaGame, telaSize, atualiza, funcaoEndGame):
        self.lib = lib
        self.jogando = False
        self.telaGame = telaGame
        self.telaSize = telaSize
        self.atualiza = atualiza
        self.tamanhoBotaoNumeros = [50,50]

        self.numeroSelecionado = ""
        self.numeroCerto = self.setNumeroCorreto()
        self.posicaoTexto_numeroCorreto = [200,200]
        self.posicaoTexto_resultadoFinal = [200,400]
        self.acabou = False
        self.cadenciaFinaliza = 50000
        self.contadorCadencia = 0
        self.avisarQueAcabou = funcaoEndGame
        

    def render(self):
        posix = 50
        posiy = 0
        for i in range(0,10):
            self.lib.draw.rect(self.telaGame,[255,255,255],[posix,posiy,self.tamanhoBotaoNumeros[0],self.tamanhoBotaoNumeros[1]])
            font = self.lib.font.Font('freesansbold.ttf', 32)
            text = font.render(str(i), True, [255,0,255])
            self.telaGame.blit(text,[posix,posiy])
            posix+=75
            if posix >= 500:
                posix = 50
                posiy += 75

        self.lib.draw.rect(self.telaGame,[255,255,0],[self.posicaoTexto_numeroCorreto[0],self.posicaoTexto_numeroCorreto[1],50,50])
        font = self.lib.font.Font('freesansbold.ttf', 32)
        text = font.render(self.numeroSelecionado, True, [255,0,255])
        self.telaGame.blit(text,self.posicaoTexto_numeroCorreto)
        

        self.atualiza()
    
    def apagaTela(self):
        if self.acabou == False:
            self.lib.draw.rect(self.telaGame,[0,0,0],[0,0,1000,1000])

    def acaoTeclado(self,tecla):
        if tecla == " ":
            self.setResult()
            
        self.numeroSelecionado = tecla

    def tick(self):
        if self.acabou:
            time.sleep(2)
            self.acabou=False
            self.contadorCadencia=0
            self.apagaTela()
            self.avisarQueAcabou()
            self.atualiza()
        else:
            self.render()
            self.apagaTela()

    def setResult(self):
        self.acabou=True
        if int(self.numeroSelecionado) == self.numeroCerto:
            print("acertou")
            self.lib.draw.rect(self.telaGame, [255,255,255],[self.posicaoTexto_resultadoFinal[0],self.posicaoTexto_resultadoFinal[1],100,50])
            font = self.lib.font.Font('freesansbold.ttf', 32)
            text = font.render("acertou", True, [255,0,255])
            self.telaGame.blit(text,self.posicaoTexto_resultadoFinal)

        else:
            print("errou")
            self.lib.draw.rect(self.telaGame, [255,255,255],[self.posicaoTexto_resultadoFinal[0],self.posicaoTexto_resultadoFinal[1],100,50])
            font = self.lib.font.Font('freesansbold.ttf', 32)
            text = font.render("errou", True, [255,0,255])
            self.telaGame.blit(text,self.posicaoTexto_resultadoFinal)

        self.atualiza()
    def setNumeroCorreto(self):
        return random.randint(0,10)
