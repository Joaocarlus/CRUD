class Cliente:
    def __init__(self,nome_cliente, endereco_cliente, telefone_cliente, data_nascimento):
        self.nome = nome_cliente
        self.endereco = endereco_cliente
        self.telefone = telefone_cliente
        self.nascimento = data_nascimento

    def print(self):
        print(f'ID: ,{self.id}')
        print(f'Nome: ,{self.nome}')
        print(f'Endereço: ,`{self.endereco}')
        print(f'Telefone: ,{self.telefone}')
        print(f'Data de Nascimento: ,{self.nascimento}')

    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome

    def set_endereco(self, endereco):
        self.endereco = endereco
    def get_endereco(self):
        return self.endereco

    def set_telefone(self, telefone):
        self.telefone= telefone
    def get_telefone(self):
        return self.telefone
    
    def set_nascimento(self, nascimento):
        self.nascimento = nascimento
    def get_nascimento(self):
        return self.nascimento

    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id