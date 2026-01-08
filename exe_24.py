# 🏢 CENÁRIO REAL — EMPRESA DE ASSISTÊNCIA TÉCNICA
# Você trabalha em uma assistência técnica de celulares (bem próximo da sua realidade).
# Um programador júnior criou um sistema simples para registrar ordens de serviço, mas o sistema está dando problema e o gerente reclamou.
# Seu trabalho: analisar, encontrar problemas e corrigir.
# 🎯 O OBJETIVO DO SISTEMA
# O sistema deve:
# Registrar:
# Nome do cliente
# Tipo de serviço (troca_tela, bateria, software)
# Valor da peça
# Mão de obra fixa: R$ 40
# Calcular:
# Valor final do serviço
# Lucro (valor cobrado – custo da peça)
# Permitir registrar vários atendimentos
# Mostrar no final:
# Total faturado
# Total de lucro
# Quantos serviços de cada tipo foram feitos
# 💣 CÓDIGO PROBLEMÁTICO (FOI ESSE QUE TE ENTREGARAM)
# 👉 NÃO CONFIE NELE. ELE TEM ERROS DE LÓGICA E DE SEGURANÇA.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# total_faturado = 0
# lucro_total = 0
# servicos = {"troca_tela": 0, "bateria": 0, "software": 0}

# while True:
#     nome = input("Nome do cliente: ")

#     servico = input("Tipo de serviço (troca_tela, bateria, software): ")

#     valor_peca = float(input("Valor da peça: "))

#     mao_de_obra = 40

#     valor_final = valor_peca + mao_de_obra
#     lucro = valor_final - valor_peca

#     total_faturado += valor_final
#     lucro_total += lucro
#     servicos[servico] += 1

#     continuar = input("Deseja registrar outro serviço? (s/n): ")
#     if continuar == "n":
#         break

# print("Total faturado:", total_faturado)
# print("Lucro total:", lucro_total)
# print("Serviços realizados:", servicos)


total_faturado = 0
lucro_total = 0
servicos = {"troca_tela": 0, "bateria": 0, "software": 0}
control = True
while True:
    while True:
        nome = input("Nome do cliente: ").strip()

        if len(nome) < 3:
            print("O nome deve ter pelo menos 3 caracteres.")
            continue

        nome_limpo = nome.replace(" ", "").replace("-", "").replace("'", "")

        if not nome_limpo.isalpha():
            print("O nome deve conter apenas letras.")
            continue

        break


    control = True
    while control:
        servico = input("Tipo de serviço (troca_tela, bateria, software):")
        for i in servicos.keys():
            if servico == i:
                print('Tudo certo')
                control = False
            else:
                continue
                

    control = True
    while control:
        try:
            entrada = input("Valor da peça: ").strip()
            entrada = entrada.replace(",",".")
            valor_peca = float(entrada)
            if valor_peca < 0:
                print('Por favor digite um valor maior que zero')
            else:
                control = False
        except ValueError:
            print('Digite um numero valido')

    mao_de_obra = 50
    #Valor repassado ao cliente 
    valor_final = (valor_peca*2) + mao_de_obra
    lucro = valor_final - valor_peca

    total_faturado += valor_final
    lucro_total += lucro
    servicos[servico] += 1

    continuar = input("Deseja registrar outro serviço? (s/n): ")
    if continuar == "n":
        break
print('-'*20)
print("Total faturado:", total_faturado)
print("Lucro total:", lucro_total)
print("Serviços realizados:", servicos)
print('-'*20)
