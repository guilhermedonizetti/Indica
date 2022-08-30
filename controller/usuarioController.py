"""
Classe relacionada ao Usuario
"""

from datetime import datetime
from controller.startup import *

class Usuario:

    def registrar_novo_usuario(dados, conexao):
        """
        Método para registrar o novo usuario no BD
        """
        nome = dados['nome']
        email = dados['email']
        senha = dados['senha']

        if factory.elementos_nao_vazios([nome, email, senha]) == False:
            return False
        
        SQL = "INSERT INTO usuarios(nome, email, senha, tms_cadastro) VALUES('{}', '{}', '{}', '{}')".format(
            nome, email, senha, datetime.now()
        )

        cursor = conexao.cursor()
        cursor.execute(SQL)
        
        if conexao.commit():
            return "S"
        else:
            return "N"

