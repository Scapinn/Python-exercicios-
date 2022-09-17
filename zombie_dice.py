#Leonardo Scapin Dias - Análise e desenvolvimento de sistemas.

import random
print( 20*"*")
print("bem vindo ao zombie dice!")
print(20*"*")
jogadores = 0
#Bloco para garantir que  terão mais de dois jogadores, também fiz uma verificação para evitar a entrada de valores não inteiros

while jogadores <=2:
    try:
        jogadores = int(input("Digite a quantidade de jogadores"))
    except ValueError:
        print("Digite apenas números")
        continue
    if jogadores <=2:
     print("São necessários, pelo menos, 3 jogadores. Chame alguns amigos!")
#Utilizei uma lista para salvar  os jogadores e os nomes, bem como os dados

lista_de_jogadores = []
for i in range(jogadores):
      nomes = input("digite o nome do " +  str( i + 1 ) + " jogador")
      #Esse print foi só para checar que todos foram salvos
      lista_de_jogadores.append(nomes)
print(lista_de_jogadores)
dado_verde = "CPCTPC"
dado_amarelo = "TPCTPC"
dado_vermelho = "TPTCPT"
dados = [ dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho,
          dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde]
dados.append(dados)
#Declarei as váriaveis que serão utilizadas no jogo
print("Inicio do jogo!")
jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0
lance = 0
#As rodadas. Atualmente estou com um bug que não está continuando as rodadas
while jogadores <= jogadores:
    print(" turno do jogador" + lista_de_jogadores[jogador_atual])
    for  lance in range(3):
        numero_sorteado = random.randint(0, 12)
        dado_sorteado = dados[numero_sorteado]
        if dado_sorteado == "CPCTPC":
            cor_dado = "verde"
        elif dado_sorteado == "TPCTPC":
            cor_dado = "amarelo"
        elif dado_sorteado == "TPTCPT":
            cor_dado = "vermelho"
        print(" O dado sorteado foi:" +  cor_dado)
        dados_sorteados.append(dado_sorteado)
    for dado_sorteado in dados_sorteados:
        face_dado = random.randint(0,5)
        if dado_sorteado[face_dado]== "C":
            print("Você comeu um cééérebrooo")
            cerebros += 1
        elif dado_sorteado[face_dado] == "T":
            print("Reção da vítima! Tomaste um tiro! ")
            tiros += 1
        elif dado_sorteado[face_dado] == "P":
            print("Passo! A vitima fugiu")
            passos += 1
    print(F" Seu resultado é de: {tiros} tiros, {passos} passos e {cerebros} cerebros")
    continuar = input("Deseja continuar seu turno ? Digite S para sim ou N para não."
                      "qualquer outra letra será considerada como não. ")
    if continuar != "N":
        continue

    elif continuar =="não" or "N" or "NÃO" or "n" :
        jogador_atual = jogador_atual +1
        tiros = 0
        passos = 0
        cerebros= 0
        if jogador_atual == len(lista_de_jogadores):
            print("fim do jogo ")
            break
    else:
        print("Iniciando mais um turno da rodada atual")
        dados_sorteados = []