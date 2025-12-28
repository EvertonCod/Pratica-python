#CONCLUIDO
#Faça um programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão 
# ser compostos pelos elementos intercalados dos dois outros vetores.

a = [1,2,3,4,5,6,7,8,9,10];
b = [11,12,13,14,15,16,17,18,19,20];
c = [];

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])


print(c)