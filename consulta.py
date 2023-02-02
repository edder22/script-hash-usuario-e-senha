# script para listar os logins dos usuarios
import sqlite3
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute('Select * FROM usuario;')
for i in cursor.fetchall():
    print(i)
    input('Pressione enter para sair ...')