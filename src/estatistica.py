from abc import ABCMeta, abstractmethod
from typing import List


class Estatistica(metaclass=ABCMeta):
    def __init__(self, agencia, dia):
        self.agencia = agencia
        self.dia = dia

    @abstractmethod
    def cria_estatisca(self, clientes_atendidos: List[str]) -> None:
        ...
