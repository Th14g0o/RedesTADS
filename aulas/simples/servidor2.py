import socket
import time
porta=4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", porta))
s.listen(1)
cliente = 1
while True:
    print("Escutando...")
    clientesocket, address = s.accept()
    print(f"conexão com {address} estabelecida.")
    msg = clientesocket.recv(100) # o mundo é nalogico, Funciona com bytes
    mensagem = msg.decode("utf-8") # tem que converter os bytes
    print(f"Recebido: {mensagem}")
    resposta = f"Obrigado por falar comigo, cliente numero {cliente}"
    cliente += 1
    time.sleep(3)
    clientesocket.send(bytes(str(resposta), "utf-8"))
    clientesocket.close