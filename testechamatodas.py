class testechama:
    def __init__(self,lib,screen,chama):
        self.lib = lib
        self.screen = screen
        self.chama = chama
        
    

    def acaoTeclado(self, acao):
        print("to aqui do teclado")
        if acao == "d":
            self.chama("imprimeDados")

    def tick(self):
        pass
