cadastro = []
while True:
    print("novo cadastro")
    nome = input("Digite seu nome completo")
    cpf= input("Digite seu cpf")
    rg = input("Digite seu rg")
    novo_cadastro = (nome, cpf, rg)
    cadastro.append(novo_cadastro)
    continuar = input("deseja fazer um novo cadastro? Se sim, digite S. Se não, digite N")
    if continuar.upper() == "N":
        break
print(cadastro)
