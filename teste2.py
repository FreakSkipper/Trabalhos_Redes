import tkinter

def command():
    pass

def main():
    w = tkinter.Tk()
    menu = tkinter.Menu(w, background="black", foreground="red")
    file_menu = tkinter.Menu(menu, background="red", foreground="red", relief="flat", border=8, tearoff=0)
    opcoes = "Contas User  Usuários  Email Services  Login Cad. Usuário  Variáveis do Sistema  Sair".split("  ")
    for opcao in opcoes:
        file_menu.add_command(label=opcao, command=command, background="black")
    menu.add_cascade(label="Cadastro", menu=file_menu)

    w.config(menu=menu)
    return w

main()
tkinter.mainloop()