import random

print('*****************')
print('Bem vindo ao jogo')
print('*****************')

numero_secreto=round(random.randrange(1,51))
total_de_tentativas = 3 
pontos = 1000

print("Qual o nível desejado?\n")
print("(1) Fácil (2) Médio (3) Difícil")

print(numero_secreto)

nivel = int(input("digite o nivel desejado"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1,total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas} ")
    chute = int(input('Digite o seu número: '))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    print(f'Você digitou {chute}') 

if(acertou):
    print(f"Você ")

 
    if(numero_secreto == chute):
        print('Você acertou!')
        break
    else:
        if(chute > numero_secreto):
            print('Você errou! Seu número foi maior do que o número secreto')
        elif(chute < numero_secreto):
            print('Você errou! Seu número foi menor do que o número secreto')
            pontos_perdidos =abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    

    print('@@@@@@@@@@@')
    print('Fim de jogo')
    print('@@@@@@@@@@@')
