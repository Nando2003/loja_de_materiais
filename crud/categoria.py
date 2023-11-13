import sqlite3


class Categoria:


    def __init__(self):
        self.connectDB = sqlite3.connect("./BANCO/loja_construcao.db")
        self.cursorDB = self.connectDB.cursor()
        self.criarTabela()

  
    def criarTabela(self):
        self.cursorDB.execute("""
        CREATE TABLE IF NOT EXISTS categoria(
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL UNIQUE
        );
        """)

        self.salvarTabela()
    
    def temVerifica(self,categoria_v):
        
        try:
            self.cursorDB.execute("SELECT * FROM categoria WHERE id_categoria = ?", (categoria_v,))
            if self.cursorDB.fetchone() is None:
                return False
            else:
                return True
        
        except ValueError:
            return False
      
    def temCategoria(self):
        self.cursorDB.execute("SELECT * FROM categoria")
        if self.cursorDB.fetchone() is None:
            return False
        else:
            return True
    
    def validacaoCategoria(self, categoria_v):
        
        try:
            if (type(categoria_v) == str and categoria_v.strip() == "") or categoria_v is None:
                        raise CategoriaNull
            else:
                return True
        
        except CategoriaNull:
            return False
    
    def cadastrarCategoria(self, categoria):
        
        if self.validacaoCategoria(categoria) == True:
            
            # categoria = categoria.upper()
            
            try:  
                self.cursorDB.execute("INSERT INTO categoria (nome_categoria) VALUES (?)", (categoria,))                
                self.salvarTabela()
                
                return True, "Cadastro realizado com sucesso!"
            
            except sqlite3.IntegrityError:
                
                return False, "Categoria já existente!"
            
        else:
            return False, "nome_categoria não pode ser nulo!"
                

    def exibirCategorias(self):
        self.cursorDB.execute("SELECT * FROM categoria")
        categorias = self.cursorDB.fetchall()
            
        return categorias

    def pesquisarID(self, id_categoria_p):
        
        try:
            self.cursorDB.execute(f"SELECT * FROM categoria WHERE id_categoria = '{id_categoria_p}'")
            categorias = self.cursorDB.fetchall()
        
            return categorias
        
        except ValueError:
            pass
        
    def pesquisarCategoria(self, categoria_a):
        
        categoria_a = categoria_a.upper()
        
        self.cursorDB.execute(f"SELECT * FROM categoria WHERE nome_categoria = '{categoria_a}'")
        categorias = self.cursorDB.fetchall()
        
        return categorias

   
    def excluirTudo(self):
        self.cursorDB.execute("DELETE FROM categoria WHERE id_categoria > 0")
        self.salvarTabela()
        return "Todas categorias foram excluídas com sucesso!"

  
    def excluirID(self, id_e):
        try:
            id_e = int(id_e)
            self.cursorDB.execute("SELECT id_categoria FROM categoria WHERE id_categoria = ?", (id_e,))
            if self.cursorDB.fetchone() is not None:                                                                            
                self.cursorDB.execute("DELETE FROM categoria WHERE id_categoria = ?", (id_e,))
                self.salvarTabela()
                return f"Categoria com ID {id_e} excluída com sucesso!"
            else:
                return f"Nenhuma categoria com ID {id_e} encontrada."
            
        except ValueError:
            return "IDs são números inteiros!"
        

    def excluirCategoria(self, categoria_e):
        self.cursorDB.execute(f"SELECT nome_categoria FROM categoria WHERE nome_categoria LIKE '%{categoria_e}%'")
        if self.cursorDB.fetchone() is not None:
            categoria_e = categoria_e.upper()
            self.cursorDB.execute("DELETE FROM categoria WHERE nome_categoria LIKE ?", (categoria_e,))
            self.salvarTabela()
            return f"Categoria {categoria_e} excluída com sucesso!"
        else:
            return f"Nenhuma categoria {categoria_e} encontrada."
        
    
    def atualizarCategoria(self, id_categoria, nova_categoria=None):
    
        try:
            self.cursorDB.execute("SELECT * FROM categoria WHERE id_categoria = ?", (id_categoria,))
            if self.cursorDB.fetchone() is not None:
                consulta = "UPDATE categoria SET "
                valores = []
                
                if nova_categoria is not None and self.validacaoCategoria(nova_categoria) is True:
                    consulta += "nome_categoria = ?"
                    valores.append(nova_categoria.upper())

                    consulta += "WHERE id_categoria = ? "
                    valores.append(id_categoria)
                    
                    print(consulta, tuple(valores))
                    
                
                    self.cursorDB.execute(consulta, tuple(valores))
                    self.salvarTabela()
                    return True, "Categoria atualizada com sucesso!"
                
                else:
                    return False, "nome_categoria não pode ser nulo!"
            
        except sqlite3.Error as erro:
                return False, f"Erro ao atualizar categoria: {erro}!"
                    
        else:
            return False, f"ID Categoria não encontrado!"
    
    
    def salvarTabela(self):
        self.connectDB.commit()


class CategoriaNull(Exception):
    "nome_categoria não pode ser nulo!"


if __name__ == "__main__":
    data = "20/20/2000"