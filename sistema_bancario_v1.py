from datetime import datetime
menu = ('''
========== MENU ==========

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - SAIR

==========================
''')

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contador_deposito = 0

while True:

    opcao = input(menu)
    data_now = datetime.now()
    data_da_operacao = data_now.strftime("%d/%m/%Y, %H:%M:%S")

    
    if opcao == "1":

        deposito = float(input('Qual valor deseja depositar? R$'))

        if deposito >= 1.00:

            contador_deposito += 1

            saldo += deposito

            extrato += (f"{contador_deposito}° - Deposito ({data_da_operacao})\n") + str(f"R$ {deposito:.2f} Reais\n")
            print(f"O valor de R${deposito:.2f} foi depositado com sucesso!")

        else:
            print("Não foi possivel efetuar essa operação, deposite NOTAS igual ou acima de R$1 real.")

    elif opcao == "2":
        
        saque = float(input("Quanto deseja sacar? R$ "))

        if saldo < 0:
            print("Não é possivel efetuar a operação, saque valores igual ou acima de R$ 1,00 real.")
        
        elif numero_saques > LIMITE_SAQUES - 1:
            print("Não foi possivel efetuar essa operação, limite de saque diário excedido! ")
        
        elif saldo > limite:
            print("Não foi possivel efetuar essa operação, o limite por saque é de R$500,00 reais.")
        
        elif saldo > 0:
            
            saldo -= saque

            numero_saques += 1

            extrato += (f"{numero_saques}° - Saque ({data_da_operacao})\n") + str(f"R$ {saque:.2f} Reais\n")

            print(f"O saque de R${saque:.2f} foi realizado com sucesso!")

        else:
            print("Saldo insuficiente para saque!")

    elif opcao == "3":

        print(f"======EXTRATO DA CONTA======")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")