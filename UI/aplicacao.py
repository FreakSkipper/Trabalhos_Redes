import tkinter
from Net.conexao import ConexaoHttp


class Aplicacao:

    def entrarSite(self):
        print("> " + self.saveSite.get())
        # novo objeto de conexão determinado para o URL
        self.novaConexao = ConexaoHttp(self.saveSite.get())

        if self.novaConexao.conectar(2.0):  # nova conexão com TimeOut 2 segundos
            self.novaConexao.getHTML()  # pega Informação do Site
            self.novaConexao.encerrar()  # encerra conexão
            self.novaConexao.printHeader()  # printa cabeçalho de conexão
            self.novaConexao.criarHTML()  # cria o arquivo HTML
        else:
            print("Não foi possível conectar-se nesse endereço.")
            self.labelResposta.configure(text="Não foi possível conectar nesse endereço.")

    def __init__(self, nome, largura, altura):
        # cria uma aplicação tkinter ( provavelmente falta o Frame )
        self.tela = tkinter.Tk()
        self.tela.title(nome)  # titulo
        self.tela.geometry(""+str(largura)+"x"+str(altura))  # dimensão

        # Label UnB
        self.labelUnb = tkinter.Label(self.tela, text="UnB", fg="blue", font=("Arial", 20, "bold"))
        self.labelUnb.grid(column=0, row=0, pady=(60, 0))

        # Imagem de Redes
        self.imageRedes = tkinter.PhotoImage(file="UI/images/redes.png")
        self.labelRedes = tkinter.Label(self.tela, image=self.imageRedes)
        self.labelRedes.grid(column=0, row=1, pady=(10, 0))
        #self.labelRedes.place(relx = 0.5, rely = 0.2)

        # Label URL
        self.labelUrl = tkinter.Label(self.tela, text="URL")
        self.labelUrl.grid(column=0, row=2, pady=(20, 0))

        # Entrada de Link
        self.saveSite = tkinter.StringVar()
        self.entrySite = tkinter.Entry(self.tela, width=100, textvariable=self.saveSite)
        self.entrySite.grid(column=0, row=3, padx=10)

        # Botão para Iniciar Entrada ( leva para o método entrarSite() )
        self.buttonEntrar = tkinter.Button(self.tela, text="Entrar", command=self.entrarSite)
        self.buttonEntrar.grid(column=1, row=3, padx=10)

        # Label Saída HTML
        self.labelOutput = tkinter.Label(self.tela, text="Console", fg="red", font=("Arial", 12, "bold"))
        self.labelOutput.grid(column=0, row=4, pady=(60, 0))

        # Label de Resposta
        self.labelResposta = tkinter.Label(self.tela, text="Aguardando conexão..", fg="black", font=("Arial", 10), height=5)
        self.labelResposta.grid(column=0, row=5, pady=(0, 0))

        # Botão para abrir Navegador
        self.buttonNavegador = tkinter.Button(self.tela, text="Abrir no Navegador")
        self.buttonNavegador.grid(column=1, row=6, padx=10, sticky=tkinter.E)

        # roda loop de apresentação
        self.tela.mainloop()
