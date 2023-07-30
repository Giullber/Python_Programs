import os

print("=============================")
print('Você deseja utilizar a calculadora?')
print('0: Sim    1: Não')
print("=============================")
opc = int(input())
os.system('cls') or None

if opc == 0:
    while True:
        os.system('cls') or None 
        print("Calculadora ATIVADA!!")
        print("=============================")
        print("Operações suportadas")
        print("0 : Soma",  "\n1 : Subtração", "\n2 : Multiplicação","\n3 : Divisão","\n4 : Exponenciação")
        print("=============================")
        print("\n")
        print("Escolha uma operação:")
        n_opr = int(input())
        opr = {0:"Soma", 1:"Subtração", 2:"Multiplicação", 3:"Divisão", 4:"Exponenciação"}
        os.system('cls') or None
        while (n_opr > 4):
            print("!------>>>>  ERROR  <<<<-------!")
            print("Você digitou um número inválido! \n\nPor favor, escolha uma operação:")
            print("0 : Soma",  "\n1 : Subtração", "\n2 : Multiplicação","\n3 : Divisão","\n4 : Exponenciação")
            n_opr = int(input())
            os.system('cls') or None
    
        print("=============================")
        print(">>>>>> Operação selecionada: \n>>>>>> {}".format(opr[n_opr].upper()))
        print("=============================")

        print("Qual o primeiro valor:")
        v1 = float(input())
        print("Qual o primeiro valor:")
        v2 = float(input())
        os.system('cls') or None
        
        print("=============================")
        print(" === Resultado === ")
        if n_opr == 0:
            soma = v1 + v2
            print("{} + {} = {}".format(v1,v2,soma))   
        elif n_opr == 1:
            sub = v1 - v2
            print("{} - {} = {}".format(v1,v2,sub))
        elif n_opr == 2:
            mult = v1 * v2
            print("{} * {} = {}".format(v1,v2,mult))
        elif n_opr == 3:
            div = v1 / v2
            print("{} / {} = {}".format(v1,v2,div))
        elif n_opr == 4:
            exp = v1 ** v2
            print("{}^{} = {}".format(v1,v2,exp))
        
        print("")
        print("=============================")
        print("Você deseja fazer mais alguma operação? \n0: SIM   \n1: NÃO")
        print("=============================")
        cond = int(input())
        if cond == 1:
            os.system("cls") or None
            print("Calculadora DESATIVADA!!")
            print("=============================")
            print("Muito Obrigado, volte sempre!")
            print("=============================")
            break
else:
    print("=============================")
    print("Muito Obrigado, volte sempre!")
    print("=============================")