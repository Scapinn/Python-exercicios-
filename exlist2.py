list1 = []
list2= []
for soca in range(5):
    primeros = int(input("digite os primeiros numeros"))
    list1.append(primeros)
for duque in range(5):
    segundos = int(input("digite outros numeros "))
    list2.append(segundos)
list2.extend(list1)

print(list2)