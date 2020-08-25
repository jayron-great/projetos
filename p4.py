print('Bem vindo ao jogo')

def menu():
    print(''' 
Você se acorda, o que você faz?

a) choro
b) escovo os dentes
c) volto a dormir
    ''')

def opcao(resposta):
    if resposta == 'a':
        print('''
Em que lugar?
        
a) quarto
b) carro
c) cozinha
        ''')
        resposta = str(input('Escolha: ')).lower()
        lista = [resposta, 1]
        return lista

    if resposta == 'b':
        print('''
Com o que?
        
a) colgate
b) outra marca
        ''')
        resposta = str(input('Escolha: ')).lower()
        lista_b = [resposta, 2]
        return lista_b

    if resposta == 'c':
        print(''' 
Bom sono :)
        ''')

def resposta_opcao(lista):

    if lista[1] == 1:
        if lista[0] == 'a':
            print('Não se esquece de fechar a porta')
        if lista[0] == 'b':
            print('Cuidado pra nao bater')
        if lista[0] == 'c':
            print('Cuidado com as facas')

    if lista[1] == 2:
        if lista[0] == 'a':
            print('Marca boa')
        if lista[0] == 'b':
            a = str(input('Qual a marca? '))
            print(f'{a} é uma boa marca!')
menu()
r1 = str(input('Escolha: ')).lower()
r1 = opcao(r1)
r1 = resposta_opcao(r1)
