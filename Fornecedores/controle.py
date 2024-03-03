from connect import Connect
from fornecedor import Fornecedor

class Controle:
    def insert(self, fornecedor):
        sql = 'INSERT INTO fornecedores (nome_empresa, telefone_empresa, endereco_empresa, produtos_fornecidos)'
        sql += f' VALUES ("{fornecedor.get_nome_empresa()}", "{fornecedor.get_telefone_empresa()}",'
        sql += f' "{fornecedor.get_endereco_empresa()}", "{fornecedor.get_produtos_fornecidos()}")'
    
        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def delete(self, id):
        sql = f'DELETE FROM fornecedores WHERE id_fornecedor = {id}'

        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False
        
    def update(self, fornecedor):
        sql = 'UPDATE fornecedores SET'
        sql += f' nome_empresa = "{fornecedor.get_nome_empresa()}",'
        sql += f' telefone_empresa = "{fornecedor.get_telefone_empresa()}",'
        sql += f' endereco_empresa = "{fornecedor.get_endereco_empresa()}",'
        sql += f' produtos_fornecidos = "{fornecedor.get_produtos_fornecidos()}"'
        sql += f' WHERE id_fornecedor = {fornecedor.get_id()}'
        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def select(self, fornecedor):
        sql = 'SELECT * FROM fornecedores WHERE TRUE = TRUE'
        if fornecedor.get_id() !='':
            sql += f' and id_fornecedor = {fornecedor.get_id()}'
        if fornecedor.get_nome_empresa() !='':
            sql += f' and nome_empresa LIKE "%{fornecedor.get_nome_empresa}%"'
        if fornecedor.get_telefone_empresa() !='':
            sql += f' and telefone_empresa = "{fornecedor.get_telefone_empresa}'
        if fornecedor.get_endereco_empresa() !='':
            sql += f' and endereco_empresa = "{fornecedor.get_endereco_empresa}"'
        if fornecedor.get_produtos_fornecidos() !='':
            sql += f' and produtos_fornecidos = "{fornecedor.get_produtos_fornecidos}"'
        connect = Connect()
        produtos = connect.execute(sql)
        return produtos