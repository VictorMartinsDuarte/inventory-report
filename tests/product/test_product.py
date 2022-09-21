from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        4, 'notebook', 'ebytr', '21/09/22', '10', '587496', 'Evitar sol')

    assert product.id == 4
    assert product.nome_do_produto == 'notebook'
    assert product.nome_da_empresa == 'ebytr'
    assert product.data_de_fabricacao == '21/09/22'
    assert product.data_de_validade == '10'
    assert product.numero_de_serie == '587496'
    assert product.instrucoes_de_armazenamento == 'Evitar sol'
