from random import randint


lista_coisas = ['Sim', 'Não', 'Boa sorte', 'Ok']
pergunta = str(input('Faça sua pergunta: '))
print(f'Respota: {lista_coisas[randint(0, len(lista_coisas)-1)]}')
