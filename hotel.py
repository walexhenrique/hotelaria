from pessoa import Cliente, Funcionario
from quarto import QuartoLuxo, QuartoCasal, QuartoSimples, QuartoDuplo
from log import LogMixin
import random


class Hotel(LogMixin):
    def __init__(self):
        self.clientes = [
            Cliente('Raimundo', '459445421', 18),
            Cliente('Breno', '5449879545', 65)
        ]
        self.quartos = {
            'luxo': [QuartoLuxo(1), QuartoLuxo(2)],
            'casal': [QuartoCasal(3), QuartoCasal(4)],
            'simples': [QuartoSimples(5), QuartoSimples(6)],
            'duplo': [QuartoDuplo(7), QuartoDuplo(8)]
        }
        self.funcionarios = [
            Funcionario('Jorge', '24574522', 25),
            Funcionario('Mauro', '24421582', 45)
        ]

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.log_info(f'Adicionado funcionário com sucesso')

    def adicionar_quarto(self, tipo, quarto):
        self.quartos[tipo].append(quarto)
        self.log_info(f'Adicionado quarto do tipo({tipo}) com sucesso')

    def cadastrar_cliente(self, cliente):
        if cliente in self.clientes:
            print('Cliente já está cadastrado')
            return

        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} cadastrado com sucesso')
        self.log_info(f'Cliente - {cliente.nome} cadastrado com sucesso')

    def autenticar(self, cliente):
        if not isinstance(cliente, Cliente):
            self.log_erro(f'Tentativa de login por objeto diferente de cliente')
            return False

        if not cliente in self.clientes:
            self.cadastrar_cliente(cliente)
            print(f'Foi preciso cadastrar o {cliente.nome} no hotel antes de autenticar')

        self.log_info(f'Cliente - {cliente.nome} autenticado com sucesso')
        return True

    def encontrar_quarto_disponivel(self, data_inicial, data_final, tipo_quarto, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError('Utilize um objeto da classe cliente')

        try:
            funcionario = self.funcionarios[random.randint(0, len(self.funcionarios) - 1)]
            for quarto in self.quartos[tipo_quarto]:
                # randomizar funcionario dps

                if quarto.reservar(data_inicial=data_inicial, data_final=data_final, cliente=cliente,
                                   funcionario=funcionario):
                    print(f'Foi realizada a reserva do quarto ({tipo_quarto}) com sucesso!')

                    self.log_info(
                        f'{cliente.nome} realizou a reserva com sucesso para a data de {data_inicial} e {data_final}\n'
                        f'para o quarto({tipo_quarto}) de numero: {quarto.numero}, funcionario: {funcionario.nome}')
                    return
        except KeyError:
            self.log_erro('Quarto procurado nao existe')
            raise KeyError('Tipo de quarto nao existe')
        except Exception as e:
            self.log_erro(f'Ocorreu um erro {e}')
            raise ValueError('Erro ao encontrar um quarto')

        print(f'Não encontramos nenhum quarto tipo({tipo_quarto}) para esse intervalo de data :/')
