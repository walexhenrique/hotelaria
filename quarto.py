from datetime import datetime


class Quarto:
    def __init__(self, numero=100):
        self.numero = numero
        self.agendamentos = []  # { "data_inicial": "12/04/2022", "data_final":"15/04/2022" }
        # self.funcionando = True
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

    def fazer_manutencao(self):
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

        if data_inicial >= data_final:
            return False

        for agendamento in self.agendamentos:
            if agendamento['data_inicial'] == data_inicial or agendamento['data_final'] == data_final:
                return False
            if data_inicial > agendamento['data_inicial'] and data_final < agendamento['data_final']:
                return False

        return True

    def reservar(self, data_inicial: str, data_final: str, cliente, funcionario=None) -> bool:

        if not isinstance(data_inicial, str):
            raise TypeError('"data_inicial" precisa ser (str)')

        if not isinstance(data_final, str):
            raise TypeError('"data_final" precisa ser (str)')

        try:
            data_inicial_convertido = datetime.strptime(data_inicial, '%d/%m/%Y').date()
            data_final_convertido = datetime.strptime(data_final, '%d/%m/%Y').date()
            if self._data_disponivel(data_inicial_convertido, data_final_convertido):
                self.agendamentos.append(
                    {'data_inicial': data_inicial_convertido, 'data_final': data_final_convertido, 'cliente': cliente,
                     'funcionario': funcionario}
                )
                cliente.quartos_reservados.append(self)

                print(
                    f'Agendamento para o dia inicial: {data_inicial} com encerramento para o dia: {data_final} realizada com sucesso')
                return True
        except Exception as e:
            raise ValueError('Valor inválido para data')
        return False


class QuartoSimples(Quarto):
    valor_diaria = 100


class QuartoDuplo(Quarto):
    valor_diaria = 150


class QuartoCasal(Quarto):
    valor_diaria = 200


class QuartoLuxo(Quarto):
    valor_diaria = 300
