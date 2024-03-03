from connect import Connect
from cliente import Cliente

class Controle:
    def insert(self, cliente):
        sql = 'INSERT INTO clientes (nome_cliente, endereco_cliente, telefone_cliente, data_nascimento)'
        sql += f' VALUES ("{cliente.get_nome()}", "{cliente.get_endereco()}", "{cliente.get_telefone()}",'
        sql += f' "{cliente.get_nascimento()}")'
        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def delete(self, id):
        sql = f'DELETE FROM clientes WHERE id_cliente = {id}'

        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False
        
    def update(self, cliente):
        sql = 'UPDATE clientes SET'
        sql += f' nome_cliente = "{cliente.get_nome()}",'
        sql += f' endereco_cliente = "{cliente.get_endereco()}",'
        sql += f' telefone_cliente = "{cliente.get_telefone()}",'
        sql += f' data_nascimento = "{cliente.get_nascimento()}"'
        sql += f' WHERE id_cliente = {cliente.get_id()}' 

        connect = Connect()
        if connect.execute(sql):
            return True
        else:
            return False

    def select(self, cliente):
        sql = 'SELECT * FROM clientes WHERE TRUE = TRUE'
        if cliente.get_id() !='':
            sql += f' and id_cliente = {cliente.get_id()}'
        if cliente.get_nome() !='':
            sql += f' and nome_cliente LIKE "%{cliente.get_nome()}%"'
        if cliente.get_endereco() !='':
            sql += f' and endereco_cliente = "{cliente.get_endereco()}"'
        if cliente.get_telefone() !='':
            sql += f' and telefone_cliente = "{cliente.get_telefone()}"'
        if cliente.get_nascimento() !='':
            sql += f' and data_nascimento = "{cliente.get_nascimento()}"'

        connect = Connect()
        produtos = connect.execute(sql)
        return produtos