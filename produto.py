class Produto:
    """
    Representa um produto no sistema GreenLink.

    :param nome: Nome do produto
    :type nome: str
    :param preco: Preço unitário do produto
    :type preco: float
    :param stock: Quantidade disponível em stock
    :type stock: int
    """
    def __init__(self, nome, preco, stock):
        """
        Inicializa um novo produto com nome, preço e quantidade em stock.

        :param nome: Nome do produto
        :param preco: Preço unitário do produto
        :param stock: Quantidade disponível em stock
        """
        self.nome = nome
        self.preco = preco
        self.stock = stock
