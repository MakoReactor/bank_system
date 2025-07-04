import os


# Variáveis
saldo = 0.0
limite_saque = 500.00
numero_saques = 0
total_saques = 0.0
total_deposito = 0.0


# constantes
LIMITE_SAQUES = 3
TITULO_MENU = "Menu".center(40, "-")
LINHA_FINAL = "-".center(40, "-")

# Menu
menu = f"""
{TITULO_MENU}
{"Bem Vindo".center(40)}

Escolha uma das opções abaixo:

d - Depósito
s - Saque
e - Extrato
q - Sair

{LINHA_FINAL}
"""

while True:
    os.system("clear")
    op = input(f"{menu} => opção: ")

    if op == "d":
        os.system("clear")
        valor = float(input("Digite o valor do Deposito: "))
        if valor <= 0:
            print("Atenção! Permitido apenas deposito acima de 0 (Zero) Reais!")
            input("Tecle 'ENTER' para continuar!")
            continue
        saldo = saldo + valor
        total_deposito = total_deposito + valor
        print("Depósito realizado com sucesso!")

        # auxiliar de pausa
        input("Tecle 'ENTER' para continuar!")

    elif op == "s":
        os.system("clear")
        valor = float(input("Digite o valor para o saque: "))
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo and valor <= limite_saque:
                if valor == 0:
                    print("Valor Inválido para saque!")
                else:
                    saldo -= valor
                    total_saques += valor
                    numero_saques += 1

                    print("Saque efetuado com sucesso!")
                    print(f"Você possui mais {LIMITE_SAQUES - numero_saques} saques.")
            else:
                print("Limite de Saque ou Saldo insuficiente!")
        else:
            print("Limite de saques excedido")

        # auxiliar de pausa
        input("Tecle 'ENTER' para continuar!")

    elif op == "q":
        print("")
        break

    elif op == "e":
        os.system("clear")
        extrato = f"""
{"Extrato".center(40, "-")}
Olá usuário!

Saques restantes: {LIMITE_SAQUES - numero_saques}

Valor total de Depósitos: +R${total_deposito:10.2f} 
Valor Total de Saques:    -R${total_saques:10.2f}

Saldo:                     R${saldo:10.2f}
{"-".center(40, "-")}
"""
        print(extrato)

        # pausa
        input("Tecle 'ENTER' para continuar!")

    else:
        print("Opção não encontrada, tente novamente!\n")

        # auxiliar de pausa
        input("Tecle 'ENTER' para continuar!")
