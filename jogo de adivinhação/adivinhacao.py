print('*****************')
print('Bem vindo ao jogo')
print('*****************')

numero_secreto=12
total_de_tentativas = 3
rodada=1
while  ( rodada <= total_de_tentativas ):
    print(f"Tentativa {rodada} de {total_de_tentativas} ")
    chute = int(input('Digite o seu número: '))

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

    rodada = rodada + 1

    print('@@@@@@@@@@@')
    print('Fim de jogo')
    print('@@@@@@@@@@@')