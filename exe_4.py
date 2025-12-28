#Imprima na tela a quantidade de numeros repetidos
lista = [3, 7, 2, 7, 10, 2,7]



for i in range(len(lista)):
   
    box = lista[i]
  
    cont = 0
    for x in lista:
        
        if box == x:
            cont+=1
            

        if cont > 1:
            print(f'{x} aparece {cont}x')
          
