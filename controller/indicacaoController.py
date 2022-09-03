"""
 Classe relaciona a Indicacao de uma pessoa para outra
"""

from datetime import datetime

class Indicacao:

    def cadastrar_indicacao(dados, conn):
        """
        Funcao para registrar no BD a indicacao feita
        """

        proximidade = dados['proximidade']
        indicacao = dados['indicacao']
        flg_status = 'P'

        SQL = "INSERT INTO indicacoes(proximidade, conteudo, tms_cadastro, flg_status) VALUES({}, '{}', '{}', '{}')".format(
            proximidade, indicacao, datetime.now(), flg_status
        )

        cursor = conn.cursor()

        if cursor.execute(SQL):
            conn.commit()
            return "S"
        else:
            return "N"
