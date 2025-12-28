#Exercicio Concluido
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

a = [1,2,3,4,5,6,7,8,9,10];
b = [11,12,13,14,15,16,17,18,19,20];
c = [21,22,23,24,25,26,27,28,29,30];
d = [];

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
    c.append(c[i])

print(d)