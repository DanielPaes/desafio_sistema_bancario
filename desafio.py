mensagem = """
====================================
           Seja bem vindo!
------------------------------------
Por gentiliza, escolha uma operação:

[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair
------------------------------------
"""

# Declaração e inicialização de variáveis
saldo = 0
qtd_saques = 0
extrato = ""
limite_valor_saque = 500
limite__qtd_saques = 3

while True:

    # Leitura da operação que será executada.
    op = input(mensagem)

    # Sai do do programa
    if op.lower() == 'q':
        break

    # Operação de depósito
    elif op.lower() == 'd':
        try:
            valor_deposito = float(input("\nInforme o valor do depósito: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                print("\nDepóstio realizado com sucesso.")
                extrato += f"Depósito: R${valor_deposito:.2f}\n"
            else:
                print("\nDepósito não realizado. Valor não permitido.")
        except:
            print("\nValor inválido. Tente novamente.")
       
    # Operação de saque
    elif op.lower() == 's':
        try:
            valor_saque =  float(input("\nInforme o valor de saque: "))

            if valor_saque > 0 and valor_saque < limite_valor_saque:
                if valor_saque < saldo :
                    if qtd_saques < limite__qtd_saques:
                        saldo -= valor_saque
                        print("\nSaque realizado com sucesso.\n")
                        qtd_saques += 1
                        extrato += f"Saque: R${valor_deposito:.2f}\n"
                    else:
                        print("\nSaque não permitido. Limite de saques diário excedido.")
                else:
                    print("\nSaque não realizado. Saldo insuficiente.")
            else:
                print("\nValor inválido. Saque não realizado.")
        except:
            print("\nValor inválido. Tente novamente.")

    # Impressão do extrato
    elif op.lower() == 'e':        
        print("\n\n==============EXTRATO===============\n")
        print("Nenhuma operação realizada\n" if extrato == '' else extrato)
        print("----------------------------------")
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n====================================\n")

    # Operação selecionada inválida
    else:
        print("\nOperação inválida. Tente novamente.")

