mensagem = """
====================================
           Seja bem vindo!
====================================

Por gentiliza, escolha uma operação:

[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair

=====================================
"""

saldo = 0
qtd_saques = 0
extrato = ""
limite_valor_saque = 500
limite__qtd_saques = 3

while True:

    op = input(mensagem)

    if op == 'q':
        break

    if op.lower() == 'd':
        valor_deposito = float(input("\nInforme o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Depóstio realizado com sucesso.")
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("Depósito não realizado. Valor não permitido.")
       
    elif op.lower() == 's':
        valor_saque =  float(input("\nInforme o valor de saque: "))

        if valor_saque > 0 and valor_saque < limite_valor_saque:
            if valor_saque < saldo :
                if qtd_saques < limite__qtd_saques:
                    saldo -= valor_saque
                    print("\nSaque realizado com sucesso.\n")
                    qtd_saques += 1
                    extrato += f"Saque: R${valor_deposito:.2f}\n"
                else:
                    print("Saque não permitido. Limite de saques diário excedido.")
            else:
                print("Saque não realizado. Saldo insuficiente.")

        else:
            print("Saque não realizado. Valor não permitido.")

    elif op.lower() == 'e':        
        print("\n==================EXTRATO=====================\n")
        print("Nenhuma operação realizada" if extrato == '' else extrato)
        print("\n----------------------------------")
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n==============================================")



