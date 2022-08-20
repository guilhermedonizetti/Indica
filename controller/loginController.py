"""
Classe relacionada ao Login
"""

from flask_mysqldb import MySQL
from MySQLdb import cursors

class Login:

    def login_usuario(login, senha):
        print("{} e {}".format(login, senha))
        return True