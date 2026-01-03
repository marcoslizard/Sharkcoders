class produto:
    def __init__(self,preco, nome, stock):
        self.preco = preco
        self.nome = nome
        self.stock = stock

    def mostra(self):
        print(self.preco, self.nome, self.stock)
    def comprar(self, quantidade):
        if self.stock >= quantidade:
            self.stock -= quantidade
            total = quantidade * self.preco
            return total
        else :
            print("Quantidade é maior que o Stock")

    def adicionar(self, quantidade):
        self.stock += quantidade

class loja:
    def __init__(self):
        self.produtos = []
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
    def listar_produtos(self):
        for p in self.produtos:
            p.mostra()
    def comprar_produto(self , quantidade , produto):
        if produto in self.produtos:
            total = produto.comprar(self,quantidade)
            print(total)
    def valor_loja(self):
        total = 0
        for produto in self.produtos:
            produto.mostra()
            total += produto.stock * produto.preco
        return total

#Programa principal
produto1 = produto(0.50,"Maçã",20)
produto2 = produto(1.20,"Banana",10)

loja = loja()
loja.adicionar_produtos(produto1)
loja.adicionar_produtos(produto2)

loja.listar_produtos()

loja.comprar_produto("Maçã",5)

loja.listar_produtos()

print(f"\nValor total da loja : {loja.valor_loja()}€")