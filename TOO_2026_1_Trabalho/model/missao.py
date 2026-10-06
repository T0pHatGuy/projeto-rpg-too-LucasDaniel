class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = 'PENDENTE'

    @property
    def nome(self):
        return self._nome


    @property
    def descricao(self):
        return self._descricao


    @property
    def recompensa(self):
        return self._recompensa

    @property
    def status(self):
        return self._status

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")

    @descricao.setter
    def descricao(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._descricao = valor
        else:
            raise ValueError("Descrição inválida. Deve ser uma string não vazia.")

    @recompensa.setter
    def recompensa(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._recompensa = valor
        else:
            raise ValueError("Recompensa inválida. Deve ser um número não negativo.")

    @status.setter
    def status(self, valor):
        if valor in ['PENDENTE', 'EM ANDAMENTO', 'CONCLUIDA']:
            self._status = valor
        else:
            raise ValueError("Status inválido. Use 'PENDENTE', 'EM ANDAMENTO' ou 'CONCLUIDA'.")

    def iniciar_missao(self):
        if self.status == 'PENDENTE':
            self.status = "EM ANDAMENTO"
            return f"A missão {self.nome} começou! O objetivo é {self.descricao}."
        else:
            return f'A missão {self.nome} já foi iniciada!!!'

    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status}
'''

        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status}'


        