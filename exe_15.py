#CONCLUIDO
# Em uma competição de salto em distância cada atleta tem direito
# a cinco saltos. O resultado do atleta será determinado pela média dos cinco
# valores restantes. Você deve fazer um programa que receba o nome e as cinco
# distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os
# saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
import time
size = 6;
array = [];
soma = 0;
name = str(input('Atleta : '));

if name == "":
    print('Deve informa o nome ')
else:

    for i in range(1,size):
        salto = float(input(f'{i}° Salto :'));
        array.append(salto)

    time.sleep(1);
    print(f'Resultado final \n ' \
            f'Atleta : {name}');


    print("Saltos:", "-".join(str(x) for x in array))   
    for x in array :
        soma += x

    print(f'Média de saltos é {soma/len(array)} m')