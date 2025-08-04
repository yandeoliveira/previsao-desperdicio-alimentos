class ProdutoAlimenticio:
    def __init__(self, nome, categoria, quantidade, data_validade):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.data_validade = data_validade

    def __repr__(self):
        return f"ProdutoAlimenticio(nome={self.nome}, categoria={self.categoria}, quantidade={self.quantidade}, data_validade={self.data_validade})"