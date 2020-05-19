from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:

    @staticmethod
    def pega_fila(tipo) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise(NotImplementedError('Tipo não cadastrado'))
