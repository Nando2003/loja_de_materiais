import sqlite3
from categoria import Categoria
from cliente import Cliente
from produto import Produto
from venda import Venda
from venda_produto import Venda_produto

Categoria()
Cliente()
Produto()
Venda()
Venda_produto()

conector = sqlite3.connect("./BANCO/loja_construcao.db")
cursor = conector.cursor()

categorias = [
    ("FERRAMENTA MANUAL",),
    ("FERRAMENTA ELETRICA",),
    ("MATERIAL DE CONTRUCAO",),
    ("PINTURA",)
]

clientes = [
    ("Fernando Luiz", "12312312300", "123"),
    ("Felipe", "12312312301", "123"),
    ("Carla", "12312312302", "123"),
    ("Guilherme", "12312312303", "123")
]

produtos = [
    ("Martelo", 100.0, 10, 1),
    ("Alicate", 120.0, 8, 1),
    ("Chave de fenda", 80.0, 5, 1),
    ("Furadeira", 200.0, 8, 2),
    ("Serra elétrica", 250.0, 13, 2),
    ("Lixadeira", 110.0, 11, 2),
    ("Tijolo", 55.0, 500, 3),
    ("Torneira", 40.0, 333, 3),
    ("Saco de areia", 70.0, 144, 3),
    ("Tinta Vermelha", 140.0, 50, 4),
    ("Tinta Amarela", 140.0, 43, 4),
    ("Papel de parede", 200.0, 23, 4)
]

vendas = [
    ("2023-04-01", 550, 1), # 10 tijolos
    ("2022-02-28", 500, 2), # 1 martelo, 1 alicate, 1 chave, 1 furadeira
    ("2023-10-25", 3030, 3), # 4 saco, 50 tijolo
    ("2023-11-21", 200, 1) # 1 papel
]

venda_produtos = [
    (10,550,1,7),
    (1,100,2,1),
    (1,120,2,2),
    (1,80,2,3),
    (1,200,2,4),
    (4,280,3,9),
    (50,2750,3,7),
    (1,200,4,12)
]

cursor.executemany("INSERT INTO categoria (nome_categoria) VALUES(?)", categorias)
cursor.executemany("INSERT INTO cliente (nome, cpf, endereco) VALUES(?,?,?)", clientes)
cursor.executemany("INSERT INTO produto (nome, preco_unitario, qtde_estoque, fk_id_categoria) VALUES(?,?,?,?)", produtos)
cursor.executemany("INSERT INTO venda (data_venda, valor_total, fk_id_cliente) VALUES(?,?,?)", vendas)
cursor.executemany("INSERT INTO venda_produto (qtde_venda,preco_venda,fk_id_venda,fk_id_produto) VALUES(?,?,?,?)", venda_produtos)


"""cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela_copia} AS SELECT * FROM {nome_tabela_original}")
cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela_original}")
cursor.execute(f"ALTER TABLE {nome_tabela_copia} RENAME TO {nome_tabela_original}")


cursor.executemany("INSERT INTO venda (data_venda, valor_total, fk_id_cliente) VALUES(?,?,?)", vendas)"""

conector.commit()
conector.close()



