def converte_binario(num):
    bin = ""
    n = num
    while n > 0:
        bin += str(n % 2)
        n = int(n / 2)
    bin = bin[::-1]
    bin = bin.zfill(8)
    return bin

def converte_binario_lista(lista):
    bs = []
    for octeto in lista:
        bin = converte_binario(octeto)
        bs.append(bin)
    return bs

def converte_octeto_binario_decimal_lista(lista):
    bs = []
    for octeto in lista:
        bin = converte_octeto_binario_decimal(octeto)
        bs.append(bin)
    return bs

def converte_octeto_binario_decimal(octeto):
    octeto_str = str(octeto)
    decimal = 0
    i = 7
    j = 0
    while i >= 0:
        decimal += int(octeto_str[i]) * 2 ** j
        j += 1
        i -= 1
    return decimal

def inverte_octeto(lista_octetos):
    for i  in range(len(lista_octetos)):
        octeto = lista_octetos[i]
        novo_octeto = ""
        for j in range(len(octeto)):
            if octeto[j] == "1":
                novo_octeto += "0"
            else:
                novo_octeto += "1"
        lista_octetos[i] = novo_octeto

class IPAddress():
    def __init__(self, IPv4, mascara):
        mascara_partes = list(map(int, mascara.split('.')))
        IPv4_partes    = list(map(int, IPv4.split('.')))
        if len(mascara_partes) == 4 and len(IPv4_partes) == 4:
            self.IPv4 = IPv4
            self.mascara = mascara
            self.rede = str(mascara_partes[0] & IPv4_partes[0]) + "." + str(mascara_partes[1] & IPv4_partes[1]) + "." + str(mascara_partes[2] & IPv4_partes[2]) + "." + str(mascara_partes[3] & IPv4_partes[3])   
        
            mascara_octetos = converte_binario_lista(mascara_partes)
            inverte_octeto(mascara_octetos)
            nova_mascara = converte_octeto_binario_decimal_lista(mascara_octetos)

            self.broadcast = str(nova_mascara[0] | IPv4_partes[0]) + "." + str(nova_mascara[1] | IPv4_partes[1]) + "." + str(nova_mascara[2] | IPv4_partes[2]) + "." + str(nova_mascara[3] | IPv4_partes[3])   
        else:
            self.IPv4 = ""
            self.mascara = ""
            self.rede = ""
            self.broadcast = ""

    def pertence_a_rede(self, ip):
        ip_partes      = list(map(int, ip.split('.')))
        mascara_partes = list(map(int, self.mascara.split('.')))
        rede_partes = list(map(int, self.rede.split('.')))
        if len(ip_partes) == 4 and len(mascara_partes) == 4 and len(rede_partes) == 4:
            i = 0
            for i in range(4):
                if ip_partes[i] & mascara_partes[i] != rede_partes[i]: return False
            return True
        return False
    
    def __str__(self):
        mascara_partes = list(map(int, self.mascara.split('.')))
        if len(mascara_partes) == 4:
            mascara_octetos = converte_binario_lista(list(map(int, self.mascara.split('.'))))
            mascara_CIDR = 0
            for octeto in mascara_octetos:
                for num in octeto:
                    if num == "1": mascara_CIDR += 1
            return self.IPv4 + "/"  + str(mascara_CIDR)
        return ""

teste = IPAddress("192.168.1.10", "255.255.255.0")
print(teste.rede)   
print(teste.broadcast)  
print(teste)      
print(teste.pertence_a_rede("192.168.1.55"))  # True
print(teste.pertence_a_rede("192.168.2.1"))   # False