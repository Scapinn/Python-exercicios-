funcionarios = []
while True:
     nome = input("Digite o nome do funcionário")
     matricula = int(input("Digite o numero da matricula"))
     dependentes = ()
     while True:
         dependente = input("digite o nome do dependente, se não houver digite N")
         if dependente =="N":

        dependentes += (dependente,)
     funcionario = (nome, matricula, dependentes)
     funcionarios.append(funcionario)
     continuar = input("Deseja cadastrar mais um funcionário? digite N se nao ")
     if continuar == "N":
         break
print(funcionarios)

