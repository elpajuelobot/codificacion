cadena = input("ingresa un texto: ")
cadenacodificada = []
cadenadecodificada = []
for i in cadena:
    cadenacodificada.append(chr(ord(i) - 30))

print(cadenacodificada)

for i in cadenacodificada:
    cadenadecodificada.append(chr(ord(i) + 30))

print(cadenadecodificada)

for i in cadenacodificada:
    print(i,end="")

print("")

for i in cadenadecodificada:
    print(i,end="")