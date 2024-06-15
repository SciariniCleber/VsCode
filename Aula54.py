import os # Para limpar o terminal

lista = []

while True:
    print('Escolha uma opçao:')
    opçao = input('[I]nserir, [A]pagar, [L]istar, [S]air: ').lower()

    if opçao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)

    elif opçao == 'a':
        os.system('cls')
        indice_str = input('Escolha o indice que voce deseja apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        
        except ValueError:
            print('O valor digitado nao é um numero')
        except IndexError:
            print('O indice nao existe')
        except Exception:
            print('Erro desconhecido')
    
        
    elif opçao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
                print(i, valor)

    elif opçao == 's':
        os.system('cls')
        break
    
    
    else:
        print('Por favor, escolha "I", "A", "L" ou "S"')

# try:
#     mostrar = input('[l]ista, [a]pagar, [i]nserir: ').lower().startswith()
        
        
#     if mostrar == 'l':
#         print('teste')
    
#     if mostrar == 'a':
#         print('teste2')

#     if mostrar == 'i':
#         inserir_lista = 'Insira o item: '
#         lista.append(enumerate(inserir_lista)) 

#         lista =+1

# except:
#     ...