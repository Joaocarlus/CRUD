import mysql.connector 


class Connect:
    def abrir_conexao(self):
        self.con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'supermercado'
        )

    def execute(self, sql):
        self.abrir_conexao()
        self.cursor = self.con.cursor()
        self.cursor.execute(sql)
        if 'SELECT' in sql.upper().strip()[0:6]:
            resposta = self.cursor.fetchall()
        else:
            resposta = True
            self.con.commit()
        self.fechar_conexao()
        return resposta

    def fechar_conexao(self):
        if self.con:
            self.con.close()
        if self.cursor:
            self.cursor.close()