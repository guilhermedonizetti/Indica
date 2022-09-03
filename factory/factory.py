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
    

    def relacoes_de_proximidade(dado):
        """
        Função para retornar os possíveis relacionamentos entre pessoas.
        """

        if dado == "1":
            return "Estudaram juntos"
        elif dado == "2":
            return "Trabalharam juntos"
        elif dado == "3":
            return "Não tarabalharam juntos, mas sim na mesma empresa"
        elif dado == "4":
            return "Se conheceram fora do ambiente acadêmico e corporativo"
        else:
            return ""

