from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        4, 'notebook', 'ebytr', '21/09/22', '10', '587496', 'Evitar sol')

    assert product.__repr__() == (
            f"O produto {product.nome_do_produto}"
            f" fabricado em {product.data_de_fabricacao}"
            f" por {product.nome_da_empresa} com validade"
            f" até {product.data_de_validade}"
            f" precisa ser armazenado {product.instrucoes_de_armazenamento}.")
