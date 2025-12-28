 #EXERCICIO CONCLUIDO 
#Descobrir qual é o segundo maior número da lista, que nesse caso é o 10 
lista = [7, 2, 15, 4, 10, 9,14];





maior = lista[0]
menor = lista[0]


contador = 0
contador_2 = 0
#Pega o maior numero da lista e usa como base 
for i in lista:
    if lista[contador] > maior:
        #print('If')
        maior = lista[contador]
        contador +=1
        
    else:
        #print('Else')
        contador +=1
#Pego o menor numero da lista e usa como base
for n in lista:
    if lista[contador_2] < menor:
        menor = lista[contador_2]
        contador_2+=1
    
    else:
        contador_2+=1

box = 0
for x in lista:
    if x < maior and x > box:
        print(x)
        box = x

        

print(f"Segundo maior numero: {box}")