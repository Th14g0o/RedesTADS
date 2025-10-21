ip = "10.9.0.222"
mask = "255.255.255.224"

binario = []
binario_masc = []

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

temp = list(map(int, ip.split(".")))    
binario = converte_binario_lista(temp)
temp = list(map(int, mask.split(".")))
binario_masc = converte_binario_lista(temp)

print("IP:",*binario)
print("Mascara:", *binario_masc)

#mascara_invertida_binaria = []  
for i  in range(len(binario_masc)):
    octeto = binario_masc[i]
    novo_octeto = ""
    for j in range(len(octeto)):
        if octeto[j] == "1":
            novo_octeto += "0"
        else:
            novo_octeto += "1"
    binario_masc[i] = novo_octeto
    #mascara_invertida_binaria.append(novo_octeto)        

print("Mascara Invertida:", *binario_masc)

ipInt = int(binario[0] + binario[1] + binario[2] + binario[3])
maskInvertInc = int(binario_masc[0] + binario_masc[1] + binario_masc[2] + binario_masc[3])
broad = ipInt | maskInvertInc

broadip = str(broad)
print(broadip)
broadip = broadip[0:8] + "." + broadip[9:18] + "." + broadip[19:28]
print(broadip)

def bin2oct(ipBin):
    byti = ""
    for octec in range(0, 32, 8):
        byti += str(int(ipBin[octec:octec+8]))
        byti += "."
    return byti[:-1]
