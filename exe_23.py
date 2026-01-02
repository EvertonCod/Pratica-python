#Altere o programa anterior permitindo ao usuário informar
#  as populações e as taxas de crescimento iniciais. Valide
#  a entrada e permita repetir a operação.

while True:
    anos = 0
    while True:
            populacao_A = int(input('Infome a população da cidade A :'));
            if populacao_A == 0 or populacao_A < 0:
                print('Por favor digite um numero valido')
            else:
             break
             
    while True:
         taxa_A = float(input('Taxa de crescimento anual A (%):'))
         if taxa_A == 0 or taxa_A < 0:
              print('Por favor digite um numero de taxa valido')
         else:
            break
         
    while True:
        populacao_B = int(input('Infome a população da cidade B : '));
        if populacao_A > populacao_B:
            print(f'Tem certeza que a população A é maior que a B? Pois assim a população A ja ultrapassou a população B (s/n)')
            resposta_user = input('Resposta :').lower()
            if resposta_user != 's':
                 new_populacao = int(input('Nova população:'))
                 populacao_B = new_populacao
        if populacao_B == 0 or populacao_B < 0:
                print('Por favor digite um numero valido')
        else:
             break
        
    while True:
        taxa_B = float(input('Taxa de crescimento anual B (%):'))
        if taxa_A < taxa_B:
            print(f'Se o valor informado da taxa A {taxa_A}% estiver correta e da taxa B {taxa_B}%, a população A')
            print('não vai alcançar a população B')
            troca_taxa_A = input("Deseja trocar o taxa da população A ? (s/n): ").lower();
            if troca_taxa_A == 's':
                new_taxa_A = float(input('Digite a nova taxa :'));
                taxa_A = new_taxa_A;
            else:
                 break
        elif taxa_A == taxa_B:
             print(f'Lamentamos mas a  taxa da população A {taxa_A}% não pode ser igual a taxa da população B {taxa_B}% informe outro valor para a taxa B')
             troca_taxa_B = input("Deseja trocar o taxa da população B ? (s/n): ").lower();
             if troca_taxa_B == 's':
               continue
             else:
                  break
        
        elif taxa_B == 0 or taxa_B < 0:
              print('Por favor digite um numero de taxa valido');
        else:
            break


    while populacao_A < populacao_B:
        anos += 1
        populacao_A = populacao_A*(taxa_A/100) + populacao_A
        populacao_B = populacao_B*(taxa_B/100) + populacao_B

    print('-'*20)
    print(f'Daqui à {anos} anos .')
    print('-'*20)
    print(f'O país A tera {populacao_A:.0f} habitantes.')
    print(f'O páis B tera {populacao_B:.0f} habitantes.')
    print(f'Uma diferença de {populacao_A-populacao_B:.0f} habiantes ')
    print('-'*20)
    repetir = input("Deseja repetir a operação? (s/n): ").lower()
    if repetir != 's':
        break



