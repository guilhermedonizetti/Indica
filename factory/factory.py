"""
Classe para funcoes padrao, em comum ou recorrentes entre as classes
"""

class Factory:

    def elementos_nao_vazios(dados):
        """
        Função para verificar se nenhum elemento do array é vazio ou nulo.
        """

        if dados is None or len(dados) == 0:
            return False
        
        status = True
        for i in dados:
            if i == None or i == "":
                return False
        
        return status


