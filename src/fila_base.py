from abc import ABCMeta, abstractmethod
from typing import List

from src.constantes import TAMANHO_MAXIMO, TAMANHO_MINIMO


class FilaBase(metaclass=ABCMeta):
    def __init__(self):
        self.codigo: int = TAMANHO_MINIMO
        self.fila: List[str] = []
        self.clientes_atendidos: List[str] = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO:
            self.codigo = TAMANHO_MINIMO
        else:
            self.codigo += 1

    def chama_cliente(self, caixa: int) -> List[str]:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: {cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return display

    def inserir_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inserir_cliente()

    @abstractmethod
    def gera_senha_atual(self) -> None:
        ...
