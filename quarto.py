from datetime import datetime
from pessoa import Cliente, Funcionario
from agendamento import Agendamento


class Quarto:
    """
    Classe (abstrata) responsável pela administração do quarto, sendo possível reservar, fazer manutenção(repor os itens no frigobar).

    atributos:
    numero (int): Número de indentificação do quarto.
    agendamentos (list): É uma lista de agendamentos(objetos) do quarto.
    itens (dict): dicionário de itens disponíveis para consumo do cliente.
    """

    def __init__(self, numero: int = 100):
        self.numero = numero
        self.agendamentos = []
        self.itens = {
            'refrigerante': {
                'valor': 5,
                'quantidade': 10
            },
            'cerveja': {
                'valor': 3.45,
                'quantidade': 20
            }
        }

    def fazer_manutencao(self) -> None:
        """
        Método responsável por repor os itens ao quarto para o novo hospéde.
        :return: None
        :rtype: None
        """
        self.itens = {
            'refrigerante': {
                'valor': 5,
                'quantidade': 10
            },
            'cerveja': {
                'valor': 3.45,
                'quantidade': 20
            }
        }
        print('Produtos reabastecidos')

    def _data_disponivel(self, data_inicial: datetime, data_final: datetime) -> bool:
        """
        Método privado responsável por realizar a verificação de disponibilidade de determinada data a ser reservada.
        :param data_inicial: Data do primeiro dia de reserva do quarto.
        :type data_inicial: datetime
        :param data_final: Data do último dia de reserva do quarto.
        :type data_final: datetime

        :return: Retorna True caso seja possível realizar a reserva do quarto na data prevista.
        :rtype: bool
        """
        if data_inicial >= data_final:
            return False

        for agendamento in self.agendamentos:
            if agendamento.data_inicial == data_inicial or agendamento.data_final == data_final:
                return False
            if data_inicial > agendamento.data_inicial and data_final < agendamento.data_final:
                return False

        return True

    def reservar(self, data_inicial: str, data_final: str, cliente: Cliente, funcionario: Funcionario = None) -> bool:
        """
        Método responsável por realizar a reserva do quarto na data prevista do cliente.
        :param data_inicial: Data do primeiro dia de reserva do quarto.
        :type data_inicial: str
        :param data_final: Data do último dia de reserva do quarto.
        :type data_final: str
        :param cliente: Cliente que deseja realizar a reserva do quarto.
        :type cliente: Cliente
        :param funcionario: Funcionário responsável pelo quarto ao se concretizar a reserva.
        :type funcionario: Funcionario

        :raises TypeError: Tentar inserir datas inválidas(diferente de uma str)
        :raise ValueError: Tentar inserir datas inválidas(Não seguir o padrão dia/mes/ano)

        :return: Caso a reserva seja possível retornará True, do contrário, False.
        :rtype: bool

        """
        if not isinstance(data_inicial, str):
            raise TypeError('"data_inicial" precisa ser (str)')

        if not isinstance(data_final, str):
            raise TypeError('"data_final" precisa ser (str)')

        try:
            data_inicial_convertido = datetime.strptime(data_inicial, '%d/%m/%Y').date()
            data_final_convertido = datetime.strptime(data_final, '%d/%m/%Y').date()
            if self._data_disponivel(data_inicial_convertido, data_final_convertido):
                self.agendamentos.append(
                    Agendamento(data_inicial_convertido, data_final_convertido, cliente, funcionario)
                )
                cliente.quartos_reservados.append(self)

                print(
                    f'Agendamento para o dia inicial: {data_inicial} com encerramento para o dia: {data_final} realizada com sucesso')
                return True
        except Exception as e:
            raise ValueError('Valor inválido para data')
        return False


class QuartoSimples(Quarto):
    """
    Classe responsável pela administração do quarto simples, sendo possível reservar, fazer manutenção(repor os itens no frigobar).

    atributos:
    numero (int): Número de indentificação do quarto.
    agendamentos (list): É uma lista de dicionários representando cada reserva, cliente e funcionários associados a mesma.
    itens (dict): dicionário de itens disponíveis para consumo do cliente.
    valor_diaria (float): Custo da diária do quarto
    """
    valor_diaria = 100


class QuartoDuplo(Quarto):
    """
    Classe responsável pela administração do quarto duplo, sendo possível reservar, fazer manutenção(repor os itens no frigobar).

    atributos:
    numero (int): Número de indentificação do quarto.
    agendamentos (list): É uma lista de dicionários representando cada reserva, cliente e funcionários associados a mesma.
    itens (dict): dicionário de itens disponíveis para consumo do cliente.
    valor_diaria (float): Custo da diária do quarto
    """
    valor_diaria = 150


class QuartoCasal(Quarto):
    """
    Classe responsável pela administração do quarto casal, sendo possível reservar, fazer manutenção(repor os itens no frigobar).

    atributos:
    numero (int): Número de indentificação do quarto.
    agendamentos (list): É uma lista de dicionários representando cada reserva, cliente e funcionários associados a mesma.
    itens (dict): dicionário de itens disponíveis para consumo do cliente.
    valor_diaria (float): Custo da diária do quarto
    """
    valor_diaria = 200


class QuartoLuxo(Quarto):
    """
    Classe responsável pela administração do quarto luxo, sendo possível reservar, fazer manutenção(repor os itens no frigobar).

    atributos:
    numero (int): Número de indentificação do quarto.
    agendamentos (list): É uma lista de dicionários representando cada reserva, cliente e funcionários associados a mesma.
    itens (dict): dicionário de itens disponíveis para consumo do cliente.
    valor_diaria (float): Custo da diária do quarto
    """
    valor_diaria = 300
