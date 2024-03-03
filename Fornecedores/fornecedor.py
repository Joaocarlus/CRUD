class Fornecedor:
    def __init__(self, nome_empresa, telefone_empresa, endereco_empresa, produtos_fornecidos):
        self.nome_empresa = nome_empresa
        self.telefone_empresa = telefone_empresa
        self.endereco_empresa = endereco_empresa
        self.produtos_fornecidos = produtos_fornecidos
        
    def print(self):
        print(f'ID: ,{self.id}')
        print(f'Nome da Empresa: ,{self.nome_empresa}')
        print(f'Telefone da Empresa: ,{self.telefone_empresa}')
        print(f'Endereço da Empresa: ,`{self.endereco_empresa}')
        print(f'Produtos Fornecidos: ,{self.produtos_fornecidos}')

    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id

    def set_nome_empresa(self, nome_empresa):
        self.nome_empresa = nome_empresa
    def get_nome_empresa(self):
        return self.nome_empresa

    def set_telefone_empresa(self, telefone_empresa):
        self.telefone_empresa = telefone_empresa
    def get_telefone_empresa(self):
        return self.telefone_empresa

    def set_endereco_empresa(self, endereco_empresa):
        self.endereco_empresa = endereco_empresa
    def get_endereco_empresa(self):
        return self.endereco_empresa

    def set_produtos_fornecidos(self, produtos_fornecidos):
        self.produtos_fornecidos = produtos_fornecidos
    def get_produtos_fornecidos(self):
        return self.produtos_fornecidos