# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
# a, b, c = lista

# print(a, c)
# for nome in lista:
#     print(nome, end= ' ') #end= quebra a linha no final, deixando tudo na mesma linha 

# p, b, *_, ap, u = lista - *_ significa pergar o resto da lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda') - primeiro print
# print(*lista) - e a mesma coisa da linha de cima
# print(*string) - separa de maneira igual ao primeiro print
# print(*tupla) - separa de maneira igual ao primeiro print

print(*salas, sep='\n') #usa o separador como quebra de linha, mostrando como esta a lista