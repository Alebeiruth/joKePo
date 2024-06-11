
from random import randint

print("Bem-Vindo ao jogo JO-KEN-PO")

# Variáveis e contadores
itens = ('Pedra', 'Papel', 'Tesoura')
vitoriaPlayerOne = 0
vitoriaPlayerTwo = 0
empate = 0

# Laço de repetição WHILE contendo modalidades de jogo e lógica geral do jogo
while True:
    print("""Qual a modalidade que você deseja jogar:
    1 - humano x humano
    2 - humano x computador
    3 - computador x computador""")
    modalidade = int(input("Escolha sua opção: "))

    # Humano x humano
    if modalidade == 1:
        print("Você escolheu humano x humano")
        jogador1 = int(input("Jogador One - Escolha sua jogada (0 - Pedra, 1 - Papel, 2 - Tesoura): "))
        jogador2 = int(input("Jogador Two - Escolha sua jogada (0 - Pedra, 1 - Papel, 2 - Tesoura): "))
    # Humano x computador
    elif modalidade == 2:
        print("Você escolheu humano x computador")
        jogador1 = int(input("Jogador One - Escolha sua jogada (0 - Pedra, 1 - Papel, 2 - Tesoura): "))
        jogador2 = randint(0, 2)
        print(f"Computador jogou {itens[jogador2]}")
    # Computador x computador
    else:
        print("Você escolheu computador x computador")
        jogador1 = randint(0, 2)
        jogador2 = randint(0, 2)
        print(f"Jogador One jogou {itens[jogador1]}")
        print(f"Jogador Two jogou {itens[jogador2]}")

    # Lógica do jogo de empate
    if jogador1 == jogador2:
        print("Empatou!")
        empate += 1
    # Lógica para determinar o vencedor e demostrar as vitorias possiveis no jogo
    elif (jogador1 == 0 and jogador2 == 2) or (jogador1 == 1 and jogador2 == 0) or (jogador1 == 2 and jogador2 == 1):
        print("Jogador One venceu, parabéns!")
        vitoriaPlayerOne += 1
    else:
        print("Jogador Two venceu, parabéns!")
        vitoriaPlayerTwo += 1

    # Decisão final do encerramento do loop while com break ou sua continuidade, com adiçaõ de upper() para manter input em letra maiuscula
    decisao = input("Digite 'CONTINUAR' para seguir jogando ou 'SAIR' para deixar: ").upper()
    if decisao == "SAIR":
        break

# Somatória das contagens de vitórias e empates
print("Obrigado por jogar comigo ou com seu amigo(s)!")
print(f"Placar final: Jogador One --> {vitoriaPlayerOne} vitórias, Jogador Two --> {vitoriaPlayerTwo} vitórias, Empates ao total {empate}")
