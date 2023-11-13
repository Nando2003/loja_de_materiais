import sqlite3
import string as s

class Cliente:


    def __init__(self):
        self.connectDB = sqlite3.connect("./BANCO/loja_construcao.db")
        self.cursorDB = self.connectDB.cursor()
        self.criarTabela()

  
    def criarTabela(self):
        self.cursorDB.execute("""
        CREATE TABLE IF NOT EXISTS cliente(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTEGER NOT NULL UNIQUE,
        endereco TEXT NOT NULL
        );
        """)

        self.salvarTabela()

    def temClientes(self):
        self.cursorDB.execute("SELECT COUNT(*) FROM cliente")
        resultado = self.cursorDB.fetchone()
        
        if resultado[0] == 0:
            return False
        else:
            return True 
    
    
    def verificarCPF(self, cpf_v):
        self.cursorDB.execute("SELECT cpf FROM cliente WHERE cpf = ?", (cpf_v,))
        if self.cursorDB.fetchone() is not None:
            return True
        else:
            return False
        

    def cadastrarCliente(self, nome, cpf, endereco):
        
        nome_hasNumber = False
        cpf_hasLetter = False
        
        for caractere in nome:
            if caractere in list(s.digits):
                nome_hasNumber = True
                break
        
        for caracteres in cpf:
            print(caracteres)
            if caracteres in list(s.ascii_letters):
                cpf_hasLetter = True
                break
        
        
        if nome_hasNumber == True:
            return False, "NOME NÃO DEVE TER NÚMERO"
        elif cpf_hasLetter or len(cpf) != 11:
            return False, "CPF TEM QUE TER 11 NÚMEROS E NENHUMA LETRA"
        elif len(cpf) == 11:
            try:
                self.cursorDB.execute("INSERT INTO cliente (nome, cpf, endereco) VALUES (?,?,?)",
                                    (nome, cpf, endereco))
            
                self.salvarTabela()
                return True, "CLIENTE CADASTRADO COM SUCESSO!"
            
            except sqlite3.IntegrityError:
                return False, "CPF JÁ CADASTRADO!"


    def exibirClientes(self):
        self.cursorDB.execute("SELECT * FROM cliente")
        clientes = self.cursorDB.fetchall()
    
        return clientes

           
    def pesquisarNome(self, nome_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE nome LIKE '%{nome_p}%'")
        clientes = self.cursorDB.fetchall()
    
        return clientes
    

    def pesquisarCPF(self, cpf_p):
        self.cursorDB.execute("SELECT * FROM cliente WHERE cpf = ?", (cpf_p,))
        clientes = self.cursorDB.fetchall()
        
        return clientes
    
    
    def pesquisarEndereco(self, endereco_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE endereco LIKE '%{endereco_p}%'")
        clientes = self.cursorDB.fetchall()

        return clientes    
    
    
    def pesquisarNomeCPF(self, nome_p,cpf_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE nome LIKE '%{nome_p}%' AND cpf = {cpf_p}")
        clientes = self.cursorDB.fetchall()
    
        return clientes


    def pesquisarNomeEndereco(self, nome_p,endereco_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE nome LIKE '%{nome_p}%' AND endereco LIKE '%{endereco_p}%'")
        clientes = self.cursorDB.fetchall()
    
        return clientes
    
    
    def pesquisarCPFEndereco(self, cpf_p, endereco_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE endereco LIKE '%{endereco_p}%' AND cpf = {cpf_p}")
        clientes = self.cursorDB.fetchall()
    
        return clientes
    
    
    def pesquisarTudo(self, nome_p, cpf_p, endereco_p):
        self.cursorDB.execute(f"SELECT * FROM cliente WHERE nome LIKE '%{nome_p}%' AND cpf = {cpf_p} AND endereco LIKE '%{endereco_p}%'")
        clientes = self.cursorDB.fetchall()

        return clientes
    

    def excluirTudo(self):
        self.cursorDB.execute("DELETE FROM cliente WHERE id_cliente > 0")
        self.salvarTabela()
        return "Clientes excluídos com sucesso!"
    

    def excluirID(self, id_e):
        try:
            id_e = int(id_e)
            self.cursorDB.execute(f"SELECT id_cliente FROM cliente WHERE id_cliente = {id_e}")
            if self.cursorDB.fetchone() is not None:
                self.cursorDB.execute(f"DELETE FROM cliente WHERE id_cliente = {id_e}")
                self.salvarTabela()
                return f"Cliente com ID {id_e} excluído com sucesso!"
            else:
                return f"Nenhum cliente com ID {id_e} encontrado."
            
        except ValueError:
            return "IDs são números inteiros!"


    def excluirNome(self, nome_e):
        self.cursorDB.execute("SELECT nome FROM cliente WHERE nome LIKE ?", (nome_e,))
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute("DELETE FROM cliente WHERE nome LIKE ?", (nome_e,))
            self.salvarTabela()
            return f"Cliente com NOME {nome_e} excluído com sucesso!"
        else:
            return f"Nenhum cliente com NOME {nome_e} encontrado."


    def excluirCPF(self, cpf_e):
        self.cursorDB.execute("SELECT cpf FROM cliente WHERE cpf = ?", (cpf_e,))
        if self.cursorDB.fetchone() is not None:
            self.cursorDB.execute("DELETE FROM cliente WHERE cpf = ?", (cpf_e,))
            self.salvarTabela()
            return f"Cliente com CPF {cpf_e} excluído com sucesso!"
        else:
            return f"Nenhum cliente com CPF {cpf_e} encontrado."
        
        
    def atualizarCliente(self, id_cliente, novo_nome=None, novo_cpf=None, novo_endereco=None):     
        self.cursorDB.execute("SELECT * FROM cliente WHERE id_cliente = ?", (id_cliente,))
        if self.cursorDB.fetchone() is not None:
            nome_hasNumber = False
            cpf_hasLetter = False
            cpfNaoTem = False
            
            if novo_nome is not None:
                for caractere in novo_nome:
                    if caractere in list(s.digits):
                        nome_hasNumber = True
                        break
            
            if novo_cpf is not None:
                for caracteres in novo_cpf:
                    if caracteres in list(s.ascii_letters):
                        cpf_hasLetter = True
                        break
                
                if len(novo_cpf) != 11:
                    cpfNaoTem = True
            
            if nome_hasNumber:
                return False, "Nome com número!"
                 
            elif cpf_hasLetter or cpfNaoTem:
                return False, "CPF com letra ou sem 11 números!"
            
            else:
                consulta = "UPDATE cliente SET "
                valores = []
                if novo_nome is not None:
                    consulta += "nome = ?,"
                    valores.append(novo_nome)
                    
                if novo_cpf is not None:
                    consulta += "cpf = ?,"
                    valores.append(novo_cpf)
                    
                if novo_endereco is not None:
                    consulta += "endereco = ?,"
                    valores.append(novo_endereco)
                    
                consulta = consulta.rstrip(",")
                consulta += "WHERE id_cliente = ?"
                valores.append(id_cliente)
                
                print(consulta, tuple(valores))
                
                try:
                    self.cursorDB.execute(consulta, tuple(valores))
                    self.salvarTabela()
                    return True, "Cliente atualizado com sucesso!"
                    
                except sqlite3.Error as erro:
                    return False, f"Erro ao atualizar cliente: {erro}"
                    
        else:
            return False, f"Cliente com o ID {id_cliente} não encontrado!"

    def salvarTabela(self):
        self.connectDB.commit()
    
if __name__ == "__main__":
    Cliente()