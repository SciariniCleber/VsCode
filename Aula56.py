"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          ' #Imutavel
lista_frases_cruas = frase.split(',') #o que eu colocar dentro do () sera onde ele ira quebrar a frase, caso nao tenha nada sera nos espaços
print(lista_frases_cruas)

lista_frases = [] #Lista Vazia que vai ser alterado con append e sera adicionado o valor da lista_frases_cruas
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #strip corta os espaços no começo e no final da frase ou rstrip = corta o espaço da direita e lstrip = corta o espaço da esquerda

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases) #Faz a uniao de frases(String,tuplas)
print(frases_unidas)