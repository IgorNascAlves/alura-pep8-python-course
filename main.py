from src.fabrica_fila import FabricaFila
from src.estatistica_detalhada import EstatisticaDetalhada
from src.estatistica_simples import EstatisticaSimples


print("----------Fila Normal----------")
fila_teste = FabricaFila.pega_fila('normal')
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

print("\n----------Fila Prioritaria----------")
fila_teste_2 = FabricaFila.pega_fila('prioritaria')
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(10))

print(fila_teste_2.estatistica(EstatisticaSimples('10/01/1993', 198)))
print(fila_teste_2.estatistica(EstatisticaDetalhada('10/01/1993', 198)))
