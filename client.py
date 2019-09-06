import socket
import time


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(2)

    host = socket.gethostbyname("unb.br")
    port = 80
    sentence = "GET / HTTP/1.1\r\nHost:"+host+"\r\n\r\n"

    s.connect((host, port))
    s.send(sentence.encode())
    tm = s.recv(4096)

    while True:
        print(tm.decode())
        try:
            tm = s.recv(4096)
        except:
            print("No data receveided.")
            break

    s.close()


if __name__ == "__main__":
    main()
