# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Estado Civil: 's', 'c', 'v', 'd';

usuario = int(input('Total de usuarios :'));
nomes_array   = [];
idade_array   = [];
salario_array = [];
estado_civil_  = [];
estado_civil_array = ['s', 'c', 'v', 'd']
for i in range(usuario):

    while True:
        nome = str(input('Nome :')).strip();
        if not nome.replace(" ", "").isalpha():
            print('Digite apenas letras ')
        elif len(nome) > 2:
            nomes_array.append(nome);
            break
        else:
            print('Por favor, seu nome deve conter mais de 2 caracteres')
    
    while True:
        try:
            idade = int(input('Idade :'));
            if idade < 151 and idade > 0:
                idade_array.append(idade)
                break
            else:
                print('Por favor digite uma idade valida')
        except ValueError:
            print('Por vador digite apenas números')
    

    while True:
        try:
            salario = float(input('Salario :').replace(',', '.'));
            if salario < 0 or salario == 0:
                print('Por favor digite um valor maior que zero')
            else:
                salario_array.append(salario)
                break
        except ValueError:
            print('Por favor digite apenas numeros')

    while True:
        estado_civil = str(input('Estado civil: "s", "c", "v", "d" : ').lower()).replace(" ", "");
        if estado_civil in estado_civil_array:
            estado_civil_.append(estado_civil);
            break
        else:
            print('Por favor digite:  "s", "c", "v", "d" para seu estado civil')




