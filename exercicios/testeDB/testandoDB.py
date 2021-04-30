import sqlite3

banco = sqlite3.connect('banco_teste.db')

cursor = banco.cursor()

#comentei a linha abaixo, pois se rodar o código novamente ele vai reclamar um erro, pois a tabela já foi criada.
#Cria a tabela 'cadastro'
#cursor.execute("CREATE TABLE cadastro (nome text, idade integer, email text, cidade text)")

#Adiciona valores na tabela
#cursor.execute("INSERT INTO cadastro VALUES ('Fernando', 59, 'Fernando@python.br', 'Fortaleza')")
#banco.commit()

#Imprime ma tela os valores contidos nela
cursor.execute("SELECT * FROM cadastro")
print(cursor.fetchall())