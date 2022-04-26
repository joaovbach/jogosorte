import random

class testechama:
    def __init__(self,lib,screen,chama):
        self.lib = lib
        self.screen = screen
        self.chama = chama
        
    

    def acaoTeclado(self, acao):
        print("to aqui do teclado")
        if acao == "d":
            self.lib.draw.rect(self.screen,[255,255,255],[random.randint(1,400),random,randint(1,400),50,50])
            self.chama("teste1")
        if acao == "a":
            self.chama("teste2")

    def tick(self):
        pass
