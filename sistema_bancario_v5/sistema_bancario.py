from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self):
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__()
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"CPF:{self.cpf}, Nome: {self.nome}, Qntde Contas: {len(self.contas)}"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"  # agência é valor fixo
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        # retorna uma Conta()
        return cls(numero, cliente)

    def sacar(self, valor):
        if valor <= 0:
            print("XXX Valor digitado inválido. XXX")
            return False

        if valor > self._saldo:
            print("XXX Operação falhou! Saldo insuficiente. XXX")
            return False
        
        self._saldo -= valor
        print("@@@ Saque efetuado com sucesso! @@@")
        return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n@@@ Depósito realizado com sucesso! @@@")
        else:
            print("\nXXX A operação falhou! O Valor informado é inválido. XXX")
            return False

        return True

        
class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite=500, limite_transacoes=10):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_transacoes = limite_transacoes

    def sacar(self, valor):
        # busca a quantidade de transações feitas até o momento
        numero_transacoes = len([transacao['tipo'] for transacao in self.historico.transacoes])
        
        if valor > self.limite:
            print("XXX Operação falhou! Valor excede o limite de saque. XXX")
            return False

        if numero_transacoes >= self.limite_transacoes:
            print("XXX Operação falhou! Número máximo de transações excedido. XXX")
            return False
        
        return super().sacar(valor)

    def depositar(self, valor):
        # busca a quantidade de transações feitas até o momento
        numero_transacoes = len([transacao['tipo'] for transacao in self.historico.transacoes])
        if numero_transacoes >= self.limite_transacoes:
            print("XXX Operação falhou! Número máximo de transações excedido. XXX")
            return False
        return super().depositar(valor)


    def __str__(self):
        return f"Agência: {self.agencia}, C/C: {self.numero}, Titular: {self.cliente.nome}"



class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                "valor": transacao.valor,
                'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        fazer_transacao = conta.sacar(self.valor)

        if fazer_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        fazer_transacao = conta.depositar(self.valor)

        if fazer_transacao:
            conta.historico.adicionar_transacao(self)