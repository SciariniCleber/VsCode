"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
# print('Valor' if False else 'Outro valor' if False else 'Fim')
comparador = 10 == 9
varComp = ('Verdadeiro' if comparador else 'Falso')
print(varComp)
digito_cpf = 10
novo_digito_cpf = digito_cpf if digito_cpf <= 9 else 0
print(novo_digito_cpf)