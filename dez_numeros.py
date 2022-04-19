import random

class dezNumeros:
    def __init__(self, lib, telaGame, telaSize, atualiza):
        self.lib = lib
        self.jogando = False
        self.telaGame = telaGame
        self.telaSize = telaSize
        self.atualiza = atualiza
        self.tamanhoBotaoNumeros = [50,50]

        self.numeroSelecionado = ""
        self.numeroCerto = self.setNumeroCorreto()
        

    def render(self):
        posix = 0
        posiy = 0
        for i in range(0,10):
            self.lib.draw.rect(self.telaGame,[255,255,255],[posix,posiy,self.tamanhoBotaoNumeros[0],self.tamanhoBotaoNumeros[1]])
            font = self.lib.font.Font('freesansbold.ttf', 32)
            text = font.render(str(i), True, [255,0,255])
            self.telaGame.blit(text,[posix,posiy])
            posiy+=100

        self.lib.draw.rect(self.telaGame,[255,255,0],[100,100,50,50])
        font = self.lib.font.Font('freesansbold.ttf', 32)
        text = font.render(self.numeroSelecionado, True, [255,0,255])
        self.telaGame.blit(text,[100,100])
        

        self.atualiza()
    
    def apagaTela(self):
        self.lib.draw.rect(self.telaGame,[0,0,0],[0,0,1000,1000])

    def acaoTeclado(self,tecla):
        if tecla == " ":
            self.setResult()
            
        self.numeroSelecionado = tecla

    def tick(self):
        self.render()
        self.apagaTela()

    def setResult(self):
        if int(self.numeroSelecionado) == self.numeroCerto:
            print("acertou")
        else:
            print("errou")

    def setNumeroCorreto(self):
        return random.randint(0,10)