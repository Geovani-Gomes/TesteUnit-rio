import pytest
from estoque import Estoque

def test_consultar_estoque():
    estoque = Estoque()
    assert estoque.consultar_estoque("cimento") == 80
    assert estoque.consultar_estoque("tijolo") == 100
    assert estoque.consultar_estoque("pisos") == 100

def test_adicionar_item():
    estoque = Estoque()
    estoque.adicionar_item("cimento", 20)
    assert estoque.consultar_estoque("cimento") == 100

    estoque.adicionar_item("pisos", 50)
    assert estoque.consultar_estoque("pisos") == 150

def test_remover_item():
    estoque = Estoque()
    assert estoque.remover_item("tijolo", 50) is True
    assert estoque.consultar_estoque("tijolo") == 50

    assert estoque.remover_item("tijolo", 60) is False  # Tentativa de remover mais do que o disponível
    assert estoque.remover_item("madeira", 10) is False  # Tentativa de remover item inexistente
