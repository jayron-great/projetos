from random import randint

valor = randint(1, 100)
print(valor)

while True:
    chute = int(input('Digite um valor: '))
    if chute != valor:
        if chute > valor:
            print('Digite um valor menor!')
        else:
            print('Digite um valor maior!')
    else:
        print('Você acertou!!!!')
        break
