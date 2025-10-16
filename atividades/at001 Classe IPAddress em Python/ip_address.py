class IPAddress():
    def __init__(self, IPv4, mascara):
        mascara_partes = mascara.split('.')
        IPv4_partes = IPv4.split('.')
        rede = ["","","",""]
        rede[0] = IPv4_partes[0] if int(mascara_partes[0]) != 0 else "0"
        rede[1] = IPv4_partes[1] if int(mascara_partes[1]) != 0 else "0"
        rede[2] = IPv4_partes[2] if int(mascara_partes[2]) != 0 else "0"
        rede[3] = IPv4_partes[3] if int(mascara_partes[3]) != 0 else "0"
        self.rede = rede[0] +"." + rede[1] +"." + rede[2] +"." + rede[3]
        self.broadcast = ""

teste = IPAddress('192.8.2.0', '255.255.0.0')
print(teste.rede)          