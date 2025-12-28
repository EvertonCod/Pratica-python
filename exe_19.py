#EXERCICIO CONCLUIDO
# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
#  com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele
#  é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles,
#  para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar 
# este levantamento. O programa deverá receber um número indeterminado de entradas,
#  cada uma contendo: um número de identificação do mouse o tipo de defeito:

# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
# Ao final o programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

array = {
    1:0,
    2:0,
    3:0,
    4:0
};

while True:
    numero = int(input(':'));
    if numero == 0:
        break;
    if numero == 1:
        array[1]+=1;
    
    if numero == 2:
        array[2]+=1

    if numero == 3:
        array[3]+=1
    
    if numero == 4:
        array[4]+=1
    
somatorio = 0
for i in array.values():
    somatorio+=i

print(f'{"Código":<6} {"Descrição":<35} {"Qtd":>5} {"%":>10}')
print('-' * 60)

print(f'{1:<6} {"Necessita da esfera":<35} {array[1]:>5} {(array[1]/somatorio)*100:>9.2f}%')
print(f'{2:<6} {"Necessita de limpeza":<35} {array[2]:>5} {(array[2]/somatorio)*100:>9.2f}%')
print(f'{3:<6} {"Troca do cabo ou conector":<35} {array[3]:>5} {(array[3]/somatorio)*100:>9.2f}%')
print(f'{4:<6} {"Quebrado ou inutilizado":<35} {array[4]:>5} {(array[4]/somatorio)*100:>9.2f}%')
