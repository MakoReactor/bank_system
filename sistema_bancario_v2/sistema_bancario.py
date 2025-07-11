def menu():
    inicio = f"""
    {"MENU".center(40, "=")}
    1 - para depositar
    2 - para sacar
    3 - para extrato
    4 - criar usuário
    5 - criar conta corrente
    6 - sair

    {"=".center(40, "=")}
    
    """
    return inicio


def depositar(saldo, valor, extrato):
    return saldo, extrato


def exibir_extrato(extrato):
    return extrato


def main():
    saldo = 0.0

    while True:
        op = input(f"{menu()} => ")

        if int(op) == 1 or op == "1":
            valor = float(input("Informe o valor do Depósito: ").strip())
            # parei aqui
            depositar(saldo, valor)
        elif int(op) == 6 or op == "6":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida, tente novamente\n")


main()
