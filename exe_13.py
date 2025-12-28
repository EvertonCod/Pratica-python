#Exercicio Concluido
#Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos.
# possuem altura inferior à média de altura desses alunos.
size         = 2
idade_array  = []
altura_array = []
media = 0
cont = 0

for i in range(size):
    idade  = int(input('Idade : '))
    altura = float(input('Altura : '))

    idade_array.append(idade)
    altura_array.append(altura)

print(idade_array)
print(altura_array)

# Calcula média
for i in range(len(altura_array)):
    media += altura_array[i]

media = media / size

# Conta alunos >13 e com altura menor que a média
for i in range(len(idade_array)):
    if idade_array[i] > 13:
        if altura_array[i] < media:
            cont += 1

print(f'Média : {media}')
print(f'Total de alunos com altura inferior à média: {cont}')
