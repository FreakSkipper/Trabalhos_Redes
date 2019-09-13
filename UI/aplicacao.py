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
        print(self.tela.winfo_height())
        print(self.tela.winfo_width())

        # novo objeto de conexão determinado para o URL
        self.novaConexao = ConexaoHttp(self.saveSite.get())
        self.header = ""
        if self.novaConexao.conectar(2.0):  # nova conexão com TimeOut 2 segundos
            if self.novaConexao.getHTML():  # pega Informação do Site
                self.novaConexao.encerrar()  # encerra conexão
                self.header = self.novaConexao.printHeader()  # printa cabeçalho de conexão
                
                self.textTerminal.config(state=tkinter.NORMAL)  # permitir a escrita
                self.textTerminal.insert(tkinter.END, self.header)
                self.textTerminal.config(state=tkinter.DISABLED)    # tornar ready only
                
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
        #------ constantes para controlar o layout dos botões ------
        button_width = 6
        button_padx = "2m"
        button_pady = "1m"
        buttons_frame_padx = "3m"
        buttons_frame_pady = "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        # -------------- fim das constantes ----------------

        # cria uma aplicação tkinter ( provavelmente falta o Frame )
        self.tela = tkinter.Tk()
        self.tela.title(nome)  # titulo
        self.tela.geometry(str(largura)+"x"+str(altura))  # dimensão
        
        # ------- Containers
        self.myContainerMain = tkinter.Frame(self.tela)
        self.myContainerMain.pack()

        self.titleContainer = tkinter.Frame(self.myContainerMain, height=32)
        self.titleContainer.pack(side=tkinter.TOP, ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady, padx=button_padx,
            pady=button_pady, fill=tkinter.X)

        self.topContainer = tkinter.Frame(self.myContainerMain)
        self.topContainer.pack(side=tkinter.TOP, fill=tkinter.BOTH,
            expand=tkinter.YES)

        self.bottomContainer = tkinter.Frame(self.myContainerMain)
        self.bottomContainer.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH,
            expand=tkinter.YES)
        
        # --- frames internos
        self.left_midle_frame = tkinter.Frame(self.topContainer)
        self.left_midle_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH,
            expand=tkinter.YES)

        self.right_midle_frame = tkinter.Frame(self.topContainer)
        self.right_midle_frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH,
            expand=tkinter.YES)
        #########################################
        # Imagem de Redes
        self.imageRedes = tkinter.PhotoImage(file="UI/images/redes.png")
        self.imageRedes.zoom(32)        # multiplies for 64
        self.imageRedes.subsample(157)  # divison for 157 (original size 157px)
        self.labelRedes = tkinter.Label(self.titleContainer, image=self.imageRedes, anchor=tkinter.NW)
        self.labelRedes.pack(side=tkinter.LEFT)
        #self.labelRedes.place(relx = 0.5, rely = 0.2)
        
        # Label UnB
        self.labelUnb = tkinter.Label(self.titleContainer, text="UnB", fg="blue", font=("Arial", 16, "bold"), 
            anchor=tkinter.NW)
        self.labelUnb.pack(side=tkinter.LEFT, padx="20px")


        # Label URL
        self.labelUrl = tkinter.Label(self.left_midle_frame, text="URL", width=6)
        self.labelUrl.pack(side=tkinter.LEFT)

        # Entrada de Link
        self.saveSite = tkinter.StringVar()
        self.entrySite = tkinter.Entry(self.left_midle_frame, width=60, textvariable=self.saveSite)
        self.entrySite.pack(side=tkinter.LEFT, padx='10px', expand=tkinter.YES)

        # Botão para Iniciar Entrada ( leva para o método entrarSite() )
        self.buttonEntrar = tkinter.Button(self.left_midle_frame, text="Conectar", command=self.entrarSite)
        self.buttonEntrar.pack(side=tkinter.LEFT)

        # Label Saída Console
        self.labelOutput = tkinter.Label(self.bottomContainer, text="Console", fg="red", font=("Arial", 12, "bold"), pady=0.4)
        self.labelOutput.grid(column=0, row=0)

        # Label de Resposta Console
        self.labelResposta = tkinter.Label(self.bottomContainer, text="Aguardando conexão..", fg="black",
            font=("Arial", 10), height=5)
        self.labelResposta.grid(column=0, row=1, padx="30px")

        # Botão para abrir Navegador (leva para o método abrirBrowser())
        self.buttonNavegador = tkinter.Button(self.bottomContainer, text="Abrir no Navegador", command=self.abrirBrowser)
        self.buttonNavegador.grid(column=1, row=1)

        # Text saída terminal
        self.sb = tkinter.Scrollbar(self.right_midle_frame)
        self.sb.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self.textTerminal = tkinter.Text(self.right_midle_frame, borderwidth=2, padx=button_padx,
            relief=tkinter.GROOVE, width=60, height=30, state=tkinter.DISABLED,
            yscrollcommand=self.sb.set)
        
        self.textTerminal.pack(fill=tkinter.BOTH, expand=tkinter.YES, padx="5px")
        self.sb.config(command=self.textTerminal.yview)

        # roda loop de apresentação
        self.tela.mainloop()
