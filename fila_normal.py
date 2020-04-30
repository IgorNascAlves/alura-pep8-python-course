from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'
