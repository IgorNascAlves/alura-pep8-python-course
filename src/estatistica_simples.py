from typing import Union, List, Dict

from src.estatistica import Estatistica


class EstatisticaSimples(Estatistica):

    def __init__(self, dia, agencia):
        super().__init__(dia, agencia)

    def cria_estatisca(self, clientes_atendidos: List[str]):
        estatistica: Dict[str, Union[int, str, List[str]]] = {}
        estatistica[f'{self.agencia} - {self.dia}'] = str(
                len(clientes_atendidos)
                )
        return estatistica
