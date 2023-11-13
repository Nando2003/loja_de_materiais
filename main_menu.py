from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from main_venda import vendaMenu
from main_categoria import categoriaMenu
from main_produto import produtoMenu
from main_venda_produto import venda_produtoMenu
from main_cliente import clienteMenu

conector = sqlite3.connect("./BANCO/loja_construcao.db")
cursor = conector.cursor()

##### JANELA #####

janela = Tk()
janela.title("MENU PRINCIPAL")
janela.geometry("1300x800")
janela.configure(bg="#e9edf5")
janela.resizable(width=False, height=False)

##### FRAME #####

frameTitulo = Frame(janela,
               width=640,
               height=50,
               bg="#000000", 
               relief="flat"
               )

framePrincipal = Frame(janela,
               width=640,
               height=750,
               bg="#feffff", 
               relief="flat"
               )

framePrincipal_esquerda = Frame(framePrincipal,
                width=320,
                height=750,
                bg="#feffff", 
                relief="flat"
                )

framePrincipal_direita = Frame(framePrincipal,
                width=320,
                height=750,
                bg="#feffff", 
                relief="flat"
                )

frameTabela = Frame(janela,
               width=640,
               height=750,
               bg="#feffff", 
               relief="flat"
               )

frameTitulo.grid(row=0,column=0)
framePrincipal.grid(row=1,column=0)
framePrincipal_esquerda.grid(row=0,column=0)
framePrincipal_direita.grid(row=0,column=1)
frameTabela.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="MENU PRINCIPAL", bg="#000000", fg="#feffff", relief="flat")
appNome.place(x=220, y=11)

def venda():
    vendaMenu(janela)
    
def categoria():
    categoriaMenu(janela)
    
def produto():
    produtoMenu(janela)
    
def venda_produto():
    venda_produtoMenu(janela)
    
def cliente():
    clienteMenu(janela)
    
def atualizar():
    cursor.execute("""
                   SELECT id_venda, data_venda, valor_total, venda_produto.preco_venda, venda_produto.qtde_venda, produto.nome, produto.preco_unitario 
                   FROM venda 
                   LEFT JOIN venda_produto 
                   ON venda.id_venda = venda_produto.fk_id_venda 
                   LEFT JOIN produto
                   ON venda_produto.fk_id_produto = produto.id_produto
                   """)
    
    resultado = cursor.fetchall()
    tree(resultado)
    

b_venda = Button(framePrincipal_esquerda, 
                     command=venda,
                     width=35, 
                     height=8, 
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="MENU VENDA", 
                     bg="#a0a0a0", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_venda.place(x=15, y=50)

b_venda_produto = Button(framePrincipal_esquerda, 
                     command=venda_produto,
                     width=35, 
                     height=8, 
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="MENU VENDA_PRODUTO", 
                     bg="#20b2aa", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_venda_produto.place(x=15, y=200)

b_produto = Button(framePrincipal_esquerda, 
                     command=produto,
                     width=35, 
                     height=8, 
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="MENU PRODUTO", 
                     bg="#4fa882", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_produto.place(x=15, y=350)

b_cliente = Button(framePrincipal_direita, 
                     command=cliente,
                     width=35, 
                     height=8, 
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="MENU CLIENTE", 
                     bg="#add8e6", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_cliente.place(x=15, y=50)

b_categoria = Button(framePrincipal_direita, 
                     command=categoria,
                     width=35, 
                     height=8,
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="MENU CATEGORIA", 
                     bg="#cf9bcc", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_categoria.place(x=15, y=200)

b_atualizar = Button(framePrincipal_direita, 
                     command=atualizar,
                     width=35, 
                     height=8, 
                     anchor=CENTER, 
                     font=("ARIAL 10 bold"), 
                     text="ATUALIZAR TABELA", 
                     bg="#47beea", 
                     fg="#403d3d", 
                     relief="raised", 
                     overrelief="ridge")

b_atualizar.place(x=15, y=350)

cursor.execute("""
                   SELECT id_venda, data_venda, valor_total, venda_produto.preco_venda, venda_produto.qtde_venda, produto.nome, produto.preco_unitario 
                   FROM venda 
                   LEFT JOIN venda_produto 
                   ON venda.id_venda = venda_produto.fk_id_venda 
                   LEFT JOIN produto
                   ON venda_produto.fk_id_produto = produto.id_produto
                   """)
    
resultado = cursor.fetchall()

def tree(clientes):
    
    tabelaColunas = ["ID venda","Data venda","Valor total","Preço venda","Qtde venda","Produto","Preço unitario"]

    tabelaDF = clientes

    tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
    vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

    tree.configure(yscrollcommand=vsb.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    frameTabela.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center", "center", "center", "center"]
    h =[90,90,90,90,90,95,90]
    n = 0

    for col in tabelaColunas:
        tree.heading(col, text=col, anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
                
        n+=1

    for item in tabelaDF:
        tree.insert("", "end", values=item)
        
tree(resultado)

janela.mainloop()