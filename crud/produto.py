import sqlite3
import string


class Produto:


    def __init__(self):
        self.connectDB = sqlite3.connect("./BANCO/loja_construcao.db")
        self.cursorDB = self.connectDB.cursor()
        self.criarTabela()

  
    def criarTabela(self):
        self.cursorDB.execute("""
        CREATE TABLE IF NOT EXISTS produto(
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco_unitario REAL NOT NULL,
        qtde_estoque INTEGER NOT NULL,
        fk_id_categoria INTEGER,
        FOREIGN KEY(fk_id_categoria) REFERENCES categoria(id_categoria)
        );
        """)

        self.salvarTabela()
        
    
    def temProduto(self):
        self.cursorDB.execute(f"SELECT nome FROM produto")
        if self.cursorDB.fetchone() is not None:
            return True
        else:
            return False

    def verificarID(self, id_e):
        self.cursorDB.execute(f"SELECT * FROM produto WHERE id_produto = ?", (id_e,))
        existeID = self.cursorDB.fetchone()
        
        if existeID is not None:
            return True
        
        else:
            return False
    
    def validarProdutos(self, preco_unitario, qtde_estoque, fk_id_categoria):
        pass
    
    def cadastrarProduto(self, nome, preco_unitario, qtde_estoque, fk_id_categoria):
        
        try:
            preco_unitario = float(preco_unitario)
            qtde_estoque = int(qtde_estoque)   
            fk_id_categoria = int(fk_id_categoria)
            
            self.cursorDB.execute("SELECT id_categoria FROM categoria WHERE id_categoria = ?",(fk_id_categoria,))
            
            if self.cursorDB.fetchone():
                
                self.cursorDB.execute("INSERT INTO produto (nome, preco_unitario, qtde_estoque, fk_id_categoria) VALUES (?,?,?,?)",
                                        (nome, preco_unitario, qtde_estoque, fk_id_categoria))
                self.salvarTabela()
                    
                return True, "Produto cadastrado com sucesso!"
            
            else:
                
                return False, "ID Categoria não existente!"
            
        except ValueError:
            
            return False, "ValueError!"
    
        except sqlite3.Error as e:
            
            return False, e
        
    
    def exibirProdutos(self):
        self.cursorDB.execute("SELECT * FROM produto")
        produtos = self.cursorDB.fetchall()
        
        return produtos
    
    
    def pesquisar(self, id_p=None, nome_p=None, preco_p=None, quantidade_p=None, categoria_p=None):
       
        if id_p or nome_p or preco_p or quantidade_p or categoria_p:
            
            consulta = "SELECT * FROM produto WHERE "
            valores = []
            
            if id_p is not None:
                consulta += f"id_produto = ?"
                valores.append(id_p)
            
            if nome_p is not None:
                consulta += f"nome LIKE ?"
                valores.append(nome_p + '%')
                
            if preco_p is not None:
                if nome_p is not None:
                    consulta += " AND "
                consulta += "preco_unitario = ?"
                valores.append(preco_p)
            
            if quantidade_p is not None:
                if nome_p is not None or preco_p is not None:
                    consulta += " AND "
                consulta += "qtde_estoque = ?"
                valores.append(quantidade_p)
                
            if categoria_p is not None:
                if nome_p is not None or preco_p is not None or quantidade_p is not None:
                    consulta += " AND "
                consulta += "fk_id_categoria = ?"
                valores.append(categoria_p)

            print(consulta, tuple(valores))
                
            try:
                self.cursorDB.execute(consulta, tuple(valores))
                return True, self.cursorDB.fetchall()
            
            except sqlite3.Error as erro:
                return False, f"Erro ao pesquisar produto: {erro}"
            
                 
    def pesquisarPrecoOFF(self, crescente, menorPreco, maiorPreco):
        if crescente is True:
            self.cursorDB.execute("SELECT * FROM produto WHERE preco_unitario >= ? and preco_unitario <= ? ORDER BY preco_unitario ASC", (menorPreco, maiorPreco))
            produtos = self.cursorDB.fetchall()
            
            return produtos
        
        else:
            self.cursorDB.execute("SELECT * FROM produto WHERE preco_unitario >= ? and preco_unitario <= ? ORDER BY preco_unitario DESC", (menorPreco, maiorPreco))
            produtos = self.cursorDB.fetchall()

            return produtos
    
    def excluirTudo(self):
        self.cursorDB.execute("DELETE FROM produto WHERE id_produto > 0")
        self.salvarTabela()
        return "Todos os produtos foram excluídos com sucesso!"
    
    
    def excluirID(self, id_e):
        try:
            id_e = int(id_e)
            self.cursorDB.execute("SELECT id_produto FROM produto WHERE id_produto = ?", (id_e,))
            if self.cursorDB.fetchone() is not None:
                self.cursorDB.execute("DELETE FROM produto WHERE id_produto = ?", (id_e,))
                self.salvarTabela()
                return f"Produto {id_e} excluído com sucesso!"
            else:
                return f"Nenhum produto {id_e} encontrado."
            
        except ValueError:
            return "Error"
        

    def excluirNome(self, nome_e):
        self.cursorDB.execute(f"SELECT nome FROM produto WHERE nome LIKE '{nome_e}%'")
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute(f"DELETE FROM produto WHERE nome LIKE '{nome_e}%'")
            self.salvarTabela()
            return f"Produto {nome_e} excluído com sucesso!"
        else:
            return f"Nenhum produto {nome_e} encontrado." 
    
    
    def excluirCategoria(self, id_categoria_e):
        self.cursorDB.execute("SELECT id_categoria FROM produto WHERE id_categoria = ?", (id_categoria_e,))
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute("DELETE FROM produto WHERE id_categoria = ?", (id_categoria_e,))
            self.salvarTabela()
            return f"Produto com id_categoria {id_categoria_e} excluído com sucesso!"
        else:
            return f"Nenhum produto com id_categoria {id_categoria_e} encontrado." 


    def atualizarProduto(self, id, novo_nome=None, novo_preco=None, nova_qtde=None, fk_id_categoria=None):
        
        self.cursorDB.execute("SELECT id_produto FROM produto WHERE id_produto = ?", (id,))
        if self.cursorDB.fetchone() is not None:
            
            if novo_nome is not None or novo_preco is not None or nova_qtde is not None or fk_id_categoria is not None:
            
                consulta = "UPDATE produto SET "
                valores = []
            
            try:    
                if novo_nome is not None:
                    consulta += "nome = ?,"
                    valores.append(novo_nome)
                    
                if novo_preco is not None:
                    novo_preco = float(novo_preco)
                    consulta += "preco_unitario = ?,"
                    valores.append(novo_preco)

                if nova_qtde is not None:
                    nova_qtde = int(nova_qtde)
                    consulta += "qtde_estoque = ?,"
                    valores.append(nova_qtde)
                    
                if fk_id_categoria is not None:
                    fk_id_categoria = int(fk_id_categoria)
                    consulta += "fk_id_categoria = ?,"
                    valores.append(fk_id_categoria)
                    
                    self.cursorDB.execute("SELECT id_categoria FROM categoria WHERE id_categoria = ?",(fk_id_categoria,))            
                    if self.cursorDB.fetchone():
                        pass
                    else:
                        return False, "ID_CATEGORIA NÃO EXISTENTE!"
                                        
                consulta = consulta.rstrip(",")
                consulta += "WHERE id_produto = ?"
                valores.append(id)
                
                self.cursorDB.execute(consulta, tuple(valores))
                self.salvarTabela()
                return True, "Produto atualizado com sucesso!"

            except sqlite3.Error as erro:
                return False, f"Erro ao atualizar produto: {erro}"
            
            except ValueError as erro:
                return False, f"Erro ao atualizar produto: {erro}"
            
        else:
            return False, f"Prdouto com o id {id} não encontrado!"
    
    def salvarTabela(self):
        self.connectDB.commit()
    
    
if __name__ == "__main__":
    Produto()