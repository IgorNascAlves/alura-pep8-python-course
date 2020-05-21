from typing import Union

from src.fila_base import FilaBase
from src.constantes import SENHA_FILA_PRIORITARIA
from src.estatistica_simples import EstatisticaSimples
from src.estatistica_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaSimples, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{SENHA_FILA_PRIORITARIA}{self.codigo}'

    def estatistica(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.cria_estatisca(self.clientes_atendidos)
