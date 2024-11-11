class Estoque:
    def __init__(self):
        self.itens = {
            "cimento": 80,
            "tijolo": 100,
            "telha": 100,
            "pisos": 100
        }

    def consultar_estoque(self, item):
        return self.itens.get(item, 0)

    def adicionar_item(self, item, quantidade):
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade
        return self.itens[item]

    def remover_item(self, item, quantidade):
        if item in self.itens and self.itens[item] >= quantidade:
            self.itens[item] -= quantidade
            return True
        return False
