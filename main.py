menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair do Programa

=> """

saldo= 0 
limite = 500
extrato = ""
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Você entrou na opção depósito")
        valor_deposito = float(input("Digite o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += (f"Valor do deposíto é: R${saldo:.2f}\n")
        else:
            print("Operação inválida")



    elif opcao == "s":
        print("Você entrou na opção Saque")
        numero_saques = 0
        valor_saque = float(input("Digite o valor do saque: "))

        # Condições

        excedeu_limite = valor_saque > limite
        excedeu_saldo = valor_saque > saldo
        excedeu_saques = numero_saques >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print("Operação inválida! Excedeu saldo")

        elif excedeu_saques:
            print("Operação inválida! Excedeu saques")

        elif excedeu_limite:
            print("Operação inválida! Excedeu limite")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += (f"Saque: R$ {valor_saque:.2f}\n")
            numero_saques += 1

        else:
            print("Operação falhou, o valor informado não é válido")

    elif opcao == "e":
        print("Você entrou na opção Extrato\n")
        print("\n =============EXTRATO===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")


    elif opcao == "q":
        break

    else:
        print("Operação inválida! Selecione a opção desejada")
        