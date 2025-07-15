def menu():
    inicio = f"""
{"MENU".center(40, "=")}
1 - para depositar
2 - para sacar
3 - para extrato
4 - criar usuário
5 - criar conta corrente
6 - listar contas
7 - listar usuários
8 - sair

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
        if cpf in user:
            usuario = user[cpf]["nome"]
            conta = numero_conta

            conta = {conta: {"agencia": agencia, "cpf": cpf, "nome": usuario}}
            contas.append(conta)

            user[cpf]["usuario_conta"].append(conta)
            return True
    
    # Se chegou até aqui, significa que o CPF não foi encontrado
    return False

def listar_contas(contas):
    for i, conta in enumerate(contas, 1):
        num_conta = list(conta.keys())[0]
        dados = conta[num_conta]
        print(f"Nº Conta: {num_conta}")
        for c, v in dados.items():
            print(f"    {c}: {v}")
        print('')

def listar_usuarios(usuarios):
    for i, usuario in enumerate(usuarios, 1):
        cpf = list(usuario.keys())[0]
        dados = usuario[cpf]
        print(f"CPF: {cpf}")
        for c, v in dados.items():
            print(f"    {c}: {v}")
        print('')

def main():
    # iniciando variáveis
    saldo = 0.0
    extrato = ""
    qntde_saques_efetuada = 0
    usuarios = []
    contas = []
    numero_conta = 1

    # Constantes
    VALOR_LIMITE_SAQUE = 500.0
    QNTDE_SAQUE_DIARIA = 3
    AGENCIA = "0001"

    while True:
        
      
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
        elif op == 5 or op == "5":            
            cpf = input("Digite aqui o CPF para abrir a conta: ")
            if criar_conta(cpf, AGENCIA, numero_conta, contas, usuarios):
                numero_conta += 1
                print("Conta criada com sucesso!")
            else:
                print("CPF não encontrado.\nPor favor crie um usuário.")
        # Listar contas
        elif op == 6 or op == '6':
            listar_contas(contas)

        # listar usuários
        elif op == 7 or op == '7':
            listar_usuarios(usuarios)
       
       
        # Sair
        elif int(op) == 8 or op == "8":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida, tente novamente\n")


main()
