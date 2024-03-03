from connect import Connect
from produto import Produto

class Controle:
    def insert(self, produto):
        sql = 'INSERT INTO produtos (nome_produto, preco, descricao, quantidade_estoque, categoria, fornecedor)'
        sql += f' VALUES ("{produto.get_nome()}", "{produto.get_preco()}", "{produto.get_descricao()}", "{produto.get_estoque()}", "{produto.get_categoria()}", "{produto.get_fornecedor()}")'
    
        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def delete(self, id):
        sql = f'DELETE FROM produtos WHERE id_produto = {id}'

        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False
        
    def update(self, produto):
        sql = 'UPDATE produtos SET'
        sql += f' nome_produto = "{produto.get_nome()}",'
        sql += f' preco = "{produto.get_preco()}",'
        sql += f' descricao = "{produto.get_descricao()}",'
        sql += f' quantidade_estoque = "{produto.get_estoque()}",'
        sql += f' categoria = "{produto.get_categoria()}",'
        sql += f' fornecedor = "{produto.get_fornecedor()}"'
        sql += f' WHERE id_produto = "{produto.get_id()}"'

        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def select(self, produto):
        sql = 'SELECT * FROM produtos WHERE TRUE = TRUE'
        if produto.get_id() !='':
            sql += f' and id_produto = {produto.get_id()}'
        if produto.get_nome() !='':
            sql += f' and nome_produto LIKE "%{produto.get_nome()}%"'
        if produto.get_preco() !='':
            sql += f' and preco = {produto.get_preco()}'
        if produto.descricao!='':
            sql += f' and descricao = "{produto.get_descricao()}"'
        if produto.get_estoque() !='':
            sql += f' and quantidade_estoque = {produto.get_estoque()}'
        if produto.get_categoria() !='':
            sql += f' and categoria = "{produto.get_categoria()}"'
        if produto.get_fornecedor() !='':
            sql += f' and fornecedor = "{produto.get_fornecedor()}"'

        connect = Connect()
        produtos = connect.execute(sql)
        return produtos