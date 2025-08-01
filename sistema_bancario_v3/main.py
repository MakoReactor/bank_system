from sistema_bancario import (
    PessoaFisica, ContaCorrente,
    Saque, Deposito
)
def menu():
    inicio = f"""
{"MENU".center(40, "=")}
1 - depositar
2 - sacar
3 - extrato
4 - cadastrar cliente
5 - criar conta corrente
6 - listar contas
7 - listar clientes
9 - sair

{"=".center(40, "=")}
    
"""
    return inicio


# pesquisar pessoa
def filtrar_pessoa(cpf, clientes):
    
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None
    
def cadastro_cliente(clientes):
    cpf = input("CPF (somente números): ")

    cliente = filtrar_pessoa(cpf, clientes)
            
    if cliente:
        print("xxx Cliente já existe! xxx")
        return

    nome = input("Nome: ")
    data_nascimento = input("Data nascimento (AAAA-M-D)")
    endereco = input("Endereco (Rua, nº - Bairro, Cidade/Estado)")
    p = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(p)
    print("\n=== Cliente criado com Sucesso! ===")



def cria_conta(clientes, contas, num_conta):
    cpf = input("Digite o CPF: ")

    cliente = filtrar_pessoa(cpf=cpf, clientes=clientes)    
    
    if cliente:
        conta = ContaCorrente(numero=num_conta, cliente=cliente)
        contas.append(conta)
        cliente.contas.append(conta)
        print(" === Conta criada com sucesso! ===")
    else:
        print("xxx Cliente não existe, falha ao criar conta. xxx")
    

# Listar Contas
def listar_contas(contas):
    print("=" * 40)
    for conta in contas:
        print(conta)
    print("=" * 40)

def listar_pessoas(clientes):
    print("=" * 40)
    for cliente in clientes:
        print(cliente)
        for conta in cliente.contas:
            print(f"{conta}")
        print("-" * 40)
    print("=" * 40)

def depositar(clientes):
    cpf = input("Qual o CPF da conta: ")
    num_conta = int(input("Digite o número da Conta: "))
    cliente = filtrar_pessoa(cpf=cpf, clientes=clientes)

    if cliente:
        for conta in cliente.contas:
            if num_conta == conta.numero:
                print("Conta encontrada!")
                valor = float(input("Valor depósito: "))
                transacao = Deposito(valor)
                cliente.realizar_transacao(conta, transacao)
                return

    print("xxx Cliente ou Conta não encontrado! xxx")
            
                
    
def sacar(clientes):
    cpf = input("Qual o CPF da conta: ")
    num_conta = int(input("Digite o número da Conta: "))
    cliente = filtrar_pessoa(cpf=cpf, clientes=clientes)

    if cliente:
        for conta in cliente.contas:
            if num_conta == conta.numero:
                print("Conta encontrada!")
                valor = float(input("Valor do Saque: "))
                transacao = Saque(valor)
                cliente.realizar_transacao(conta, transacao)
                return

    print("xxx Cliente ou Conta não encontrado! xxx")
               
    
def extrato(clientes):
    
    cpf = input("Qual o CPF da conta: ")
    num_conta = int(input("Digite o número da Conta: "))
    cliente = filtrar_pessoa(cpf=cpf, clientes=clientes)

    if cliente:
               
        cc = [conta for conta in cliente.contas if conta.numero == num_conta]
        cc = cc[0]
        
        saques_realizados = len([transacao for transacao in cc.historico.transacoes if transacao["tipo"] == Saque.__name__])
        
        print(f"\n\n{'Extrato'.center(40, "=")}")
        print(f"Cliente: {cliente.nome}\nSaques Restantes: {cc.limite_saques - saques_realizados}\n\n")
        
        for transacao in cc.historico.transacoes:
            print(f"{transacao['tipo']} R$ {transacao['valor']:15.2f}")
    print(f"\n\nSaldo: R$ {cc.saldo:15.2f}")
        
        
    print("=" * 40)

     

# Início do Programa
def main():
    clientes = []
    contas = []

    while True:

        op = input(f"{menu()} opção: ")

        if op == "1":
            print("Deposito")
            depositar(clientes)

        elif op =="2":
            print("Saque")
            sacar(clientes)

        elif op == "3":
            extrato(clientes)

        elif op == "4":
            print("Cadastro de Cliente\n")
            cadastro_cliente(clientes)   

        elif op == '5':
            print("Criar Conta Corrente\n")
            num_conta = len(contas) + 1
            cria_conta(clientes, contas, num_conta)

        elif op == "6":
            print("Listar Contas")
            listar_contas(contas)

        elif op == '7':
            print("Listar Clientes")
            listar_pessoas(clientes=clientes)

        elif op == "9":
            print("--- Obrigado por usar os nossos serviços! ---")
            break
        else:
            print("*** Opção inválida, tente novamente! ***")



if __name__ == "__main__":
    main()