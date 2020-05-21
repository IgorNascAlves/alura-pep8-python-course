from typing import Union, List, Dict

from src.estatistica import Estatistica


class EstatisticaDetalhada(Estatistica):

    def __init__(self, dia, agencia):
        super().__init__(dia, agencia)

    def cria_estatisca(self, clientes_atendidos: List[str]):
        estatistica: Dict[str, Union[int, str, List[str]]] = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes atendidos'] = clientes_atendidos
        estatistica['quantidade de clientes atendidos'] = (
                len(clientes_atendidos)
            )
        return estatistica
