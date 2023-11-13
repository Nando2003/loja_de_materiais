import sqlite3

class Venda_produto:
    
    def __init__(self):
        self.connectDB = sqlite3.connect("./BANCO/loja_construcao.db")
        self.cursorDB = self.connectDB.cursor()
        self.criarTabela()
       
        
    def criarTabela(self):
        self.cursorDB.execute("""
        CREATE TABLE IF NOT EXISTS venda_produto(
        id_venda_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        qtde_venda INT NOT NULL,
        preco_venda DOUBLE NOT NULL,
        fk_id_venda INTEGER,
        fk_id_produto INTEGER,
        FOREIGN KEY(fk_id_venda) REFERENCES venda(id_venda),
        FOREIGN KEY(fk_id_produto) REFERENCES produto(id_produto)
        );
        """)        
        self.salvarTabela()

    def verificarID(self, id_e):
        self.cursorDB.execute("SELECT id_venda_produto FROM venda_produto WHERE id_venda_produto = ?", (id_e,))
        if self.cursorDB.fetchone():
            return True
        else:
            return False

    def temVenda_produto(self, id_venda_produto=None):
        
        if id_venda_produto is None:
            self.cursorDB.execute("SELECT * FROM venda_produto")
            if self.cursorDB.fetchone():
                return True
            else:
                return False
        else:
            self.cursorDB.execute("SELECT * FROM venda_produto WHERE id_venda_produto = ?", (id_venda_produto,))
            if self.cursorDB.fetchone():
                return True
            else:
                return False
    
    def validarProduto(self, id_produto):
        self.cursorDB.execute("SELECT * FROM produto WHERE id_produto = ?", (id_produto,))
        produto = self.cursorDB.fetchone()

        if produto:
            return produto
    
        else:
            return False
   
    def validarVenda(self, id_venda):
        self.cursorDB.execute("SELECT * FROM venda WHERE id_venda = ?", (id_venda,))
        venda = self.cursorDB.fetchone()

        if venda is None:
            return False
        else:
            return venda


    def cadastrarVenda_produto(self, qtde_venda, fk_id_produto, fk_id_venda):
        
        produto = self.validarProduto(fk_id_produto)
        venda = self.validarVenda(fk_id_venda)
        
        try:
            if produto and venda:
                
                fk_id_produto = int(fk_id_produto)
                fk_id_venda = int(fk_id_venda)
                qtde_venda = int(qtde_venda)

                self.cursorDB.execute("INSERT INTO venda_produto (qtde_venda, preco_venda, fk_id_venda, fk_id_produto) VALUES (?,?,?,?)",
                                    (qtde_venda, ((float(produto[2])*qtde_venda)), fk_id_venda, fk_id_produto))
                self.salvarTabela() 
                
            
                return True, "venda_produto cadastrada com sucesso!"
            
            else:
                return False, "id_produto ou id_venda não existem, ou qtde_venda extrapola qtde_estoque!"
            
        except ValueError:

            return False, "O preço da venda é um número real e os IDs e quantidade de estoque são números inteiros"
    
    
    def exibirVenda_produto(self):
        
        self.cursorDB.execute("SELECT * FROM venda_produto")
        venda_produtos = self.cursorDB.fetchall()
        
        return venda_produtos
    
    
    def pesquisar(self, id_venda_produto=None, qtde_venda=None, preco_venda=None, fk_id_venda=None, fk_id_produto=None):
       
        if id_venda_produto or qtde_venda or preco_venda or fk_id_venda or fk_id_produto:
            
            consulta = "SELECT * FROM venda_produto WHERE "
            valores = []
            
            if id_venda_produto is not None:
                consulta += "id_venda_produto = ?"
                valores.append(id_venda_produto)
            
            if qtde_venda is not None:
                if id_venda_produto:
                    consulta += " AND "
                consulta += "qtde_venda = ?"
                valores.append(qtde_venda)
            
            if preco_venda is not None:
                if id_venda_produto or qtde_venda:
                    consulta += " AND "
                consulta += "preco_venda = ?"
                valores.append(preco_venda)
            
            if fk_id_venda is not None:
                if id_venda_produto or qtde_venda or preco_venda:
                    consulta += " AND "
                consulta += "fk_id_venda = ?"
                valores.append(fk_id_venda)
                
            if fk_id_produto is not None:
                if id_venda_produto or qtde_venda or preco_venda or fk_id_venda:
                    consulta += " AND "
                consulta += "fk_id_produto = ?"
                valores.append(fk_id_produto)
            
            print(consulta, tuple(valores))
            try:
                self.cursorDB.execute(consulta, tuple(valores))
                return True, self.cursorDB.fetchall()
            
            except sqlite3.Error as erro:
                return False, f"Erro ao pesquisar produto: {erro}"
    
    def excluirTudo(self):
        self.cursorDB.execute("DELETE FROM venda_produto WHERE id_venda_produto > 0")
        self.salvarTabela()
        return "Todos os venda_produto foram excluídos com sucesso!"
    
    
    def excluirID(self, id_e):
        
        try:
            id_e = int(id_e)
            self.cursorDB.execute("SELECT id_venda_produto FROM venda_produto WHERE id_venda_produto = ?", (id_e,))
            if self.cursorDB.fetchone() is not None:
                self.cursorDB.execute("DELETE FROM venda_produto WHERE id_venda_produto = ?", (id_e,))
                self.salvarTabela()
                return f"venda_produto {id_e} excluída com sucesso!"
            else:
                return f"Nenhum venda_produto {id_e} encontrada."
            
        except ValueError:
            return "Error"
        
    
    def excluirFK_id_venda(self, fk_id_venda):
        
        try:
            fk_id_venda = int(fk_id_venda)
            self.cursorDB.execute("SELECT fk_id_venda FROM venda_produto WHERE fk_id_venda = ?", (fk_id_venda,))
            if self.cursorDB.fetchone() is not None:
                self.cursorDB.execute("DELETE FROM venda_produto WHERE fk_id_venda = ?", (fk_id_venda,))
                self.salvarTabela()
                return f"venda_produto {fk_id_venda} excluída com sucesso!"
            else:
                return f"Nenhum venda_produto {fk_id_venda} encontrada."
            
        except ValueError:
            return "Error"
        
        
    def excluirFK_id_produto(self, fk_id_produto):
        
        try:
            fk_id_produto = int(fk_id_produto)
            self.cursorDB.execute("SELECT fk_id_produto FROM venda_produto WHERE fk_id_produto = ?", (fk_id_produto,))
            if self.cursorDB.fetchone() is not None:
                self.cursorDB.execute("DELETE FROM venda_produto WHERE fk_id_produto = ?", (fk_id_produto,))
                self.salvarTabela()
                return f"venda_produto {fk_id_produto} excluída com sucesso!"
            else:
                return f"Nenhum venda_produto {fk_id_produto} encontrada."
            
        except ValueError:
            return "Error"
    
    def atualizarVenda_produto(self, id_venda_produto, nova_qtde=None, nova_fk_id_venda=None, nova_fk_id_produto=None):
        
        if self.temVenda_produto(id_venda_produto=id_venda_produto):
            if nova_qtde is not None or nova_fk_id_venda is not None or nova_fk_id_produto is not None:
            
                consulta = "UPDATE venda_produto SET "
                valores = []
            
            try:    
                if nova_qtde is not None:
                    nova_qtde = int(nova_qtde)
                    if nova_qtde == 0:
                        return False, "Quantidade não pode ser 0"
                    
                    consulta += "qtde_venda = ?,"
                    valores.append(nova_qtde)
                    
                if nova_fk_id_venda is not None and self.validarVenda(nova_fk_id_venda):
                    nova_fk_id_venda = int(nova_fk_id_venda)
                    
                    if nova_fk_id_venda == 0:
                        return False, "Venda não pode ser 0"
                    
                    consulta += "fk_id_venda = ?,"
                    valores.append(nova_fk_id_venda)

                produto = self.validarProduto(nova_fk_id_produto)
                if nova_fk_id_produto is not None and produto:
                    nova_fk_id_produto = int(nova_fk_id_produto)
                    
                    if nova_fk_id_produto == 0:
                        return False, "Produto não pode ser 0"
                    
                    consulta += "fk_id_produto = ?,"
                    valores.append(nova_fk_id_produto)
                                        
                consulta = consulta.rstrip(",")
                consulta += "WHERE id_venda_produto = ?"
                valores.append(id_venda_produto)
                
                print(consulta, valores)
                self.cursorDB.execute(consulta, tuple(valores))
                
                if nova_fk_id_produto is None and nova_qtde is not None:
                    
                    self.cursorDB.execute("SELECT fk_id_produto FROM venda_produto WHERE id_venda_produto = ?", (id_venda_produto,))
                    fk_id_produto = self.cursorDB.fetchone()
                    
                    produto2 = self.validarProduto(fk_id_produto[0])
                    
                    preco_unitario = produto2[2]
                    preco_unitario = str(preco_unitario)
                    
                    novo_preco = float(nova_qtde)*float(produto2[2])
                    
                    print(novo_preco, produto2[2])
                    print(type(novo_preco), type(produto2[2]))
                    self.cursorDB.execute("UPDATE venda_produto SET preco_venda = ? WHERE id_venda_produto = ?", (novo_preco, id_venda_produto))
                    
                elif nova_qtde is None and nova_fk_id_produto is not None:
                    self.cursorDB.execute("SELECT qtde_venda FROM venda_produto WHERE id_venda_produto = ?", (id_venda_produto,))
                    qtde_venda = self.cursorDB.fetchone()
                    
                    produto3 = self.validarProduto(nova_fk_id_produto)
                    
                    preco_unitario = produto3[2]
                    preco_unitario = str(preco_unitario)
                    
                    novo_preco = float(qtde_venda)* float(preco_unitario)
                    self.cursorDB.execute("UPDATE venda_produto SET preco_venda = ? WHERE id_venda_produto = ?", (novo_preco, id_venda_produto))
                    
                elif nova_qtde and nova_fk_id_produto:
                    produto4 = self.validarProduto(nova_fk_id_produto)

                    preco_unitario = produto4[2]
                    preco_unitario = str(preco_unitario)
                    
                    novo_preco = float(nova_qtde)*float(preco_unitario)
                    self.cursorDB.execute("UPDATE venda_produto SET preco_venda = ? WHERE id_venda_produto = ?", (novo_preco, id_venda_produto))
                    
                self.salvarTabela()
                
                return True, "Venda_produto atualizado com sucesso!"

            except sqlite3.Error as erro:
                return False, f"Erro ao atualizar venda_produto: {erro}"
            
            except ValueError as erro:
                return False, f"Erro ao atualizar venda_produtoto: {erro}"
            
        else:
            return False, f"id_venda_produto não encontrado!"
    
    
    def salvarTabela(self):
        self.connectDB.commit()
        
        
if __name__ == "__main__":
    Venda_produto().atualizarVenda_produto(1, nova_qtde=1)
