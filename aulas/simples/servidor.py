import socket
porta=4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", porta))
# s.listen(1) # tamanho da fila, ou seja, pode lidar com um cliente enquanto agurda outro. ou seja se tiver 3 conexoes o 3 vai ser recusada
s.listen(1)
print("Escutando...")
clientesocket, address = s.accept()
print(f"conexão com {address} estabelecida.")
msg = clientesocket.recv(100) # o mundo é nalogico, Funciona com bytes
mensagem = msg.decode("utf-8") # tem que converter os bytes
print(f"Recebido: {mensagem}")
resposta = "Obrigado por falar comigo"
clientesocket.send(bytes(str(resposta), "utf-8"))
clientesocket.close