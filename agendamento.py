from datetime import datetime
from pessoa import Cliente, Funcionario

class Agendamento:
    """
    Classe responsável por organizar cada agendamento de acordo com a data e cliente
    data_inicial (datetime.data): Data do primeiro dia de reserva do quarto.
    data_final (datetime.data): Data do último dia de reserva do quarto.
    cliente (Cliente): Cliente que realizou a reserva do quarto.
    funcionario (Funcionario): Funcionário responsável pelo quarto nesta reserva.
    """
    def __init__(self, data_inicial: datetime.date, data_final: datetime.date, cliente: Cliente, funcionario: Funcionario):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.cliente = cliente
        self.funcionario = funcionario

