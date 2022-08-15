class LogMixin:
    """
    Classe responsável pelo gerenciamento das logs (que são armazenadas em um arquivo), funcionando como um Mixin.
    """
    @staticmethod
    def escrever(mensagem: str) -> None:
        """
        Método estático responsável por escrever as logs no arquivo.
        :param mensagem: Mensagem a ser escrita no arquivo.
        :type mensagem: str
        :return: None
        :rtype: None
        """
        with open('log.txt', 'a+') as arquivo:
            arquivo.write(f'{mensagem}\n')

    def log_info(self, mensagem: str) -> None:
        """
        Método responsável por adicionar um préfixo 'Info' para caracterizar a relevância da Log.
        :param mensagem: Mensagem a ser escrita no arquivo.
        :type mensagem: str

        :return: None
        :rtype: None
        """
        self.escrever(f'Info: {mensagem}')

    def log_erro(self, mensagem: str) -> None:
        """
        Método responsável por adicionar um préfixo 'Error' para caracterizar a relevância da Log.
        :param mensagem: Mensagem a ser escrita no arquivo.
        :type mensagem: str

        :return: None
        :rtype: None
        """
        self.escrever(f'Error: {mensagem}')