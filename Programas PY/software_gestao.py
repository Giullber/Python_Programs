import os

port = ["Chevrolet Tracker - R$ 120 /dia",
       "Chevrolet Onix - R$ 90 /dia",
       "Chevrolet Spin - R$ 150 /dia",
       "Hyundai HB20 - R$ 85 /dia",
       "Hyundai Tucson - R$ 120 /dia",
       "Fiat Uno - R$ 60 /dia",
       "Fiat Mobi - R$ 70 /dia",
       "Fiat Pulse - R$ 130 /dia"]

nome = ["Chevrolet Tracker",
       "Chevrolet Onix",
       "Chevrolet Spin",
       "Hyundai HB20",
       "Hyundai Tucson",
       "Fiat Uno",
       "Fiat Mobi",
       "Fiat Pulse"]

preco = [120,90,150,85,120,60,70,130]

list_car_alug = []
list_car_nome = []
while True:
    os.system("cls") or None
    print("=--------------------------------=")
    print("Bem vindo à locadora de carros!")
    print("=--------------------------------=\n")

    print("O que você deseja fazer?")
    print("0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro")
    choice = int(input())
    
    if choice == 0:
        os.system("cls") or None
        print("Carros disponíveis para aluguel:")
        print("-------------------------------------")
        for i in range(len(port)):
            print("[{}]  {}".format(i,port[i]))
        print("-------------------------------------")
        print("\n==============================")
        print("0 - Continuar || 1 - Sair")
        comand = int(input())
        if comand == 1:
            os.system("cls") or None
            print("Até logo!")
            break
    elif choice == 1:
        os.system("cls") or None
        print("Carros disponíveis para aluguel:")
        print("-------------------------------------")
        for i in range(len(port)):
            print("[{}]  {}".format(i,port[i]))
        print("-------------------------------------")
        print("")
        print("==============================")
        print("Escolha o código do carro:")
        car_n = int(input())
        print("Por quantos dias você deseja alugar:")
        dias = int(input())
        
        os.system("cls") or None
        print("Você escolheu {} por {} dias.".format(nome[car_n],dias))
        print("O aluguel custará R$ {}".format(preco[car_n] * dias))
        print("\n==============================")
        print("Deseja alugar?")
        print("0 - Sim || 1 - Não")
        alug_n = int(input())
        
        if alug_n == 0:
            os.system("cls") or None
            list_car_alug.append(port[car_n])
            list_car_nome.append(nome[car_n])
            print("Parabéns! Você alugou {}.".format(nome[car_n]))
            port.remove(port[car_n])
            nome.remove(nome[car_n])
            print("")
            print("==========================")
            print("0 - Continuar || 1 - Sair")
            comand = int(input())
            if comand == 1:
                print("Até logo!")
                break
            
        
        elif alug_n == 1:
            os.system("cls") or None
            print("O que você deseja?")
            print("0 - Continuar || 1 - Sair")
            comand = int(input())
            if comand == 1:
                print("Até logo!")
                break
    elif choice == 2:
        os.system("cls") or None
        print("Carros alugados.")
        print("-------------------------------------")
        for i in range(len(list_car_alug)):
            print("[{}]  {}".format(i,list_car_alug[i]))
        print("-------------------------------------\n")
        print("Informe o códido do carro que você quer devolver: ")
        car_dev = int(input())
        if car_dev > len(list_car_alug):
            os.system("cls") or None
            print("XX >>> ERROR !!! <<< XX")
            print("Você informou um número incorreto!")
            print("")
            print("0 - Continuar || 1 - Sair")
            comand = int(input())
            if comand == 1:
                print("Até logo!")
                break
        os.system("cls") or None
        print("Obrigado por devolver o {}.".format(list_car_nome[car_dev]))
        port.append(list_car_alug[car_dev])
        list_car_alug.remove(list_car_alug[car_dev])
        print("")
        print("0 - Continuar || 1 - Sair")
        comand = int(input())
        if comand == 1:
            os.system("cls") or None
            print("Até logo!")
            break