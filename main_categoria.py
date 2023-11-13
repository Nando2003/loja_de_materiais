from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import categoria
categoria = categoria.Categoria()

def categoriaMenu(root):

    janela = Toplevel(root)
    janela.title("CRUD DE CATEGORIA")
    janela.geometry("1000x650")
    janela.configure(bg="#e9edf5")
    janela.resizable(width=False, height=False)

    ############# FUNCTIONS #############

    def cadastrarC():
        categoria_c = e_categoria.get()
        
        if categoria_c:
            retorno = categoria.cadastrarCategoria(categoria_c)
            if retorno[0]:
                messagebox.showinfo("SUCESSO", retorno[1])
                e_categoria.delete(0,"end")
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(categoria.exibirCategorias())
            else:
                messagebox.showerror("ERRO", retorno[1])
        else:
            messagebox.showerror("ERRO", "PREECHA TODOS OS CAMPOS DE CADASTRO!")

    def pesquisarC():
        categoria_a = e_categoria_pesquisar.get()
        
        if categoria_a:
            retorno = categoria.pesquisarCategoria(categoria_a)
            
            e_categoria_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
            
            tree(retorno)
            
        else:
            messagebox.showerror("ERRO", "PREECHA Pesquisar Categoria!")
            
    def voltarPesquisar():
        retorno = categoria.exibirCategorias()
        
        for widget in frameTabela.winfo_children():
            widget.destroy()
            
        tree(retorno)
        
    def excluirTudo():
        
        if categoria.temCategoria() is False:
            messagebox.showinfo("AVISO", "NÃO HÁ CATEGORIAS CADASTRADOS!")
            
        else:
            resultado = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir tudo?")
            
            if resultado:
                messagebox.showinfo("Ação confirmada", "Todos os cadastros foram excluídos com sucesso!")
                categoria.excluirTudo()
                for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                tree(categoria.exibirCategorias())
            else:
                messagebox.showerror("Ação negada", "Não foi possível excluir tudo!")

    def excluirC():
        
        excluir = e_excluir.get()
        
        if excluir and categoria.temCategoria():
            excluir = excluir.strip()
            if excluirPor.get() == "ID":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir a categoria com ID {excluir}?")
                if resultado:
                    mensagem = categoria.excluirID(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(categoria.exibirCategorias())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
                    
            elif excluirPor.get() == "Categoria":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir a categoria {excluir}?")
                if resultado:
                    mensagem = categoria.excluirCategoria(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(categoria.exibirCategorias())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
        else:
            messagebox.showerror("Ação negada", f"Não foi possivel encontrar categoria!")
            
    def atualizarC():
        
        def atualizarBotao():
                    categoria_a = e_categoria_atualizar.get()
                    
                    if categoria_a:
                        mensagem = categoria.atualizarCategoria(categoria_v, nova_categoria=categoria_a)
                        e_categoria_atualizar.delete(0,"end")
                        e_categoria_verificar.delete(0,"end")
                    
                    if mensagem[0]:   
                        messagebox.showinfo("SUCESSO", mensagem[1])
                        
                        l_categoria_atualizar.destroy()
                        e_categoria_atualizar.destroy()
                        b_atualizar.destroy()
                        b_atualizar_voltar.destroy()
                        
                        for widget in frameTabela.winfo_children():
                            widget.destroy()

                        tree(categoria.exibirCategorias())              
                    else:
                        messagebox.showerror("ERRO", mensagem[1])
        
        def voltarAtualizar():
            
            e_categoria_verificar.delete(0,"end")
            
            for widget in frameTabela.winfo_children():
                widget.destroy()
                    
            tree(categoria.exibirCategorias())
                        
            l_categoria_atualizar.destroy()
            e_categoria_atualizar.destroy()
            b_atualizar.destroy()
            b_atualizar_voltar.destroy()
        
        categoria_v = e_categoria_verificar.get()

        if categoria_v:
            if categoria.temVerifica(categoria_v):
                messagebox.showinfo("SUCESSO", "CATEGORIA EXISTENTE!")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(categoria.pesquisarID(categoria_v))
                
                # CATEGORIA ATUALIZAR
                l_categoria_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Nome: ", bg="#feffff", fg="#403d3d", relief="flat")
                l_categoria_atualizar.place(x=10, y=400)
                e_categoria_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                e_categoria_atualizar.place(x=15, y=440)
                
                # Botão confirmar
                b_atualizar = Button(framePrincipal_direita, command=atualizarBotao, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="ATUALIZAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                b_atualizar.place(x=15, y=480)
                
                b_atualizar_voltar = Button(framePrincipal_direita, command=voltarAtualizar, width=10, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                b_atualizar_voltar.place(x=208, y=480)
                
            else:
                messagebox.showerror("ERRO", "CATEGORIA NÃO EXISTENTE!")
                
    ############# FRAME #############

    frameTitulo = Frame(janela,
                width=640,
                height=50,
                bg="#cf9bcc", 
                relief="flat"
                )

    framePrincipal = Frame(janela,
                width=640,
                height=600,
                bg="#feffff", 
                relief="flat"
                )

    framePrincipal_esquerda = Frame(framePrincipal,
                    width=320,
                    height=600,
                    bg="#feffff", 
                    relief="flat"
                    )

    framePrincipal_direita = Frame(framePrincipal,
                    width=320,
                    height=600,
                    bg="#feffff", 
                    relief="flat"
                    )

    frameTabela = Frame(janela,
                width=360,
                height=600,
                bg="#feffff", 
                relief="flat"
                )

    frameTitulo.grid(row=0,column=0)
    framePrincipal.grid(row=1,column=0)
    framePrincipal_esquerda.grid(row=0,column=0)
    framePrincipal_direita.grid(row=0,column=1)
    frameTabela.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

    ############# frameTitulo #############

    appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CRUD DE CATEGORIA", bg="#cf9bcc", fg="#feffff", relief="flat")
    appNome.place(x=210, y=11)

    ############# framePrincipal_esquerda #############

    #### CADASTRO ####

    l_cadastrarTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CADASTRO", bg="#feffff", fg="#cf9bcc", relief="flat")
    l_cadastrarTitulo.place(x=10, y=10)

    # CATEGORIA

    l_categoria = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Categoria*", bg="#feffff", fg="#403d3d", relief="flat")
    l_categoria.place(x=10, y=50)
    e_categoria = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_categoria.place(x=15, y=80)

    # CADASTRAR

    b_cadastrar = Button(framePrincipal_esquerda, command=cadastrarC, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="CADASTRAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cadastrar.place(x=15, y=120)

    #### EXCLUSÃO ####

    l_excluirTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="EXCLUSÃO", bg="#feffff", fg="#cf9bcc", relief="flat")
    l_excluirTitulo.place(x=10, y=240)

    l_excluir = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Excluir por:", bg="#feffff", fg="#403d3d", relief="flat")
    l_excluir.place(x=10, y=280)

    excluirPor = StringVar()
    excluirPor.set("ID")

    b_excluirID = Radiobutton(framePrincipal_esquerda, text="ID", font=("ARIAL 10 bold"), variable=excluirPor, value="ID",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirCategoria = Radiobutton(framePrincipal_esquerda, text="Categoria", font=("ARIAL 10 bold"), variable=excluirPor, value="Categoria",bg="#feffff", fg="#403d3d", relief="flat")

    b_excluirID.place(x=90, y=280)
    b_excluirCategoria.place(x=140, y=280)

    e_excluir = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_excluir.place(x=15,y=320)

    # EXCLUIR BOTAO
    b_excluir = Button(framePrincipal_esquerda, command=excluirC, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir.place(x=15, y=360)

    # EXCLUIR TUDO BOTAO
    b_excluir_tudo = Button(framePrincipal_esquerda, command=excluirTudo, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR TUDO", bg="#d07684", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir_tudo.place(x=15, y=400)

    ############# framePrincipal_esquerda #############

    #### PESQUISAR ####

    l_pesquisarTitulo = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="PESQUISA", bg="#feffff", fg="#cf9bcc", relief="flat")
    l_pesquisarTitulo.place(x=10, y=10)

    # PESQUISAR CATEGORIA

    l_categoria_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Categoria", bg="#feffff", fg="#403d3d", relief="flat")
    l_categoria_pesquisar.place(x=10, y=50)
    e_categoria_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_categoria_pesquisar.place(x=15, y=80)

    # PESQUISAR

    b_pesquisar = Button(framePrincipal_direita, command=pesquisarC, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=15, y=120)

    # VOLTAR

    b_pesquisar_voltar = Button(framePrincipal_direita, command=voltarPesquisar, width=10, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar_voltar.place(x=205, y=120)

    #### ATUALIZAR ####

    l_atualizarTitulo = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="ATUALIZAÇÃO", bg="#feffff", fg="#cf9bcc", relief="flat")
    l_atualizarTitulo.place(x=10, y=240)

    l_categoria_verificar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Verificar ID da categoria", bg="#feffff", fg="#403d3d", relief="flat")
    l_categoria_verificar.place(x=10, y=280)
        
    e_categoria_verificar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_categoria_verificar.place(x=15, y=320)

    b_categoria_verificar = Button(framePrincipal_direita, command=atualizarC, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VERIFICAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_categoria_verificar.place(x=15, y=360)

    ############# frameTabela #############

    def tree(clientes):
        
        tabelaColunas = ["ID_categoria","Categoria"]

        tabelaDF = clientes

        tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
        vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)

        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        frameTabela.grid_rowconfigure(0, weight=12)

        hd = ["center","center"]
        h =[88,250]
        n = 0

        for col in tabelaColunas:
            tree.heading(col, text=col, anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
                    
            n+=1

        for item in tabelaDF:
            tree.insert("", "end", values=item)

    tree(categoria.exibirCategorias())

    janela.mainloop()