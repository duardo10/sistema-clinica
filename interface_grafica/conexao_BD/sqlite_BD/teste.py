import sqlite3

conexao = sqlite3.connect('teste.sqlite')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(cpf text NOT NULL PRIMARY KEY,
         nome text NOT NULL, email text NOT NULL)"""

nome = 'eduardo'
email = 'duardos36@gmail.com'
cursor.execute(sql)

cursor.close()
conexao.commit()
conexao.close()