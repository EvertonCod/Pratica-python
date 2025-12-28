# EXERCICIO CONCLUIDO
# Faça um programa que carregue uma lista com os
#  modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
#  Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros
#  cada um desses carros faz com um litro de combustível. Calcule e mostre:

# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para
#  percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais
#  próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.



array_carros = {
    'Fusca':7,
    'Gol':10,
    'peugeout':14.5,
    'Vectra':12.5
};

cont = 1
for chave, valor in array_carros.items():
    print(f'Veiculo {cont}');
    print(f'Nome: {chave}');
    print(f'Km por litro: {valor}');
    cont+=1
maior_consumo = 0
mais_economico = None
cont = 1
for chave, valor in array_carros.items():
    calculo_litros = 1000/valor
    calculo_gasolina = 2.25*calculo_litros
    print(f' {cont}- {chave} - {valor} - {calculo_litros:.1f} Litros - R$ {calculo_gasolina:.1f}')
    cont+=1

    if valor > maior_consumo:
        maior_consumo = valor;
        mais_economico = chave;

print(f'O carro mais economico é o{mais_economico} com apenas')