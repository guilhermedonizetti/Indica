"""
Classe para criar a variavel de conexao com o BD
"""

from flaskext.mysql import MySQL
# from MySQLdb import cursors

class Conexao:
    

    def iniciar_banco_dados(app):
        """
        Método para iniciar a aplicação com a configuração do BD
        """
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = ''
        app.config['MYSQL_DATABASE_DB'] = 'bd_indica'

        try:            
            mysql = MySQL()
            mysql.init_app(app)
            conn = mysql.connect()
            conn = conn.cursor()

            return conn
            
        except Exception as e:
            return e

