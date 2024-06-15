import random
import sys

# print(random.randint(0, 9))

# for _ in range(100): Para gerar 100 CPFs
nove_digitos = ''
for i in range(9): #regra para gerar um numero de ate 9 digitos
    nove_digitos += str(random.randint(0, 9)) #criando um numero de ate 9 digitos 

contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

import re #regular expression
import sys 

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = cpf_gerado_pelo_calculo
cpf_enviado_usuario = re.sub(
    r'[^0-9]', #espressao usada para tudo aquilo que nao e um numero
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)
# print(entrada)
# print(entrada[0])
# print(len(entrada))
# print(entrada_e_sequencial)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit() #para sair do python

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')