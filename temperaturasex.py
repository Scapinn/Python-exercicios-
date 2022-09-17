meses = [" Janeiro", " Fevereiro", " Março", " Abril", " Maio", " Junho", " Julho", " Agosto", " Setembro",
         " Outubro", " Novembro", " Dezembro"]
tempmedia =[]
acima_da_media = []
for temp in meses:
    media = float(input(F"Qual a temperatura media do mês{temp} ?"))
    tempmedia.append(media)
media_ano = sum(tempmedia)/12
print("A media de temperatura anual foi ", media_ano)
for i in range(12):
    if tempmedia[i] >  media_ano:
        print(F"O mês de {meses[i]} ficou acima da média com {tempmedia[i]}")


