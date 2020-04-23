from typing import List, Dict


class FilaPrioritaria:
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def chama_cliente(self, caixa: int) -> List[str]:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return display

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

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
