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

class UI:
    def __init__(self):
        self.endereco = None
        self.opcao = 0
        self.msg = ""

    def main(self):
        rodando = True
        while rodando:
            try:
                if self.opcao == 0:
                    self.selecao()
                elif self.opcao == 1:
                    self.criar_rede()
                elif self.opcao == 2:
                    self.ver_CIDR()
                elif self.opcao == 3:
                    self.ver_ip()
                elif self.opcao == 4:
                    self.ver_mascara()
                elif self.opcao == 5:
                    self.ver_rede()
                elif self.opcao == 6:
                    self.ver_broadcast()
                elif self.opcao == 7:
                    self.testar_ip_pertence_rede()
                elif self.opcao == -1:
                    rodando = False
            except:
                self.opcao = 0
                print("Ocorreu algum erro")
    
    def selecao(self):
        print("Digite:")
        ops = 7
        print("    \"1\" | Para criar rede")
        if self.endereco != None:
            print("    \"2\" | Para ver CIDR")
            print("    \"3\" | Para ver ip")
            print("    \"4\" | Para ver mascara")
            print("    \"5\" | Para ver rede")
            print("    \"6\" | Para ver broadcast")
            print("    \"7\" | Para verificar se ip exite na rede")
        print("    \"-1\" | Para sair do sistema")

        if self.msg != "":
            print(self.msg)

        op = input("Digite aqui: ")
        print(op)
        if op == None or op == "":
            self.msg = ""
        else:
            self.opcao = int(op) if -1 <= int(op) <= ops else 0

    def criar_rede(self):
        ip = input("Digite um ip: ")
        mascara = input("Digite a mascara da rede: ")
        self.endereco = IPAddress(ip, mascara)
        self.opcao = 0

    def ver_CIDR(self):
        self.msg = self.endereco
        self.opcao = 0

    def ver_ip(self):
        self.msg = self.endereco.IPv4
        self.opcao = 0
    
    def ver_mascara(self):
        self.msg = self.endereco.mascara
        self.opcao = 0

    def ver_rede(self):
        self.msg = self.endereco.rede
        self.opcao = 0
    
    def ver_broadcast(self):
        self.msg = self.endereco.broadcast
        self.opcao = 0

    def testar_ip_pertence_rede(self):
        pertence = self.endereco.pertence_a_rede(input("Digite um ip: "))
        self.msg = "Pertence" if pertence else "Não Pertence"
        self.opcao = 0

ui = UI()
ui.main()