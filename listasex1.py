numeros = []
for i in range(6):
    numero = float(input("digite o "+ str(i +1)+" numero"))
    numeros.append(numero)
abaixo = []
acima_media = []
soma = sum(numeros)
media = soma/6
for i in numeros:
    if i < media:
        abaixo.append(i)
    else:
        acima_media.append(i)
print(media)
print(" Os numeros abaixo da media são:", abaixo)
print("os numeros acima ou na media são: " , acima_media)