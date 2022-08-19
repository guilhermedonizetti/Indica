"""
Classe relacionada ao Login
"""

from flask import redirect, url_for

class Login:

    def login_usuario(login, senha):
        print("{} e {}".format(login, senha))
        return True