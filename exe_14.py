#EXERCICIO CONCLUIDO
# Faça um programa que leia um número indeterminado de 
# valores, correspondentes a notas, encerrando a entrada de dados
#  quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

import time
loop = True;
array = [];
soma = 0;
while loop:
    box = int(input('Numero :'));
    if box == -1:
        size = len(array) -1;
        print(f'Quantidade de valores é : {len(array)}');
        print('Valores da ordem inversa :');
        for i in array:
            print(f'{array[size]}');
            size-=1;
            soma+=i;

        print(f'Soma dos valores: {soma}');
        print(f'Média dos valores: {soma/(len(array))}');
        
        media = soma/(len(array));
        soma = 0
       
        for i in array:
            if i > media:
                soma+=1
        print(f'A quantidade de valores acima da média é {soma}');

        soma = 0;
        for i in array:
            if i < 7:
                soma+=1;
        print(f'A quantidade de valores abaixo de sete é {soma}');
        

        time.sleep(1)
        print('Fim do programa')
        break;
    else:
        array.append(box);
