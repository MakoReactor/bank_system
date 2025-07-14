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
    if valor <= 0:
        return False
    else:
        saldo += valor
        extrato += f"Depósito R${valor:28.2f}+\n"
        return saldo, extrato


def sacar(
    *,
    saldo,
    valor,
    extrato,
    valor_limite_saque,
    limite_qntde_saque,
    qntde_saques_efetuada,
):
    if valor <= 0:
        print("Valor inválido para o saque.")
        return False

    if qntde_saques_efetuada == limite_qntde_saque:
        print("Qnatidade de Saques diários excedida.")
        return False

    if valor > valor_limite_saque:
        print("Valor excede o valor permitido por saque!")
        return False

    if valor > saldo:
        print("Saldo insuficiente!")
        return False

    saldo = saldo - valor
    extrato = extrato + f"Saque R${valor:31.2f}-\n"

    return saldo, extrato


# Extrato
def exibir_extrato(saldo, *, extrato):
    print(f"{'Extrato'.center(40, '=')}")
    if extrato:
        print(extrato)
        print(f"\nSaldo R${saldo:31.2f}")
        print(f"{'='.center(40, '=')}")
    else:
        print("Sem Trasações financeiras")
        print(f"\nSaldo R${saldo:31.2f}")
        print(f"{'='.center(40, '=')}")


def criar_usuario(cpf, usuarios):
    for user in usuarios:
        if user.get(cpf):
            print(f"Usuário com CPF: {cpf} já existe")
            return False
    else:
        cpf = cpf
        nome = input("Digite o nome do usuário: ").strip()
        data_nascimento = input("Data nascimento 'DD/MM/AAAA': ").strip()
        logradouro = input(
            "Digite o seu endereço: ex: 'Logradouro, nº - bairro - cidade/sigla estado': "
        )

        usuario = {
            cpf: {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "logradouro": logradouro,
                "usuario_conta": [],
            }
        }
        usuarios.append(usuario)
        return usuarios


def criar_conta(cpf, agencia, numero_conta, contas, usuarios):
    for user in usuarios:
        if user.get(cpf):
            usuario = user[cpf]["nome"]
            conta = numero_conta + 1

            conta = {conta: {"agencia": agencia, "cpf": cpf, "nome": usuario}}

            contas.append(conta)
            user[cpf]["usuario_conta"].append(conta)


def main():
    # iniciando variáveis
    saldo = 0.0
    extrato = ""
    qntde_saques_efetuada = 0
    usuarios = []
    contas = []
    numero_conta = 0

    # Constantes
    VALOR_LIMITE_SAQUE = 500.0
    QNTDE_SAQUE_DIARIA = 3
    AGENCIA = "0001"

    while True:
        print("usuarios", usuarios)

        op = input(f"{menu()} opção: ")

        # Depositar
        if int(op) == 1 or op == "1":
            valor = float(input("Informe o valor do Depósito: ").strip())

            if depositar(saldo, valor, extrato):
                saldo, extrato = depositar(saldo, valor, extrato)
            else:
                print(f"Valor R${valor:.2f} inválido para depósito!")

        # Sacar
        elif op == 2 or op == "2":
            valor = float(input("Informe o valor do Saque: ").strip())
            if sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                valor_limite_saque=VALOR_LIMITE_SAQUE,
                limite_qntde_saque=QNTDE_SAQUE_DIARIA,
                qntde_saques_efetuada=qntde_saques_efetuada,
            ):
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    valor_limite_saque=VALOR_LIMITE_SAQUE,
                    limite_qntde_saque=QNTDE_SAQUE_DIARIA,
                    qntde_saques_efetuada=qntde_saques_efetuada,
                )
                qntde_saques_efetuada += 1

            else:
                print("Saque 'NÃO' efetuado!")

        # Extrato
        elif op == 3 or op == "3":
            exibir_extrato(saldo, extrato=extrato)

        # Criar usuário
        elif op == 4 or op == "4":
            cpf = input("Digite o seu CPF, apenas números: ")
            criar_usuario(cpf, usuarios)

        # Criar conta
        elif op == 4 or op == "4":
            # Fazer / finalizar a criação de conta
            return True

        # Sair
        elif int(op) == 6 or op == "6":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida, tente novamente\n")


main()
