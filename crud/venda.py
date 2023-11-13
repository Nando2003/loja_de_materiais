import sqlite3
from datetime import date

class Venda:
    
    
    def __init__(self):
        self.connectDB = sqlite3.connect("./BANCO/loja_construcao.db")
        self.cursorDB = self.connectDB.cursor()
        self.criarTabela()
        
        
    def criarTabela(self):
        self.cursorDB.execute("""
        CREATE TABLE IF NOT EXISTS venda(
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda DATE NOT NULL,
        valor_total DOUBLE NOT NULL,
        fk_id_cliente INTEGER,
        FOREIGN KEY(fk_id_cliente) REFERENCES cliente(id_cliente)
        );
        """)
        
        self.salvarTabela()
    
    
    def verificarID(self, id_v):
        self.cursorDB.execute("SELECT * FROM venda WHERE id_venda = ?", (id_v,))
        if self.cursorDB.fetchone():
            return True
        else:
            return False

    def temVenda(self):
        self.cursorDB.execute("SELECT * FROM venda")
        if self.cursorDB.fetchone():
            return True
        else:
            return False    
    
    
    def cadastrarVenda(self, data_venda, valor_total, fk_id_cliente):
        
        try:
            valor_total = float(valor_total)
            fk_id_cliente = int(fk_id_cliente)
            
            self.cursorDB.execute("INSERT INTO venda (data_venda, valor_total, fk_id_cliente) VALUES (?,?,?)",
                                (data_venda, valor_total,fk_id_cliente))
            
            self.salvarTabela()
            
            return True, "Venda cadastrada com sucesso!"
    
        except ValueError:
            return False, "Os preços são número reais e o id cliente é inteiro!"
 
 
    def exibirTudo(self):
        
        self.cursorDB.execute("SELECT * FROM venda")
        vendas = self.cursorDB.fetchall()
        
        if vendas is not None:
            return vendas

    def pesquisarID(self, id_p=None):
        self.cursorDB.execute("SELECT * FROM venda WHERE id_venda = ?", (id_p,))
        resultado = self.cursorDB.fetchall()
        
        if resultado:
            return True, resultado
        else:
            return False, []
    
    def pesquisar(self, ano_p=None, mes_p=None, dia_p=None, valor_p=None, fk_id_cliente_p=None):

        if ano_p or mes_p or dia_p or valor_p or fk_id_cliente_p:
            consulta = "SELECT * FROM venda WHERE "
            valores = []
            
            if dia_p is not None:
                if len(dia_p) == 1:
                    dia_p = "0" + dia_p
                    
                consulta += f"data_venda LIKE ?"
                valores.append(str("%-" + dia_p))
                
            if mes_p is not None:
                if len(mes_p) == 1:
                    mes_p = "0" + mes_p
                    
                if dia_p is not None:
                    consulta += " AND "
                consulta += f"data_venda LIKE ?"
                valores.append(str("%-" + mes_p + "-%"))
                
            if ano_p is not None:
                if dia_p is not None or mes_p is not None:
                    consulta += " AND "
                consulta += f"data_venda LIKE ?"
                valores.append(str(ano_p + "-%"))
            
            if valor_p is not None:
                if dia_p is not None or mes_p is not None or ano_p is not None:
                    consulta += " AND "
                consulta += f"valor_total = ?"
                valores.append(valor_p)
                
            if fk_id_cliente_p is not None:
                if dia_p is not None or mes_p is not None or ano_p is not None or valor_p is not None:
                    consulta += " AND "
                consulta += "fk_id_cliente = ?"
                valores.append(fk_id_cliente_p)
                
            try:
                self.cursorDB.execute(consulta, tuple(valores))
                
                query = self.cursorDB.fetchall()
                print(query)
                print(query is None)
                
                if len(query) != 0:
                    return True, query
                else:
                    return True, self.exibirTudo() 
            
            except sqlite3.Error as erro:
                return False, f"Erro ao pesquisar produto: {erro}"
    
    def excluirTudo(self):
        
        self.cursorDB.execute("DELETE FROM venda WHERE id_venda > 0")
        self.salvarTabela()
        return "Todas as vendas foram excluídas com sucesso!"
        
    def excluirID(self, id_e):
        
        try:
            id_e = int(id_e)
            self.cursorDB.execute("SELECT id_venda FROM venda WHERE id_venda = ?", (id_e,))
            if self.cursorDB.fetchone() is not None:                                                                            
                self.cursorDB.execute("DELETE FROM venda WHERE id_venda = ?", (id_e,))  
                self.salvarTabela()
                return f"Venda com ID {id_e} excluída com sucesso!"
            else:
                return f"Nenhuma Venda com ID {id_e} encontrada."
            
        except ValueError:
            return "IDs são números inteiros!"
    
    def excluirData(self, data_venda_e):
        self.cursorDB.execute("SELECT data_venda FROM venda WHERE data_venda = ?", (data_venda_e,))
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute("DELETE FROM venda WHERE data_venda = ?", (data_venda_e,))
            self.salvarTabela()
            return f"Venda com data {data_venda_e} excluído com sucesso!"
        else:
            return f"Nenhum Venda com data {data_venda_e} encontrado."
    
    def excluirValor(self, valor_e):
        self.cursorDB.execute("SELECT valor_total FROM venda WHERE valor_total = ?", (valor_e,))
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute("DELETE FROM venda WHERE valor_total = ?", (valor_e,))
            self.salvarTabela()
            return f"Venda com valor {valor_e} excluído com sucesso!"
        else:
            return f"Nenhum venda com valor {valor_e} encontrado."
        
    def atualizarVenda(self, id, nova_data_venda=None, nova_valor_total=None, nova_fk_id_cliente=None):
        self.cursorDB.execute("SELECT id_venda FROM venda WHERE id_venda = ?", (id,))
        if self.cursorDB.fetchone() is not None:
            consulta = "UPDATE venda SET "
            valores = []
            
            try:
                if nova_data_venda is not None:
                    dia, mes, ano = nova_data_venda.split("/")
                    nova_data_venda = date(int(ano),int(mes),int(dia))
                    nova_data_venda = str(nova_data_venda)
                    consulta += "data_venda = ?,"
                    valores.append(nova_data_venda)
                    
                if nova_valor_total is not None:
                    nova_valor_total = float(nova_valor_total)
                    consulta += "valor_total = ?,"
                    valores.append(nova_valor_total)
                    
                if nova_fk_id_cliente is not None:
                    nova_fk_id_cliente = int(nova_fk_id_cliente)
                    consulta += "fk_id_cliente = ?,"
                    valores.append(nova_fk_id_cliente)
                    
                consulta = consulta.rstrip(",")
                consulta += "WHERE id_venda = ?"
                valores.append(id)

                print(consulta, tuple(valores))
                
                self.cursorDB.execute(consulta, tuple(valores))
                self.salvarTabela()
                return True, "Venda atualizado com sucesso!"
                    
            except sqlite3.Error as erro:
                
                return False, f"Erro ao atualizar venda: {erro}"
            
            except ValueError as erro:
                
                return False, f"Erro ao atualizar venda: {erro}"
            
        else:
            return False, f"Venda com o ID {id} não encontrada!"
            
        
    def validacao(self, data_venda=None, valor_total=None):
        
        if data_venda is not None:
            if type(data_venda) is date:
                return True
            
            else:
                return False
        
        if valor_total is not None:
            if type(valor_total) is int or type(valor_total) is float:
                return True
            
            else:
                return False 

    def salvarTabela(self):
        self.connectDB.commit()
    
        
if __name__ == "__main__":
    print(Venda().pesquisar(dia_p="2"))
    
    
    