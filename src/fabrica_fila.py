from typing import Union

from src.fila_normal import FilaNormal
from src.fila_prioritaria import FilaPrioritaria
from src.constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:

    @staticmethod
    def pega_fila(tipo) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise(NotImplementedError('Tipo não cadastrado'))
