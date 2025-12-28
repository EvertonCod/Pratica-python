#FUNÇÃO ISALPHA
#Verifica se foi digitado algum numero onde era para ser digitado apenas letras
# nome = str(input(':'))
# print(nome.isalpha())
#-=-=-=-=-=-=-=-=-=-=
#FUNÇÃO STRIP
#Função STRIP() Podemos utiliza-lo para remoer espaços mal digitados pelo usuario ou remover caracteres especificos 
#No texto como @,!,#,$,%
# texto_sem_espacos = "Olá, Mundo!"
# texto_com_espacos = "                Ola Mundo!@";
# remover = texto_com_espacos.strip()
# remover = remover.strip('!@')
# print(remover)

#-=-=-=-=-=-=-=-=-=-=
#FUNÇÃO LOWER
#Serve basicamente para convertes todo o texto digitado pelo
#  usuario em um unico padrao de letra minuscula
# Normalização de Dados: Garante que textos sejam
# comparados de forma consistente,
# independentemente de como foram digitados (ex: "Email" vs "email").

# text = "HeLlO, WoRlD! 123"
# lowercase_text = text.lower()

# print(f"Original: {text}")
# print(f"Lowercase: {lowercase_text}")
#-=-=-=-=-=-=-=-=-=-=
#FUNÇÃO REPLACE
#Esse metodo serve para substituir ocorrencias de uma subtring por outra
# dentro de uma string, retornando uma nova string com as mudanças, já que 
#string são imutáveis.

# texto = 'Python é demais!';
# novo_texto = texto.replace('demais', 'fantastico');
# print(novo_texto)
# texto_com_numero = "EVER3TON";
# texto_limpo = texto_com_numero.replace('3', "")
# print(texto_limpo)