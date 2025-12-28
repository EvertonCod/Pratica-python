 #EXERCICIO CONCLUIDO 
#Verificar se a lista está em ordem crescente

numeros = [1, 3, 5, 7, 10]

numeros_ = [2, 4, 4, 7, 9]


controlador_1 = 0
controlador_2 = 1

p = len(numeros)     

for i in numeros:
      if controlador_2 == p:
          print('A lista esta ordenada')
          break
      if numeros[controlador_1] < numeros[controlador_2]:
        #print('sim')
        controlador_1+=1
        controlador_2+=1
      else:
          print('A lista não esta ordenada ')
          break
          