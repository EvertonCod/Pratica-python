#CONCLUIDO
# Faça um Programa que leia um vetor
#  A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
lista = [1,2,3,4,5,6,7,8,9,10];
soma = [];
box = 0
for i in lista:
    soma.append(i**2)
    
for i in range(len(soma)):
    box+=soma[i];

print(box)