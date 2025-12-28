#EXERCICIO CONCLUIDO
#Crie uma função que receba uma lista e retorne o maior e o menor da lista, sem usar max() nem min().
#lista  = [1,2,3,4,5,6];
#lista = [6,7,4,2,3,25,-1,-2]
lista = [-8, -3, -10, -2]



def funcao(i):
    array_lista = i
    maior = array_lista[0]
    menor = array_lista[0]

    
    #Pegar o maior numero
    for i in range(len(array_lista)):
        if array_lista[i] > maior:
            maior = array_lista[i];
        
    #Pegar o menor numero
    for i in array_lista:
        if menor < i:
            continue
        else:
            menor = i
         


    #return print(f'Maior numero da lista {maior} e menor o {menor}');
    return menor,maior
   

box = funcao(lista);
print(f'O menor numero da lista é {box[0]} e o maior {box[1]}');