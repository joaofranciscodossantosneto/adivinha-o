print('*****************')
print('Bem vindo ao jogo')
print('*****************')

chute = int(input('Digite o seu número: '))

numero_secreto = 12
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto


print(f'Você digitou {chute}') 

if(numero_secreto == chute):
    print('Você acertou!')
else:
    if(chute > numero_secreto):
        print('Você errou! Seu número foi maior do que o número secreto')
    elif(chute < numero_secreto):
        print('Você errou! Seu número foi menor do que o número secreto')

    print('@@@@@@@@@@@')
    print('Fim de jogo')
    print('@@@@@@@@@@@')