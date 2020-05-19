from typing import Dict, Union, List

from fila_base import FilaBase
from constantes import SENHA_FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{SENHA_FILA_PRIORITARIA}{self.codigo}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: Dict[str, Union[int, str, List[str]]] = {}
        if flag != 'detail':
            estatistica[f'{agencia} - {dia}'] = str(
                len(self.clientes_atendidos)
                )
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quantidade de clientes atendidos'] = (
                    len(self.clientes_atendidos)
                )
        return estatistica
