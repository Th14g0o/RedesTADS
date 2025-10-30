import socket
porta=4444 # porta
servidor = "127.0.0.1" # ip unicersal, si mesmo. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((servidor, porta)) # se o servidor não tiver ligado da erro aqui
msg = input("Mensagem aqui: ")
s.send(msg.encode("utf-8"))
resposta = s.recv(100) # tamanho da mensagem recebida
print("Resposta:", resposta.decode("utf-8"))