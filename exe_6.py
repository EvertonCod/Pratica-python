#EXERCICIO CONCLUIDO
vogal = ['a','e','i','o','u'];
palavra = ['p','r','o','p','a','r','o','x','i','t','o','n','a'];

teste = palavra[0] not in vogal[0]
print(teste)

consoantes = []

for i in palavra:

    if i not in vogal:
        consoantes.append(i)

print(f'Quantidade de consoantes: {len(consoantes)}')
print('Consoantes:', consoantes)