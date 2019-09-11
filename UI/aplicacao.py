import tkinter

class Aplicacao:
    def __init__(self, nome, largura, altura):
        self.tela = tkinter.Tk()
        self.tela.title(nome)
        self.tela.geometry(""+str(largura)+"x"+str(altura))

        self.site = tkinter.Label(self.tela, text = "URL")
        self.site.pack()

        self.tela.mainloop()


app = Aplicacao("Zenites", 300, 200)