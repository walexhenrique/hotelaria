from pessoa import Cliente, Funcionario
from quarto import QuartoLuxo, QuartoCasal, QuartoSimples, QuartoDuplo
from log import LogMixin
import random


class Hotel(LogMixin):
    """
    Classe responsável pelo gerenciamento dos clientes e o Hotel em si.

    atributos:
    clientes (list): Lista de objetos do tipo Cliente.
    quartos (dict): dicionário de listas de objetos do tipo Quarto.
    funcionarios (list): Lista de objetos do tipo Funcionário.
    """

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

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        """
        Método para adicionar um funcinário ao sistema do hotel.
        :param funcionario: Funcionário a ser adicionado a serviço de quartos.
        :type funcionario: Funcionario

        :return: None
        :rtype: None
        """
        self.funcionarios.append(funcionario)
        self.log_info(f'Adicionado funcionário com sucesso')

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        """
        Método para adicionar um cliente ao sistema do hotel.
        :param cliente: Cliente a ser adicionado ao sistema.
        :type cliente: Cliente

        :return: None
        :rtype: None
        """

        if not isinstance(cliente, Cliente):
            self.log_erro('Tentativa de cadastrar um objeto que não é Cliente')
            print('Não foi possível cadastrar esse cliente')
            return

        if cliente in self.clientes:
            print('Cliente já está cadastrado')
            return

        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} cadastrado com sucesso')
        self.log_info(f'Cliente - {cliente.nome} cadastrado com sucesso')

    def autenticar(self, cliente: Cliente) -> bool:
        """
        Método responsável por autenticar o cliente antes de realizar a ocupação/reserva do quarto.
        :param cliente: Cliente a ser autenticado no sistema do hotel.
        :type cliente: Cliente

        :return: Retorna True caso o Cliente esteja cadastrado no sistema do hotel e False caso não esteja cadastrado.
        :rtype: bool
        """
        if not isinstance(cliente, Cliente):
            self.log_erro(f'Tentativa de login por objeto diferente de cliente')
            return False

        if not cliente in self.clientes:
            self.cadastrar_cliente(cliente)
            print(f'Foi preciso cadastrar o {cliente.nome} no hotel antes de autenticar')

        self.log_info(f'Cliente - {cliente.nome} autenticado com sucesso')
        return True

    def encontrar_quarto_disponivel(self, data_inicial: str, data_final: str, tipo_quarto: str,
                                    cliente: Cliente) -> None:
        """
        Método responsável em encontrar quarto disponível(caso possível) de acordo com a preferência e data do cliente.
        :param data_inicial: Data do primeiro dia de reserva do quarto no hotel.
        :type data_inicial: str
        :param data_final: Data do último dia de reserva do quarto no hotel.
        :type data_final: str
        :param tipo_quarto: A escolha de quarto das quais são possíveis(luxo, casal, simples, duplo).
        :type tipo_quarto: str
        :param cliente: O cliente que está realizando o pedido de reserva.
        :type cliente: Cliente


        :raise TypeError: Se o 'cliente' não for um objeto da classe Cliente.
        :raise KeyError: Se o 'tipo' de quarto requisitado não existir no hotel.
        :raise ValueError: Ocorrer algum outro erro não esperado.

        :return: None
        :rtype: None
        """
        if not isinstance(cliente, Cliente):
            raise TypeError('Utilize um objeto da classe cliente')

        try:
            # Pega um funcionário aleatório para ser responsável por esse quarto caso alugado
            funcionario = self.funcionarios[random.randint(0, len(self.funcionarios) - 1)]
            for quarto in self.quartos[tipo_quarto]:

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
