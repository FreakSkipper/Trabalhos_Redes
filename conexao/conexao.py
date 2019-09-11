import socket

class ConexaoHttp:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 80
    
    html = b""

    def __init__(self, host):
        self.HOST =  (host)
        self.mensagem = 'GET / HTTP/1.1\r\nHost:'+self.HOST+'\r\n\r\n'
    def conectar(self, timeout):    
        self.mysock.connect((self.HOST, self.PORT))
        self.mysock.sendall(self.mensagem.encode())
        self.mysock.settimeout(timeout)

    def getHTML(self):
        self.html = b""
        while True:
            try:
                self.recebido = self.mysock.recv(1024)
                self.html = self.html + self.recebido    
            except:
                print("Conexao Encerrada.")
                break
    
    def encerrar(self):
        self.mysock.close()

    def printHeader(self):
        self.pos = self.html.find(b"\r\n\r\n")
        print('Header length', self.pos)
        print(self.html[:self.pos].decode())


    def criarHTML(self):
        self.html = self.html[self.pos+8:]
        self.fhand = open("index.html", "wb")
        self.fhand.write(self.html)
        self.fhand.close()