from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import venda_produto
venda_produto = venda_produto.Venda_produto()

def venda_produtoMenu(root):

    janela = Toplevel(root)
    janela.title("CRUD DE VENDA-PRODUTO")
    janela.geometry("1300x800")
    janela.configure(bg="#e9edf5")
    janela.resizable(width=False, height=False)

    def cadastrarVP():
        
        fk_id_venda = e_fk_id_venda.get()
        fk_id_produto = e_fk_id_produto.get()
        qtde_venda = e_qtde_venda.get()

        if fk_id_venda and fk_id_produto and qtde_venda:

            fk_id_produto.strip()
            fk_id_venda.strip()
            qtde_venda.strip()

            retorno = venda_produto.cadastrarVenda_produto(fk_id_produto=fk_id_produto, fk_id_venda=fk_id_venda, qtde_venda=qtde_venda)

            if retorno[0]:
                messagebox.showinfo("SUCESSO", retorno[1])
                e_fk_id_produto.delete(0,"end")
                e_fk_id_venda.delete(0,"end")
                e_qtde_venda.delete(0,"end")
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(venda_produto.exibirVenda_produto())
            else:
                messagebox.showerror("ERRO", retorno[1])
        else:
            messagebox.showerror("ERRO", "PREECHA TODOS OS CAMPOS DE CADASTRO!")

    def pesquisarDP():
        
        campos_pesquisa = {
            "id_venda_produto": e_id_venda_produto_pesquisar.get() or None,
            "qtde_venda": e_quantidade_pesquisar.get() or None,
            "preco_venda": e_preco_pesquisar.get() or None,
            "fk_id_venda": e_fk_id_venda_pesquisar.get() or None,
            "fk_id_produto": e_fk_id_produto_pesquisar.get() or None
        }

        print(any(valor for valor in campos_pesquisa.values()))
        # se tudo for none = False / se pelo menos um campo não for none = True
        
        if any(valor for valor in campos_pesquisa.values()):
            
            mensagem = venda_produto.pesquisar(**campos_pesquisa)
            if mensagem[0]:
                if len(mensagem[1]) == 0:
                    messagebox.showerror("ERRO", "Nada encontrado!")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda_produto.exibirVenda_produto()) 
                else:
                    
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
                    tree(mensagem[1])
                    
            else:
                messagebox.showerror("ERRO", mensagem[1])
                
            e_id_venda_produto_pesquisar.delete(0, "end")
            e_quantidade_pesquisar.delete(0, "end")
            e_preco_pesquisar.delete(0, "end")
            e_fk_id_venda_pesquisar.delete(0, "end")
            e_fk_id_produto_pesquisar.delete(0, "end")
        else:
            messagebox.showerror("ERRO", "Nenhum campo preenchido para pesquisa.")
            
    def voltarPesquisa():
        for widget in frameTabela.winfo_children():
                    widget.destroy()    
            
        tree(venda_produto.exibirVenda_produto())

    def excluirDP():
        
        excluir = e_excluir.get()
        
        if excluir:
            excluir = excluir.strip()
            if excluirPorVP.get() == "ID":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o venda_produto com ID {excluir}?")
                if resultado:
                    mensagem = venda_produto.excluirID(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda_produto.exibirVenda_produto())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
                    
            elif excluirPorVP.get() == "Venda":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o venda_produto com ID Venda {excluir}?")
                if resultado:
                    mensagem = venda_produto.excluirFK_id_venda(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda_produto.exibirVenda_produto())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
            
            elif excluirPorVP.get() == "Produto":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o venda_produto com ID Produto {excluir}?")
                if resultado:
                    mensagem = venda_produto.excluirFK_id_produto(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda_produto.exibirVenda_produto())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")

    def excluirTudo():
        
        if venda_produto.temVenda_produto() is False:
            messagebox.showinfo("AVISO", "NÃO HÁ VENDA_PRODUTO CADASTRADOS!")
            
        else:
            resultado = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir tudo?")
            
            if resultado:
                messagebox.showinfo("Ação confirmada", "Todos os cadastros foram excluídos com sucesso!")
                venda_produto.excluirTudo()
                for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                tree(venda_produto.exibirVenda_produto())
            else:
                messagebox.showerror("Ação negada", "Não foi possível excluir tudo!")

    def verificarVenda_produto():
            
            def atualizarBotao():
                        fk_id_produto = e_fk_id_produto_atualizar.get()
                        fk_id_venda = e_fk_id_venda_atualizar.get()
                        qtde_venda = e_qtde_venda_atualizar.get()
                        
                        if qtde_venda and not(fk_id_produto) and not(fk_id_venda) :
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_qtde=qtde_venda)
                            
                        elif fk_id_produto and not(qtde_venda) and not(fk_id_venda):
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_produto=fk_id_produto)
                        
                        elif fk_id_venda and not(qtde_venda) and not(fk_id_produto):
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_venda=fk_id_venda)
                        
                        elif fk_id_venda and qtde_venda and not(fk_id_produto):
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_venda=fk_id_venda, nova_qtde=qtde_venda)
                            
                        elif fk_id_venda and not(qtde_venda) and fk_id_produto:
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_venda=fk_id_venda, nova_fk_id_produto=fk_id_produto)
                            
                        elif not(fk_id_venda) and qtde_venda and fk_id_produto:
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_produto=fk_id_produto, nova_qtde=qtde_venda)
                            
                        elif fk_id_venda and qtde_venda and fk_id_produto:
                            mensagem = venda_produto.atualizarVenda_produto(id, nova_fk_id_venda=fk_id_venda, nova_fk_id_produto=fk_id_produto, nova_qtde=qtde_venda) 
                        
                        
                        if mensagem[0]:
                            messagebox.showinfo("SUCESSO", mensagem[1])
                            e_fk_id_produto_atualizar.delete(0,"end")
                            e_fk_id_venda_atualizar.delete(0,"end")
                            e_qtde_venda_atualizar.delete(0,"end")
                            
                            for widget in frameTabela.winfo_children():
                                widget.destroy()
                        
                            tree(venda_produto.exibirVenda_produto())
                            
                            l_fk_id_produto_atualizar.destroy()
                            e_fk_id_produto_atualizar.destroy()
                            l_fk_id_venda_atualizar.destroy()
                            e_fk_id_venda_atualizar.destroy()
                            l_qtde_venda_atualizar.destroy()
                            e_qtde_venda_atualizar.destroy()
                            b_atualizar.destroy()
                            b_atualizar_voltar.destroy()
                            b_atualizar_voltar.destroy()
                            e_ID_verificar.delete(0,"end")
                            
                        else:
                            messagebox.showerror("ERRO", mensagem[1])
            
            def voltarAtualizar():
                
                e_ID_verificar.delete(0,"end")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
                        
                tree(venda_produto.exibirVenda_produto())
                            
                l_fk_id_produto_atualizar.destroy()
                e_fk_id_produto_atualizar.destroy()
                l_fk_id_venda_atualizar.destroy()
                e_fk_id_venda_atualizar.destroy()
                l_qtde_venda_atualizar.destroy()
                e_qtde_venda_atualizar.destroy()
                b_atualizar.destroy()
                b_atualizar_voltar.destroy()
            
            id = e_ID_verificar.get()

            if id:
                
                if venda_produto.verificarID(id):
                    messagebox.showinfo("SUCESSO", "ID VENDA_PRODUTO EXISTE!")
                    
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
                    
                    resultado = venda_produto.pesquisar(id_venda_produto=id)
                    
                    tree(resultado[1])
                    
                    # FK_PRODUTO
                    l_fk_id_produto_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Produto", bg="#feffff", fg="#403d3d", relief="flat")
                    l_fk_id_produto_atualizar.place(x=10, y=420)
                    e_fk_id_produto_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_fk_id_produto_atualizar.place(x=15, y=450)
                    
                    # FK_VENDA
                    l_fk_id_venda_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Venda", bg="#feffff", fg="#403d3d", relief="flat")
                    l_fk_id_venda_atualizar.place(x=10, y=480)
                    e_fk_id_venda_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_fk_id_venda_atualizar.place(x=15, y=510)
                    
                    # QUANTIDADE
                    l_qtde_venda_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Quantidade: ", bg="#feffff", fg="#403d3d", relief="flat")
                    l_qtde_venda_atualizar.place(x=10, y=540)
                    e_qtde_venda_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_qtde_venda_atualizar.place(x=15, y=570)
                    
                    # Botão confirmar
                    b_atualizar = Button(framePrincipal_direita, command=atualizarBotao, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="ATUALIZAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar.place(x=15, y=600)
                    
                    b_atualizar_voltar = Button(framePrincipal_direita, command=voltarAtualizar, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar_voltar.place(x=15, y=630)
                    
                else:
                    messagebox.showerror("ERRO", "ID VENDA_PRODUTO NÃO EXISTE!")

    ############# FRAME #############

    frameTitulo = Frame(janela,
                width=640,
                height=50,
                bg="#20b2aa", 
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

    appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CRUD DE VENDA-PRODUTO", bg="#20b2aa", fg="#feffff", relief="flat")
    appNome.place(x=180, y=11)

    ############# framePrincipal Esquerda #############

    #### CADASTRO ####

    l_cadastrarTitle = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CADASTRO", bg="#feffff", fg="#20b2aa", relief="flat")
    l_cadastrarTitle.place(x=10, y=10)

    # ID_PRODUTO
    l_fk_id_produto = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="ID Produto*", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_produto.place(x=10, y=50)
    e_fk_id_produto = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_fk_id_produto.place(x=15, y=80)

    # ID_VENDA
    l_fk_id_venda = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="ID Venda*", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_venda.place(x=10, y=110)
    e_fk_id_venda = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_fk_id_venda.place(x=15, y=140)

    # QUANTIDADE DE PRODUTOS VENDIDOS
    l_qtde_venda = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Quantidade da venda*", bg="#feffff", fg="#403d3d", relief="flat")
    l_qtde_venda.place(x=10, y=170)
    e_qtde_venda = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_qtde_venda.place(x=15, y=200)

    # CADASTRAR
    b_cadastrar = Button(framePrincipal_esquerda, command=cadastrarVP, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="CADASTRAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cadastrar.place(x=15, y=240)

    #### EXCLUSÃO ####

    l_excluirTitle = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="EXCLUSÃO", bg="#feffff", fg="#20b2aa", relief="flat")
    l_excluirTitle.place(x=10, y=300)

    l_excluir = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Excluir por:", bg="#feffff", fg="#403d3d", relief="flat")
    l_excluir.place(x=10, y=340)

    excluirPorVP = StringVar()
    excluirPorVP.set("ID")

    b_excluirID = Radiobutton(framePrincipal_esquerda, text="ID", font=("ARIAL 10 bold"), variable=excluirPorVP, value="ID",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirNome = Radiobutton(framePrincipal_esquerda, text="Venda", font=("ARIAL 10 bold"), variable=excluirPorVP, value="Venda",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirCategoria = Radiobutton(framePrincipal_esquerda, text="Produto", font=("ARIAL 10 bold"), variable=excluirPorVP, value="Produto",bg="#feffff", fg="#403d3d", relief="flat")

    b_excluirID.place(x=90, y=340)
    b_excluirNome.place(x=135, y=340)
    b_excluirCategoria.place(x=205, y=340)

    e_excluir = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_excluir.place(x=15,y=370)

    # EXCLUIR BOTAO
    b_excluir = Button(framePrincipal_esquerda, command=excluirDP, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir.place(x=15, y=400)

    # EXCLUIR TUDO BOTAO
    b_excluir_tudo = Button(framePrincipal_esquerda, command=excluirTudo, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR TUDO", bg="#d07684", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir_tudo.place(x=15, y=440)

    #### ATUALIZAR ####

    l_atualizarTitle = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="ATUALIZAÇÃO", bg="#feffff", fg="#20b2aa", relief="flat")
    l_atualizarTitle.place(x=10, y=500)

    l_ID_verificar = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Verificar ID Venda_produto", bg="#feffff", fg="#403d3d", relief="flat")
    l_ID_verificar.place(x=10, y=540)
        
    e_ID_verificar = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_ID_verificar.place(x=15, y=570)

    b_ID_verificar = Button(framePrincipal_esquerda, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), command=verificarVenda_produto, text="VERIFICAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_ID_verificar.place(x=15, y=600)

    ############# framePrincipal Direita #############

    #### PESQUISAR ####

    l_pesquisarTitle= Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="PESQUISA", bg="#feffff", fg="#20b2aa", relief="flat")
    l_pesquisarTitle.place(x=10, y=10)

    # PESQUISAR ID_VENDA_PRODUTO
    l_id_venda_produto_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Venda_produto", bg="#feffff", fg="#403d3d", relief="flat")
    l_id_venda_produto_pesquisar.place(x=10, y=50)
    e_id_venda_produto_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_id_venda_produto_pesquisar.place(x=15, y=80)

    # PESQUISAR ID_PRODUTO
    l_fk_id_produto_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Produto", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_produto_pesquisar.place(x=10, y=110)
    e_fk_id_produto_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_fk_id_produto_pesquisar.place(x=15, y=140)

    # PESQUISAR ID_VENDA
    l_fk_id_venda_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Venda", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_venda_pesquisar.place(x=10, y=170)
    e_fk_id_venda_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_fk_id_venda_pesquisar.place(x=15, y=200)

    # PESQUISAR QUANTIDADE
    l_quantidade_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Quantidade", bg="#feffff", fg="#403d3d", relief="flat")
    l_quantidade_pesquisar.place(x=10, y=230)
    e_quantidade_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_quantidade_pesquisar.place(x=15, y=260)

    # PESQUISAR PREÇO
    l_preco_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Preço", bg="#feffff", fg="#403d3d", relief="flat")
    l_preco_pesquisar.place(x=10, y=290)
    e_preco_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_preco_pesquisar.place(x=15, y=320)

    # PESQUISAR
    b_pesquisar = Button(framePrincipal_direita, command=pesquisarDP, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=15, y=360)

    # VOLTAR
    b_pesquisar = Button(framePrincipal_direita, command=voltarPesquisa, width=10, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=205, y=360)



    ############# Tree #############

    def tree(clientes):
        
        tabelaColunas = ["ID Venda_produto","Quantidade de produto","Preço da venda","ID Venda","ID Produto"]

        tabelaDF = clientes

        tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
        vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)

        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        frameTabela.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center", "center"]
        h =[110,165,165,100,100]
        n = 0

        for col in tabelaColunas:
            tree.heading(col, text=col, anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
                    
            n+=1

        for item in tabelaDF:
            tree.insert("", "end", values=item)

    tree(venda_produto.exibirVenda_produto())


    janela.mainloop()