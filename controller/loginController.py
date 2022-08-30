"""
Classe relacionada ao Login
"""

from controller.startup import *

class Login:

    def login_usuario(dados, conexao):
        """
        Método para verificar existencia do registro do usuario
        """

        conexao = conexao.cursor()
        login = dados['login']
        senha = dados['senha']

        if factory.elementos_nao_vazios([login, senha]) == False:
            return False
        
        SQL = "SELECT * FROM usuarios WHERE email = '{}' AND senha = '{}'".format(login, senha)
        stmt = conexao.execute(SQL)

        existe = "N"
        if stmt > 0:
            existe = "S"
        
        return existe


