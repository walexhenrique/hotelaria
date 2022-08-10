class Pessoa:
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


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)

        self.quartos_reservados = []
        self.consumidos = []
        self.servicos = []

    def pagar_diaria(self):
        total = sum([x.valor_diaria for x in self.quartos_reservados])
        if total > 0:
            print(f'Foi realizado o pagamento de R$ {total} da(s) diária(s)')
            return

        print('Você não realizou nenhuma reserva')

    def consumir(self, quarto: object, item: str):
        if item in quarto.itens:
            if quarto.itens[item]['quantidade'] >= 1:
                quarto.itens[item]['quantidade'] -= 1
                print(f'Foi consumido 1 {item} com sucesso')
                return
        print(f'Não foi possível consumir {item}')


# c = Cliente('raimundo', '4545464', 12)
# c.pagar_diaria()
#
# O valor do quarto varia de acordo com a categoria
# 	- X método para agendar no quarto
# 		X- metodo interno para verificar se a data é valida
# 	- lista items
#
# HOTEL = TER UM MÉTODO PARA IDENTIFICAÇÃO, METODO PARA PEDIR PASSAR ROUPA
# cliente = PAGA DIARIA DE ACORDO COM AS RESERVAS DELEX, consumir itemX
# (LISTA DE QUARTOS)
#
# funcionario locação do quarto