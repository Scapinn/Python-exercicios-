matriz1 = []
matriz2 = []
matriz_soma =[]
for i in range(3):
    a = int(input("Digite um numero que formará a primeira matriz 3X3"))
    b = int(input("Digite um numero que formará a primeira matriz 3X3"))
    c = int(input("Digite um numero que formará a primeira matriz 3X3"))
    matriz1.append([a,b,c])
for i in range(3):
    d = int(input("Digite um numero que formará a segunda matrix 3x3"))
    e = int(input("Digite um numero que formará a segunda matrix 3x3"))
    f = int(input("Digite um numero que formará a segunda matrix 3x3"))
    matriz2.append([d,e,f])
for i in range(3):
    matriz_soma.append([])
    for j in range(3):
        soma = matriz1[j] + matriz2[j]
        matriz_soma.append(soma)
print(matriz_soma)
