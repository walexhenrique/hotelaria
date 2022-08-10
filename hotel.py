from pessoa import Cliente


class Hotel:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        # FALTA OS SERVIÇOS

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def autenticar(self, cliente):
        if not isinstance(cliente, Cliente):
            return False

        if not cliente in self.clientes:
            self.cadastrar_cliente(cliente)
            print(f'Foi preciso cadastrar o {cliente.nome} no hotel antes de autenticar')

        return True

    def servicos(self, cliente, servico):
        pass