from src.fila_base import FilaBase
from src.constantes import SENHA_FILA_NORMAL


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{SENHA_FILA_NORMAL}{self.codigo}'
