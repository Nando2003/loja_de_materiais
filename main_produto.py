from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import produto
produto = produto.Produto()

def produtoMenu(root):

    janela = Toplevel(root)
    janela.title("CRUD DE CLIENTE")
    janela.geometry("1300x800")
    janela.configure(bg="#e9edf5")
    janela.resizable(width=False, height=False)

    ############# FUNCTIONS #############

    def cadastrarP():
        nome = e_nome.get()
        preco = e_preco_uni.get()
        quantidade = e_qtde_estoque.get()
        id_categoria = e_fk_id_categoria.get()

        if nome and preco and quantidade and id_categoria:
            retorno = produto.cadastrarProduto(nome,preco,quantidade,id_categoria)
            if retorno[0]:
                messagebox.showinfo("SUCESSO", retorno[1])
                e_nome.delete(0,"end")
                e_preco_uni.delete(0,"end")
                e_qtde_estoque.delete(0,"end")
                e_fk_id_categoria.delete(0,"end")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(produto.exibirProdutos())
            else:
                messagebox.showerror("ERRO", retorno[1])
        else:
            messagebox.showerror("ERRO", "PREECHA TODOS OS CAMPOS DE CADASTRO!")
            
    def pesquisarP():
        
        campos_pesquisa = {
            "nome_p": e_nome_pesquisar.get() or None,
            "preco_p": e_preco_pesquisar.get() or None,
            "quantidade_p": e_quantidade_pesquisar.get() or None,
            "categoria_p": e_categoria_pesquisar.get() or None
        }

        print(any(valor for valor in campos_pesquisa.values()))
        # se tudo for none = False / se pelo menos um campo não for none = True
        
        if any(valor for valor in campos_pesquisa.values()):
            
            mensagem = produto.pesquisar(**campos_pesquisa)
            if mensagem[0]:
                for widget in frameTabela.winfo_children():
                    widget.destroy()
                tree(mensagem[1])
            else:
                messagebox.showerror("ERRO", mensagem[1])

            e_nome_pesquisar.delete(0, "end")
            e_preco_pesquisar.delete(0, "end")
            e_quantidade_pesquisar.delete(0, "end")
            e_categoria_pesquisar.delete(0, "end")
        else:
            messagebox.showerror("ERRO", "Nenhum campo preenchido para pesquisa.")
            
    def excluirTudo():
        
        if produto.temProduto() is False:
            messagebox.showinfo("AVISO", "NÃO HÁ PRODUTOS CADASTRADOS!")
            
        else:
            resultado = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir tudo?")
            
            if resultado:
                messagebox.showinfo("Ação confirmada", "Todos os cadastros foram excluídos com sucesso!")
                produto.excluirTudo()
                for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                tree(produto.exibirProdutos())
            else:
                messagebox.showerror("Ação negada", "Não foi possível excluir tudo!")

    def voltarPesquisa():
        for widget in frameTabela.winfo_children():
            widget.destroy()
            
        tree(produto.exibirProdutos())
            
    def excluirProduto():
        
        excluir = e_excluir.get()
        
        if excluir and produto.temProduto():
            excluir = excluir.strip()
            if excluirPor.get() == "ID":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o produto com ID {excluir}?")
                if resultado:
                    mensagem = produto.excluirID(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(produto.exibirProdutos())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
                    
            elif excluirPor.get() == "Nome":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir os produtos com nome {excluir}?")
                if resultado:
                    mensagem = produto.excluirNome(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(produto.exibirProdutos())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
            
            elif excluirPor.get() == "Categoria":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o produto com ID_categoria {excluir}?")
                if resultado:
                    mensagem = produto.excluirCategoria(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(produto.exibirProdutos())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
        
        
    def verificarProduto():
            
            def atualizarBotao():
                        nome = e_nome_atualizar.get()
                        preco = e_preco_atualizar.get()
                        quantidade = e_quantidade_atualizar.get()
                        categoria = e_categoria_atualizar.get()
                        
                        if categoria:
                            mensagem = produto.atualizarProduto(id, fk_id_categoria=categoria)
                        
                        if nome:
                            mensagem = produto.atualizarProduto(id, novo_nome=nome)
                            
                        if preco:
                            mensagem = produto.atualizarProduto(id, novo_preco=preco)
                            
                        if quantidade:
                            mensagem = produto.atualizarProduto(id, nova_qtde=quantidade)
                                    
                        if mensagem[0]:
                            messagebox.showinfo("SUCESSO", mensagem[1])
                            e_nome_atualizar.delete(0,"end")
                            e_preco_atualizar.delete(0,"end")
                            e_quantidade_atualizar.delete(0,"end")
                            
                            for widget in frameTabela.winfo_children():
                                widget.destroy()
                        
                            tree(produto.exibirProdutos())
                            
                            l_nome_atualizar.destroy()
                            l_quantidade_atualizar.destroy()
                            l_preco_atualizar.destroy()
                            e_nome_atualizar.destroy()
                            e_quantidade_atualizar.destroy()
                            e_preco_atualizar.destroy()
                            l_categoria_atualizar.destroy()
                            e_categoria_atualizar.destroy()
                            b_atualizar.destroy()
                            b_atualizar_voltar.destroy()
                            e_ID_verificar.delete(0,"end")
                            
                        else:
                            messagebox.showerror("ERRO", mensagem[1])
            
            def voltarAtualizar():
                
                e_ID_verificar.delete(0,"end")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
                        
                tree(produto.exibirProdutos())
                            
                l_nome_atualizar.destroy()
                l_quantidade_atualizar.destroy()
                l_preco_atualizar.destroy()
                e_nome_atualizar.destroy()
                e_quantidade_atualizar.destroy()
                e_preco_atualizar.destroy()
                b_atualizar.destroy()
                b_atualizar_voltar.destroy()
                l_categoria_atualizar.destroy()
                e_categoria_atualizar.destroy()
            
            id = e_ID_verificar.get()

            if id:
                
                if produto.verificarID(id):
                    messagebox.showinfo("SUCESSO", "ID_PRODUTO EXISTENTE!")
                    
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
                    
                    resultado = produto.pesquisar(id_p=id)
                    
                    tree(resultado[1])
                    
                    # Nome
                    l_nome_atualizar = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Nome: ", bg="#feffff", fg="#403d3d", relief="flat")
                    l_nome_atualizar.place(x=10, y=550)
                    e_nome_atualizar = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
                    e_nome_atualizar.place(x=15, y=580)
                    
                    # Preco
                    l_preco_atualizar = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Preço", bg="#feffff", fg="#403d3d", relief="flat")
                    l_preco_atualizar.place(x=10, y=610)
                    e_preco_atualizar = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
                    e_preco_atualizar.place(x=15, y=640)
                    
                    # Quantidade
                    l_quantidade_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Quantidade em estoque", bg="#feffff", fg="#403d3d", relief="flat")
                    l_quantidade_atualizar.place(x=10, y=550)
                    e_quantidade_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_quantidade_atualizar.place(x=15, y=580)
                    
                    # Categoria
                    l_categoria_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar ID_categoria", bg="#feffff", fg="#403d3d", relief="flat")
                    l_categoria_atualizar.place(x=10, y=610)
                    e_categoria_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_categoria_atualizar.place(x=15, y=640)
                    
                    # Botão confirmar
                    b_atualizar = Button(framePrincipal_esquerda, command=atualizarBotao, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="ATUALIZAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar.place(x=15, y=680)
                    
                    b_atualizar_voltar = Button(framePrincipal_direita, command=voltarAtualizar, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar_voltar.place(x=15, y=680)
                    
                else:
                    messagebox.showerror("ERRO", "ID_PRODUTO NÃO EXISTENTE!")
                    
    ############# FRAME #############

    frameTitulo = Frame(janela,
                width=640,
                height=50,
                bg="#4fa882", 
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

    ############# frameTitulo #############

    appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CRUD DE PRODUTO", bg="#4fa882", fg="#feffff", relief="flat")
    appNome.place(x=210, y=11)

    ############# framePrincipal Esquerda #############

    #### CADASTRO ####

    l_cadastrarTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CADASTRO", bg="#feffff", fg="#4fa882", relief="flat")
    l_cadastrarTitulo.place(x=10, y=10)

    # NOME
    l_nome = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Nome*", bg="#feffff", fg="#403d3d", relief="flat")
    l_nome.place(x=10, y=50)
    e_nome = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_nome.place(x=15, y=80)

    # PRECO UNITARIO
    l_preco_uni = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Preço unitario*", bg="#feffff", fg="#403d3d", relief="flat")
    l_preco_uni.place(x=10, y=110)
    e_preco_uni = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_preco_uni.place(x=15, y=140)

    # QTDE ESTOQUE
    l_qtde_estoque = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Quantidade de estoque*", bg="#feffff", fg="#403d3d", relief="flat")
    l_qtde_estoque.place(x=10, y=170)
    e_qtde_estoque = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_qtde_estoque.place(x=15, y=200)

    # FK ID_CATEGORIA
    l_fk_id_categoria = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="ID Categoria*", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_categoria.place(x=10, y=230)
    e_fk_id_categoria = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_fk_id_categoria.place(x=15, y=260)

    # CADASTRAR
    b_cadastrar = Button(framePrincipal_esquerda, command=cadastrarP, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="CADASTRAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cadastrar.place(x=15, y=300)

    #### EXCLUSÃO ####

    l_excluirTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="EXCLUSÃO", bg="#feffff", fg="#4fa882", relief="flat")
    l_excluirTitulo.place(x=10, y=350)

    l_excluir = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Excluir por:", bg="#feffff", fg="#403d3d", relief="flat")
    l_excluir.place(x=10, y=390)

    excluirPor = StringVar()
    excluirPor.set("ID")

    b_excluirID = Radiobutton(framePrincipal_esquerda, text="ID", font=("ARIAL 10 bold"), variable=excluirPor, value="ID",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirNome = Radiobutton(framePrincipal_esquerda, text="Nome", font=("ARIAL 10 bold"), variable=excluirPor, value="Nome",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirCategoria = Radiobutton(framePrincipal_esquerda, text="Categoria", font=("ARIAL 10 bold"), variable=excluirPor, value="Categoria",bg="#feffff", fg="#403d3d", relief="flat")

    b_excluirID.place(x=90, y=390)
    b_excluirNome.place(x=135, y=390)
    b_excluirCategoria.place(x=205, y=390)

    e_excluir = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_excluir.place(x=15,y=420)

    # EXCLUIR BOTAO
    b_excluir = Button(framePrincipal_esquerda, command=excluirProduto, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir.place(x=15, y=450)

    # EXCLUIR TUDO BOTAO
    b_excluir_tudo = Button(framePrincipal_esquerda, command=excluirTudo, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR TUDO", bg="#d07684", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir_tudo.place(x=15, y=480)

    ############# framePrincipal Direita #############

    #### PESQUISAR ####

    l_pesquisarNome = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="PESQUISA", bg="#feffff", fg="#4fa882", relief="flat")
    l_pesquisarNome.place(x=10, y=10)

    # PESQUISAR NOME
    l_nome_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Nome", bg="#feffff", fg="#403d3d", relief="flat")
    l_nome_pesquisar.place(x=10, y=50)
    e_nome_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_nome_pesquisar.place(x=15, y=80)

    # PESQUISAR PRECO
    l_preco_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Preço", bg="#feffff", fg="#403d3d", relief="flat")
    l_preco_pesquisar.place(x=10, y=110)
    e_preco_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_preco_pesquisar.place(x=15, y=140)

    # PESQUISAR QUANTIDADE
    l_quantidade_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Quantidade", bg="#feffff", fg="#403d3d", relief="flat")
    l_quantidade_pesquisar.place(x=10, y=170)
    e_quantidade_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_quantidade_pesquisar.place(x=15, y=200)

    # PESQUISAR CATEGORIA
    l_categoria_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar ID Categoria", bg="#feffff", fg="#403d3d", relief="flat")
    l_categoria_pesquisar.place(x=10, y=230)
    e_categoria_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_categoria_pesquisar.place(x=15, y=260)

    # PESQUISAR
    b_pesquisar = Button(framePrincipal_direita, command=pesquisarP, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=15, y=300)

    # VOLTAR
    b_pesquisar = Button(framePrincipal_direita, command=voltarPesquisa, width=10, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=205, y=300)

    #### ATUALIZAR ####

    l_atualizarTitle = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="ATUALIZAÇÃO", bg="#feffff", fg="#4fa882", relief="flat")
    l_atualizarTitle.place(x=10, y=350)

    l_ID_verificar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Verificar ID", bg="#feffff", fg="#403d3d", relief="flat")
    l_ID_verificar.place(x=10, y=390)
        
    e_ID_verificar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_ID_verificar.place(x=15, y=420)

    b_ID_verificar = Button(framePrincipal_direita, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), command=verificarProduto, text="VERIFICAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_ID_verificar.place(x=15, y=450)

    def tree(clientes):
        
        tabelaColunas = ["ID_produto","Nome","Preço Unitario","Qtde em estoque","ID_categoria(fk)"]

        tabelaDF = clientes

        tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
        vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)

        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        frameTabela.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center", "center"]
        h =[100,165,135,135,100]
        n = 0

        for col in tabelaColunas:
            tree.heading(col, text=col, anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
                    
            n+=1

        for item in tabelaDF:
            tree.insert("", "end", values=item)

    tree(produto.exibirProdutos())

    janela.mainloop()