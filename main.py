from hotel import Hotel
from pessoa import Cliente, Funcionario
from servicos import Servicos

raimundo = Cliente('Raimundo', '459445421', 18)
breno = Cliente('Breno', '5449879545', 65)

hotel = Hotel()
hotel.autenticar('sla')
hotel.cadastrar_cliente(raimundo)
hotel.cadastrar_cliente(breno)
hotel.encontrar_quarto_disponivel('15/04/2022', '16/04/2022', 'luxo', raimundo)
hotel.encontrar_quarto_disponivel('15/04/2022', '16/04/2022', 'luxo', breno)
hotel.autenticar(raimundo)
raimundo.solicitar_servico(Servicos.limpar_quarto)
raimundo.desocupar_quarto(0)
hotel.encontrar_quarto_disponivel('18/04/2022', '19/04/2022', 'simples', raimundo)
raimundo.pagar_diaria()
