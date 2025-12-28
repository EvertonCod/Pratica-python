 #EXERCICIO CONCLUIDO 
      # 0   1  2  3  4
#lista = [14,13,12,11,10,15,18,16,17,21,19,20]
lista = [13,12,11,10,14]
#lista = [12,11,10,13,14]
#lista = [11, 10, 12, 13, 14]
#lista = [10, 11, 12, 13, 14]
#lista = [5,4,3,2,1]
#lista = [1,5,6,22,66,2,78,99,10]
#lista = [5,4,3,2,1,7,6]

print(lista)
x = 0
y = 1

p = len(lista)
a = len(lista)
while p > 1:
      # print('Inicio do While')
       #print(x)
       #print(y)
      # print(p)

       for i in lista:
             # print('Inicio do laço')
              if y == a:
                     #print('primeiro if')
                     y = 1
                     x = 0    

              if lista[x] > lista[y]:
                    # print('segundo if')
                     #print(lista)
                     box = lista[y];
                     lista[y] = lista[x];
                     lista[x] = box
                    # print(lista)
                    # print(lista[x])
                     #print(lista[y])
                     x+=1
                     y+=1
                     
              else:
                     #print('else')
                     y += 1
                     x += 1
                    
       p-=1
      # print(p)

print(lista)