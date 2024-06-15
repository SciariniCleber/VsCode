"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890) - Multiplicar o valor dos 9 digitos do cpf, com uma contagem regressiva começando pelo 10
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: - depois somar tudo
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010 - depois multiplicar por 10
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re # regular expression 

# cpf_enviado= input(f'Digite o cpf: {''}') \
#     .replace('.', '') \
#     .replace(',', '') \
#     .replace('-', '') \
#     .replace(' ', '')   
cpf_enviado = re.sub( # aqui eu chamo a regular expression
    r'[^0-9]', # aqui a regra e somente para aceitar numeros
    '', # aqui substituir por nada
    input(f'Digite o cpf: {''}') # aqui serà a entrada do usuario
)
 
nove_digitos = cpf_enviado[:9] # aqui estou pegando somente os 9 primeiros digitos
contador_regressivo_1 = 10 # contador de regras no cpf que precisa começar no 10 
resultado_digito_1 = int() # começando o resultado do primeiro digito com vazio
for digito_1 in nove_digitos: # usando for para pegar digito por digito 
    
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 # multiplicando o primeiro digito com o contador regressivo e depois somando
    contador_regressivo_1 -= 1 # com cada passagem no contador ele diminui 1 começando do 10 depois 9 e assim sucessivamente
    
digito_1 = (resultado_digito_1 * 10) % 11 # usando os parametros de multiplicaçao e resto para chegar no valor desejado
digito_1 = digito_1 if digito_1 <= 9 else 0 # se digito_1 for <=9 ele mantem o numero, se for maior serà 0
# print(digito_1)

# Segundo Digito CPF
dez_digitos = nove_digitos + str(digito_1) # adicionando o primeiro digito
contador_regressivo_2 = 11 # contador que vai ate o 11

resultado_digito_2 = int() # resultado inicial como vazio
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
# print(digito_2)


comparador_de_cpf = f'{nove_digitos}{digito_1}{digito_2}' # concatenando todos os numeros

#validando o cpf digitado
if cpf_enviado == comparador_de_cpf: 
    print(f'{cpf_enviado} è valido')
else:
    print(f'CPF {cpf_enviado} è invalido')


