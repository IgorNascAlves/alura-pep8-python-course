from typing import Dict
from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: Dict[str, str] = {}
        if flag != 'detail':
            estatistica[f'{agencia} - {dia}'] = str(
                len(self.clientes_atendidos)
                )
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = str(agencia)
            estatistica['clientes atendidos'] = str(self.clientes_atendidos)
            estatistica['quantidade de clientes atendidos'] = (
                str(len(self.clientes_atendidos))
                )

        return estatistica
