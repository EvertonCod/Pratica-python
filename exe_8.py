#EXERCICIO CONCLUIDO
#Faça um programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
array  = [];
altura_ = [];
idade_  = [];
for i in range(2):
    idade  = int(input('Idade :'));
    altura = float(input('Altura :'));
    
    idade_.append(idade);
    altura_.append(altura);


box = len(idade_) - 1;
box_ = len(altura_)-1;
for i in range(len(idade_)):
    print(idade_[box]);
    print(altura_[box_])
    box-=1;
    box_-=1



