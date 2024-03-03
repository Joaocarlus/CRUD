class Produto:
    def __init__(self, nome_produto, preco, descricao, quantidade_estoque, categoria, fornecedor):
        self.nome = nome_produto
        self.preco = preco
        self.descricao = descricao
        self.estoque = quantidade_estoque
        self.categoria = categoria
        self.fornecedor = fornecedor

    def print(self):
        print(f'ID: ,{self.id}')
        print(f'Nome: ,{self.nome}')
        print(f'Preço: ,`{self.preco}')
        print(f'Descrição: ,{self.descricao}')
        print(f'Quantidade em Estoque: ,{self.estoque}')
        print(f'Categoria: ,{self.categoria}')
        print(f'Fornecedor: ,{self.fornecedor}')

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome

    def set_preco(self, preco):
        if preco < 0:
            return False
        else:
            self.preco = preco
            return True

    def get_preco(self):
        return self.preco

    def set_descricao(self, descricao):
        if len(self.descricao > 100):
            print('Erro! Descrição ultrapassou o Limite de 100 caracteres')
            return
        else:
            self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    def set_estoque(self, estoque):
        if self.estoque < 0:
            print('Erro!')
        else:
            self.estoque = estoque

    def get_estoque(self):
        return self.estoque

    def set_categoria(self, categoria):
        self.categoria = categoria
    
    def get_categoria(self):
        return self.categoria

    def set_fornecedor(self, fornecedor):
        self.fornecedor = fornecedor
    
    def get_fornecedor(self):
        return self.fornecedor