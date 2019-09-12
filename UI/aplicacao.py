import tkinter
from Net.conexao import ConexaoHttp
import platform                   # system calls
import webbrowser           # usado para abrir no navegador
from pathlib import Path    # path to workspace

if platform.system() is "Windows":
    OS = "Windows"
    CLEAR = 'cls'
else:
    OS = "Linux"
    CLEAR = 'clear'

class Aplicacao:

    def entrarSite(self):
        print("> " + self.saveSite.get())
        # novo objeto de conexão determinado para o URL
        self.novaConexao = ConexaoHttp(self.saveSite.get())
        self.header = ""
        if self.novaConexao.conectar(2.0):  # nova conexão com TimeOut 2 segundos
            if self.novaConexao.getHTML():  # pega Informação do Site
                self.novaConexao.encerrar()  # encerra conexão
                self.header = self.novaConexao.printHeader()  # printa cabeçalho de conexão
                self.labelTerminal.configure(text=self.header)
                
                self.novaConexao.criarHTML()  # cria o arquivo HTML

                self.labelResposta.configure(text="Conectado com sucesso!")

            else:
                self.labelResposta.configure(text="Tempo de conexão excedido!")
        else:
            self.labelResposta.configure(text="Não foi possível conectar nesse endereço.")

    def abrirBrowser(self):
        work_path = Path(__file__).parent.absolute()
        # print(work_path)
        # print(platform.system())
        # print(OS)

        aux = len(str(work_path))
        aux_str = str(work_path)
        caracter_stop = 0
        for i in range(aux-1, -1, -1):
            if OS is "Windows":
                if aux_str[i] == "\\":
                    caracter_stop = i
                    break
            else:
                if aux_str[i] == "/":
                    caracter_stop = i
                    break
        # print(str(caracter_stop) + '\n' + aux_str[0:caracter_stop] + "\index.html")
        if OS == "windows":
            webbrowser.open(aux_str[0:caracter_stop] + "\index.html")
        else:
            webbrowser.open(aux_str[0:caracter_stop] + "/index.html")

    def __init__(self, nome, largura, altura):
        # cria uma aplicação tkinter ( provavelmente falta o Frame )
        self.tela = tkinter.Tk()
        self.tela.title(nome)  # titulo
        self.tela.geometry(str(largura)+"x"+str(altura))  # dimensão

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
        self.buttonEntrar = tkinter.Button(self.tela, text="Conectar", command=self.entrarSite)
        self.buttonEntrar.grid(column=1, row=3, padx=10)

        # Label Saída HTML
        self.labelOutput = tkinter.Label(self.tela, text="Console", fg="red", font=("Arial", 12, "bold"))
        self.labelOutput.grid(column=0, row=4, pady=(60, 0))

        # Label de Resposta
        self.labelResposta = tkinter.Label(self.tela, text="Aguardando conexão..", fg="black", font=("Arial", 10), height=5)
        self.labelResposta.grid(column=0, row=5, pady=(0, 0))

        # Botão para abrir Navegador (leva para o método abrirBrowser())
        self.buttonNavegador = tkinter.Button(self.tela, text="Abrir no Navegador", command=self.abrirBrowser)
        self.buttonNavegador.grid(column=1, row=6, padx=10, sticky=tkinter.E)

        # Label saída terminal
        self.labelTerminal = tkinter.Label(self.tela, text="Label terminal", borderwidth=2, relief=tkinter.GROOVE, width=60, height=30)
        self.labelTerminal.grid(column=2, row=2)
        # roda loop de apresentação
        self.tela.mainloop()
