import socket
import traceback

class ConexaoHttp:
    PORT = 80
    html = b""

    def __init__(self, host):
        self.HOST = (host)
        self.mensagem = 'GET / HTTP/1.1\r\nHost:'+self.HOST+'\r\n\r\n'

    def conectar(self, timeout):
        print("> " + self.HOST + " [" + socket.gethostbyname(self.HOST) + "]")
        valor_ret = False
        
        try:
            self.mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # refazer soket toda vez
            self.mysock.connect((self.HOST, self.PORT))
            print("Sucesso ao conectar!")
        except Exception:
            # self.mysock.close()
            print("Falha ao tentar conectar!")
            traceback.print_exc()
        else:
            self.mysock.sendall(self.mensagem.encode())
            self.mysock.settimeout(timeout)
            valor_ret = True

        return valor_ret

    def getHTML(self):
        self.html = b""
        valor_ret = False
       
        while True:
            try:
                self.recebido = self.mysock.recv(1024)
                self.html = self.html + self.recebido
            except Exception:
                traceback.print_exc()
                break
            else:
                valor_ret = True

        return valor_ret

    def encerrar(self):
        self.mysock.close()

    def printHeader(self):
        self.pos = self.html.find(b"\r\n\r\n")
        print('Header length', self.pos)
        print(self.html[:self.pos].decode())

        return self.html[:self.pos].decode()

    def criarHTML(self):
        self.fhand = open("index.html", "wb")
        self.fhand.write(self.html[self.pos+8:])
        self.fhand.close()
