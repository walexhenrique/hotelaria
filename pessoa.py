from servicos import Servicos
from log import LogMixin


class Pessoa:
    """
    Classe (abstrata) responsável por generalizar as classes Funcionários e Clientes.

    atributos:
    nome (str): Nome da pessoa.
    cpf (str): Cpf para identificação da pessoa.
    idade (int): Idade da pessoa.
    """
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self._cpf = cpf
        self.idade = idade

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        self._cpf = valor


class Funcionario(Pessoa):
    """
    Classe responsável por gerenciar funcionário.

    atributos:
    nome (str): Nome da pessoa.
    cpf (str): Cpf para identificação da pessoa.
    idade (int): Idade da pessoa.
    trabalhando (bool): Status relacionado a disponibilidade serviço do mesmo.
    """
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.trabalhando = True

    def parar_de_trabalhar(self) -> None:
        """
        Método responsável por desabilitar o trabalho do funcionário.
        :return: None
        :rtype: None
        """
        self.trabalhando = False

    def voltar_a_trabalhar(self) -> None:
        """
        Método responsável por reativar o trabalho do funcionário.
        :return: None
        :rtype: None
        """
        self.trabalhando = True


class Cliente(Pessoa, LogMixin):
    """
    Classe responsável por gerenciar o cliente.

    atributos:
    nome (str): Nome da pessoa.
    cpf (str): Cpf para identificação da pessoa.
    idade (int): Idade da pessoa.
    quartos_reservados (list): Lista de todos os quartos reservados pelo cliente até o momento.
    consumidos (list): Lista de itens consumidos no quarto pelo cliente para posterior cobrança.
    servicos (list): Lista de serviços solicitados pelo cliente para posterior cobrança.
    """
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)

        self.quartos_reservados = []
        self.consumidos = []
        self.servicos = []

    def pagar_diaria(self) -> None:
        """
        Método responsável por pagar a(s) diária(s) de todos os quartos reservados.

        :return: None
        :rtype: None
        """
        total = sum([x.valor_diaria for x in self.quartos_reservados])
        if total > 0:
            print(f'Foi realizado o pagamento de R$ {total} da(s) diária(s)')
            self.log_info(f'Cliente - {self.nome} pagou um total de R${total} de diaria')
            return

        print('Você não realizou nenhuma reserva')

    def consumir(self, quarto_id: int, item: str) -> None:
        """
        Método responsável por consumir item do frigobar do quarto.
        :param quarto_id: Id na lista do quarto reservado pelo cliente.
        :type quarto_id: int
        :param item: Nome do item a ser consumido do frigobar.
        :type item: str

        :return: None
        :rtype: None
        """
        if quarto_id >= len(self.quartos_reservados):
            print('Não encontramos esse quarto')
            self.log_erro(f'Cliente - {self.nome} tentou acessar um quarto inexistente ')
            return

        if item in self.quartos_reservados[quarto_id].itens:
            if self.quartos_reservados[quarto_id].itens[item]['quantidade'] >= 1:
                self.quartos_reservados[quarto_id].itens[item]['quantidade'] -= 1
                print(f'Foi consumido 1 {item} com sucesso')
                self.log_info(
                    f'Cliente - {self.nome} consumiu um {item} de R${self.quartos_reservados[quarto_id].itens[item]["valor"]} ')
                return
        print(f'Não foi possível consumir {item}')

    def solicitar_servico(self, servico: Servicos) -> None:
        """
        Método responsável por solicitar serviço de hotel.
        :param servico: Serviço a ser solicitado ao hotel dos quais são: limpar_quarto, passar_roupa, lavar_roupa.
        :type servico: Servicos

        :raise TypeError: Caso o serviço solicitado não seja um Enum(Servicos).

        :return: None
        :rtype: None
        """
        if not isinstance(servico, Servicos):
            self.log_erro(f'Cliente {self.nome} solicitou um cliente que nao existe')
            raise TypeError('Servico solicitado não é um Enum')

        self.log_info(f'Cliente - {self.nome} fez um servico pelo valor de R${servico.value}')
        print(f'Serviço realizado com o custo de R${servico.value}')

    def desocupar_quarto(self, quarto_id: int) -> None:
        """
        Método responsável em desocupar um quarto após a estadia.
        :param quarto_id: Id do quarto que vai desocupar.
        :type quarto_id: int

        :return: None
        :rtype: None
        """
        if quarto_id >= len(self.quartos_reservados):
            print('Não foi possivel desocupar esse quarto')
            return

        self.log_info(f'Cliente - {self.nome} desocupou o quarto de num {quarto_id} dele')
        print(f'{self.nome} desocupou um quarto')
        self.quartos_reservados.pop(quarto_id).fazer_manutencao()
