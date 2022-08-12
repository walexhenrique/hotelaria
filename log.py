class LogMixin:
    @staticmethod
    def escrever(mensagem):
        with open('log.txt', 'a+') as arquivo:
            arquivo.write(f'{mensagem}\n')

    def log_info(self, mensagem):
        self.escrever(f'Info: {mensagem}')

    def log_erro(self, mensagem):
        self.escrever(f'Error: {mensagem}')