def deposit(saldo, quantidade):
    if quantidade > 0:
        saldo += quantidade
        print(f"Depósito = R${quantidade:.2f}")
    else:
        print("Depósito precisa ser positivo")
    return saldo

def withdraw(saldo, quantidade):
    if quantidade > 0 and quantidade <= 500:
        if saldo >= quantidade:
            saldo -= quantidade
            print(f"Saque: R${quantidade:.2f}")
        else:
            print("Saldo insuficiente")
    else:
        print("Seu limite para saques é R$500")
    return saldo

def main():
    saldo = 500
    while True:
        print("Caixa Eletrônico")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            quant = float(input("Digite o valor do depósito: "))
            saldo = deposit(saldo, quant)
        elif choice == '2':
            quant = float(input("Digite o valor do saque: "))
            saldo = withdraw(saldo, quant)
        elif choice == '3':
            print(f"Seu saldo é igual à R$:{saldo:.2f}")
        elif choice == '4':
            print("Obrigado por usar o caixa eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
