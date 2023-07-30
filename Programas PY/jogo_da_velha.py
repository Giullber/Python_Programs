from collections import UserString
from logging.config import dictConfig
import random
import os
from colorama import Fore, Back, Style

# Definindo variáveis
posicao = [1,2,3,4,5,6,7,8,9]

class velha_game:
    def __init__(self):
        self.reset()

    def layout_menu(self):
        global posicao
        print("Bem vindo ao jogo da velha! \nBy Giullber Valentim da Silva")
        print("\n")
        print("O jogo seguirá o seguinte esquema de espaços:")
        print("  {}  |".format(posicao[0])," {}  |".format(posicao[1])," {} ".format(posicao[2]))
        print("-----|-----|-----")
        print("  {}  |".format(posicao[3])," {}  |".format(posicao[4])," {} ".format(posicao[5]))
        print("-----|-----|-----")
        print("  {}  |".format(posicao[6])," {}  |".format(posicao[7])," {} ".format(posicao[8]))
       
    def user(self):
        global esco_user
        if esco_user == 1:
            self.user = "O" 
            self.pc = "X"
            return self.user
        elif esco_user == 2:
            self.user = "X"
            self.pc = "O" 
            return self.user
    def pc(self):
        return self.pc

    def layout_game(self):
        print("")
        print("  " + self.table[0] + "  |  " + self.table[1] + "  |  " + self.table[2])
        print("-----|-----|-----")
        print("  " + self.table[3] + "  |  " + self.table[4] + "  |  " + self.table[5])
        print("-----|-----|-----")
        print("  " + self.table[6] + "  |  " + self.table[7] + "  |  " + self.table[8])

    def escolha(self):
        print("Você joga com: {}".format(user) )
        print("Maquina joga com: {}".format(pc) )

    def reset(self):
        self.table = [" "," "," "," "," "," "," "," "," "]
        self.done = ""
      
    def teste_vit_emp(self):
        dict_win = {}

        for i in [user,pc]:
            # Linhas
            dict_win[i] = (self.table[0] == self.table[1] == self.table[2] == i)   
            dict_win[i] = (self.table[3] == self.table[4] == self.table[5] == i) or dict_win[i]
            dict_win[i] = (self.table[6] == self.table[7] == self.table[8] == i) or dict_win[i]

            # Colunas
            dict_win[i] = (self.table[0] == self.table[3] == self.table[6] == i) or dict_win[i]  
            dict_win[i] = (self.table[1] == self.table[4] == self.table[7] == i) or dict_win[i]
            dict_win[i] = (self.table[2] == self.table[5] == self.table[8] == i) or dict_win[i]

            # Diagonais
            dict_win[i] = (self.table[0] == self.table[4] == self.table[8] == i) or dict_win[i]  
            dict_win[i] = (self.table[2] == self.table[4] == self.table[6] == i) or dict_win[i]

        if dict_win[user]:
            self.done = "x"
            print("Parabéns, você venceu!")
        elif dict_win[pc]:
            self.done = "o"    
            print("Você Perdeu!")
            
        c = 0
        for i in range (9):
            if self.table[i] != " ":
                c += 1
                
        if c == 9:
            self.done = "d"
            print("Empate!")
    

    def user_move(self):
        invalid_move = True
        while invalid_move:
            try:
                print("Escolha um espaço entre 1 e 9:")
                espaco_user = int(input()) - 1

                if espaco_user > 8 or espaco_user < 0:
                    print("Espaço inválido")
                
                if self.table[espaco_user]!= " ":
                    print("Espaço já preenchido.")
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_move = False
        self.table[espaco_user] = user

    def pc_move(self):
        lista_disp = []
        for i in range (9):
            if self.table[i] == " ":
                lista_disp.append(i)

        if len(lista_disp) > 0:
            espaco_pc = random.choice(lista_disp)
            self.table[espaco_pc] = pc
            

game = velha_game()
#game.layout_menu()
cond_rep = 0

game.user
while cond_rep == 0:
    os.system("cls") or None
    game = velha_game()
    game.layout_menu()
    print("\n")   
    print("Você quer jogar com O ou X? \nDigite: 1 = O || 2 = X")
    esco_user = int(input())
    user = game.user()
    user =  Fore.GREEN + str(user)+ Fore.RESET
    pc = game.pc
    pc = Fore.RED + str(pc) + Fore.RESET
    while game.done == "":
        os.system("cls") or None
        game.escolha()
        game.layout_game()
        game.user_move()
        game.teste_vit_emp()
        game.pc_move()
        game.teste_vit_emp()
        os.system("cls") or None
        game.escolha()
        game.layout_game()
        game.teste_vit_emp()

    print("\n")
    print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")
    cond_rep = int(input())
    if cond_rep == 1:
        print("Obrigado, até mais!")
        break
    else:
        game.reset()
        cond_rep = 0