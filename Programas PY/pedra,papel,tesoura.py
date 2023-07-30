import random
import os
from colorama import Fore, Back, Style


print("===========================================")
print("Bem vindo ao jogo de Pedra, Papel e Tesoura")
print("===========================================")

print("\n")

# Definindo as variáveis:
my_pts = 0
pc_pts = 0

while True:
    
# Placar do jogo:
    print("PLACAR:")
    print("Você: {}".format(my_pts))
    print("Computador: {}".format(pc_pts))

    print("\n")

# jogo:
    print("Escolha seu lance:")
    print("| 0 - Papel | | 1 - Pedra | | 2 - Tesoura |")
    lance_user = int(input())
    lance_pc = random.randint(0,2)


    if lance_user == 0:
        os.system("cls") or None
        print("=================")
        print("Sua jogada:" + Fore.GREEN + " Papel" + Fore.RESET)
        if lance_pc == 0:
            print("Jogada do Computador:" + Fore.RED + " Papel" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Empate!" + Fore.RESET)
            print("=================")
        elif lance_pc == 1:
            print("Jogada do Computador:" + Fore.RED + " Pedra" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.GREEN + "Você venceu!" + Fore.RESET)
            my_pts += 1
            print("=================")
        else:
            print("Jogada do Computador:" + Fore.RED+ " Tesoura" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.RED + "Você perdeu!" + Fore.RESET)
            pc_pts += 1
            print("=================")
    elif lance_user == 1:
        os.system("cls") or None
        print("=================")
        print("Sua jogada:" + Fore.GREEN + " Pedra" + Fore.RESET)
        if lance_pc == 0:
            print("Jogada do Computador:" + Fore.RED + " Papel" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.RED + "Você perdeu!" + Fore.RESET)
            pc_pts += 1 
            print("=================")
        elif lance_pc == 1:
            print("Jogada do Computador:" + Fore.RED + " Pedra" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Empate!" + Fore.RESET)
            print("=================")
        else:
            print("Jogada do Computador:" + Fore.RED + " Tesoura" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.GREEN + "Você venceu!"+ Fore.RESET)
            my_pts += 1
            print("=================")
    elif lance_user == 2:
        os.system("cls") or None
        print("=================")
        print("Sua jogada:" + Fore.GREEN + " Tesoura" + Fore.RESET)
        if lance_pc == 0:
            print("Jogada do Computador:" + Fore.RED + " Papel" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.GREEN + "Você venceu!" + Fore.RESET)
            my_pts += 1
            print("=================")
        elif lance_pc == 1:
            print("Jogada do Computador:" + Fore.RED + " Pedra" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.RED + "Você perdeu!" + Fore.RESET)
            pc_pts += 1 
            print("=================")
        else:
            print("Jogada do Computador:" + Fore.RED + " Tesoura" + Fore.RESET)
            print('\n')
            print("------- RESULTADO ------")
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Empate!" + Fore.RESET)
            print("=================")
    print("\n")
    print("--------------------------------------------")
    print("Jogar novamente? 0 - SIM | | 1 - NÃO")
    cond = int(input())
    if cond == 1:
        os.system("cls") or None
        print("Obrigado, volte sempre!")
        break
    else:
        os.system("cls") or None