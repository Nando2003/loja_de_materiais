from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import cliente
cliente = cliente.Cliente()


def clienteMenu(root):
    
    janela = Toplevel(root)
    janela.title("CRUD DE CLIENTE")
    janela.geometry("1300x800")
    janela.configure(bg="#e9edf5")
    janela.resizable(width=False, height=False)

    ############# FUNCTIONS #############

    def cadastrarCliente():
        nome = e_nome.get()
        cpf = e_cpf.get()
        endereco = e_endereco.get()

        if nome and cpf and endereco:
            retorno = cliente.cadastrarCliente(nome,cpf,endereco)
            if retorno[0]:
                messagebox.showinfo("SUCESSO", retorno[1])
                e_nome.delete(0,"end")
                e_cpf.delete(0,"end")
                e_endereco.delete(0,"end")
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(cliente.exibirClientes())
            else:
                messagebox.showerror("ERRO", retorno[1])
        else:
            messagebox.showerror("ERRO", "PREECHA TODOS OS CAMPOS DE CADASTRO!")

    def pesquisarCliente():
        nome = e_nome_pesquisar.get()
        cpf = e_cpf_pesquisar.get()
        endereco = e_endereco_pesquisar.get()
        
        if nome and not(cpf) and not(endereco):
            resultado1 = cliente.pesquisarNome(nome)
            e_nome_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
            
            tree(resultado1)
            
        elif cpf and not(nome) and not(endereco):
            resultado2 = cliente.pesquisarCPF(cpf)
            e_cpf_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
            
            tree(resultado2)
            
        elif endereco and not(nome) and not(cpf):
            resultado7 = cliente.pesquisarEndereco(endereco)
            e_endereco_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
            
            tree(resultado7)
            
        elif nome and (cpf) and not(endereco):
            resultado3 = cliente.pesquisarNomeCPF(nome,cpf)
            e_cpf_pesquisar.delete(0,"end")
            e_nome_pesquisar.delete(0,"end")
            e_endereco_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
            
            tree(resultado3)
            
        elif nome and endereco and not(cpf):
            resultado4 = cliente.pesquisarNomeEndereco(nome,endereco)
            e_cpf_pesquisar.delete(0,"end")
            e_nome_pesquisar.delete(0,"end")
            e_endereco_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
                
            tree(resultado4)
            
        elif cpf and endereco and not(nome):
            resultado5 = cliente.pesquisarCPFEndereco(cpf,endereco)
            e_cpf_pesquisar.delete(0,"end")
            e_nome_pesquisar.delete(0,"end")
            e_endereco_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
                
            tree(resultado5)
                
        elif nome and cpf and endereco:
            resultado6 = cliente.pesquisarTudo(nome,cpf,endereco)
            e_cpf_pesquisar.delete(0,"end")
            e_nome_pesquisar.delete(0,"end")
            e_endereco_pesquisar.delete(0,"end")
            for widget in frameTabela.winfo_children():
                widget.destroy()
                
            tree(resultado6)
            
        else:
            pass

    def voltarExibir():
        
        resultado4 = cliente.exibirClientes()
        for widget in frameTabela.winfo_children():
            widget.destroy()
            
        tree(resultado4)

    def verificarCliente():
        
        def atualizarBotao():
                    nome = e_nome_atualizar.get()
                    cpf_a = e_cpf_atualizar.get()
                    endereco = e_endereco_atualizar.get()
                    
                    if nome:
                        mensagem = cliente.atualizarCliente(cpf, novo_nome=nome)
                        e_nome_atualizar.delete(0,"end")
                        
                    if endereco:
                        mensagem = cliente.atualizarCliente(cpf, novo_endereco=endereco)
                        e_cpf_atualizar.delete(0,"end")
                        
                    if cpf_a:
                        mensagem = cliente.atualizarCliente(cpf, novo_cpf=cpf_a)
                        e_endereco_atualizar.delete(0,"end")
                        
                    if mensagem[0]:
                        messagebox.showinfo("SUCESSO", mensagem[1])
                        e_nome_atualizar.delete(0,"end")
                        e_cpf_atualizar.delete(0,"end")
                        e_endereco_atualizar.delete(0,"end")
                        
                        for widget in frameTabela.winfo_children():
                            widget.destroy()
                    
                        tree(cliente.exibirClientes())
                        
                        l_nome_atualizar.destroy()
                        l_cpf_atualizar.destroy()
                        l_endereco_atualizar.destroy()
                        e_nome_atualizar.destroy()
                        e_cpf_atualizar.destroy()
                        e_endereco_atualizar.destroy()
                        b_atualizar.destroy()
                        b_atualizar_voltar.destroy()
                        
                    else:
                        messagebox.showerror("ERRO", mensagem[1])
        
        def voltarAtualizar():
            
            e_cpf_verificar.delete(0,"end")
            
            for widget in frameTabela.winfo_children():
                widget.destroy()
                    
            tree(cliente.exibirClientes())
                        
            l_nome_atualizar.destroy()
            l_cpf_atualizar.destroy()
            l_endereco_atualizar.destroy()
            e_nome_atualizar.destroy()
            e_cpf_atualizar.destroy()
            e_endereco_atualizar.destroy()
            b_atualizar.destroy()
            b_atualizar_voltar.destroy()
        
        cpf = e_cpf_verificar.get()

        if cpf:
            if cliente.verificarCPF(cpf):
                messagebox.showinfo("SUCESSO", "CPF EXISTENTE!")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(cliente.pesquisarCPF(cpf))
                
                # Nome
                l_nome_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Nome: ", bg="#feffff", fg="#403d3d", relief="flat")
                l_nome_atualizar.place(x=10, y=480)
                e_nome_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                e_nome_atualizar.place(x=15, y=520)
                
                # CPF
                l_cpf_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar CPF", bg="#feffff", fg="#403d3d", relief="flat")
                l_cpf_atualizar.place(x=10, y=560)
                e_cpf_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                e_cpf_atualizar.place(x=15, y=600)
                
                # Endereço
                l_endereco_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Endereço", bg="#feffff", fg="#403d3d", relief="flat")
                l_endereco_atualizar.place(x=10, y=640)
                e_endereco_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                e_endereco_atualizar.place(x=15, y=680)
                
                # Botão confirmar
                b_atualizar = Button(framePrincipal_direita, command=atualizarBotao, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="ATUALIZAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                b_atualizar.place(x=15, y=720)
                
                b_atualizar_voltar = Button(framePrincipal_direita, command=voltarAtualizar, width=10, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                b_atualizar_voltar.place(x=208, y=720)
                
            else:
                messagebox.showerror("ERRO", "CPF NÃO EXISTENTE!")
                
    def excluirCliente():
        
        excluir = e_excluir.get()
        
        if excluir and cliente.temClientes():
            excluir = excluir.strip()
            if excluirPor.get() == "CPF":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o cliente com CPF {excluir}?")
                if resultado:
                    mensagem = cliente.excluirCPF(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(cliente.exibirClientes())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
                    
            elif excluirPor.get() == "Nome":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir os clientes com nome {excluir}?")
                if resultado:
                    mensagem = cliente.excluirNome(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(cliente.exibirClientes())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
            
            elif excluirPor.get() == "ID":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir o cliente com ID {excluir}?")
                if resultado:
                    mensagem = cliente.excluirID(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(cliente.exibirClientes())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
            
    def excluirTudo():
            
        if cliente.temClientes() is False:
            messagebox.showinfo("AVISO", "NÃO HÁ CLIENTES CADASTRADOS!")
            
        else:
            resultado = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir tudo?")
            
            if resultado:
                messagebox.showinfo("Ação confirmada", "Todos os cadastros foram excluídos com sucesso!")
                cliente.excluirTudo()
                for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                tree(cliente.exibirClientes())
            else:
                messagebox.showerror("Ação negada", "Não foi possível excluir tudo!")

    ############# FRAME #############

    frameTitulo = Frame(janela,
                width=640,
                height=50,
                bg="#add8e6", 
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

    appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CRUD DE CLIENTE", bg="#add8e6", fg="#feffff", relief="flat")
    appNome.place(x=210, y=11)

    ############# framePrincipal Esquerda #############

    #### CADASTRO ####

    l_cadastrarNome = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CADASTRO", bg="#feffff", fg="#add8e6", relief="flat")
    l_cadastrarNome.place(x=10, y=8)

    # NOME
    l_nome = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Nome*", bg="#feffff", fg="#403d3d", relief="flat")
    l_nome.place(x=10, y=50)
    e_nome = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_nome.place(x=15, y=80)

    # CPF
    l_cpf = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="CPF*", bg="#feffff", fg="#403d3d", relief="flat")
    l_cpf.place(x=10, y=110)
    e_cpf = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_cpf.place(x=15, y=140)

    # ENDEREÇO
    l_endereco = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Endereço*", bg="#feffff", fg="#403d3d", relief="flat")
    l_endereco.place(x=10, y=170)
    e_endereco = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_endereco.place(x=15, y=200)

    # CADASTRAR
    b_cadastrar = Button(framePrincipal_esquerda, command=cadastrarCliente, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="CADASTRAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cadastrar.place(x=15, y=250)

    #### EXCLUSÃO ####

    l_excluirNome = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="EXCLUSÃO", bg="#feffff", fg="#add8e6", relief="flat")
    l_excluirNome.place(x=10, y=310)

    # EXCLUIR
    l_excluir = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Excluir por:", bg="#feffff", fg="#403d3d", relief="flat")
    l_excluir.place(x=10, y=360)

    excluirPor = StringVar()
    excluirPor.set("ID")

    b_excluirID = Radiobutton(framePrincipal_esquerda, text="ID", font=("ARIAL 10 bold"), variable=excluirPor, value="ID",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirNome = Radiobutton(framePrincipal_esquerda, text="Nome", font=("ARIAL 10 bold"), variable=excluirPor, value="Nome",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirCPF = Radiobutton(framePrincipal_esquerda, text="CPF", font=("ARIAL 10 bold"), variable=excluirPor, value="CPF",bg="#feffff", fg="#403d3d", relief="flat")

    b_excluirID.place(x=90, y=360)
    b_excluirNome.place(x=140, y=360)
    b_excluirCPF.place(x=210, y=360)

    e_excluir = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_excluir.place(x=15,y=400)

    # EXCLUIR BOTAO
    b_excluir = Button(framePrincipal_esquerda, command=excluirCliente, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir.place(x=15, y=440)

    # EXCLUIR TUDO BOTAO
    b_excluir_tudo = Button(framePrincipal_esquerda, command=excluirTudo, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR TUDO", bg="#d07684", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir_tudo.place(x=15, y=480)

    ############# framePrincipal Direita #############

    #### PESQUISAR ####

    l_pesquisarNome = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="PESQUISA", bg="#feffff", fg="#add8e6", relief="flat")
    l_pesquisarNome.place(x=10, y=8)

    # PESQUISAR NOME
    l_nome_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Nome", bg="#feffff", fg="#403d3d", relief="flat")
    l_nome_pesquisar.place(x=10, y=50)
    e_nome_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_nome_pesquisar.place(x=15, y=80)

    # PESQUISAR CPF
    l_cpf_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar CPF", bg="#feffff", fg="#403d3d", relief="flat")
    l_cpf_pesquisar.place(x=10, y=110)
    e_cpf_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_cpf_pesquisar.place(x=15, y=140)

    # PESQUISAR ENDEREÇO
    l_endereco_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Endereço", bg="#feffff", fg="#403d3d", relief="flat")
    l_endereco_pesquisar.place(x=10, y=170)
    e_endereco_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_endereco_pesquisar.place(x=15, y=200)

    # PESQUISAR
    b_pesquisar = Button(framePrincipal_direita, command=pesquisarCliente, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=15, y=250)

    # VOLTAR
    b_pesquisar = Button(framePrincipal_direita, command=voltarExibir, width=10, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=205, y=250)

    #### ATUALIZAR ####

    l_atualizarTitle = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="ATUALIZAÇÃO", bg="#feffff", fg="#add8e6", relief="flat")
    l_atualizarTitle.place(x=10, y=310)

    l_cpf_verificar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Verificar CPF", bg="#feffff", fg="#403d3d", relief="flat")
    l_cpf_verificar.place(x=10, y=360)
        
    e_cpf_verificar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_cpf_verificar.place(x=15, y=400)

    b_cpf_verificar = Button(framePrincipal_direita, command=verificarCliente, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VERIFICAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cpf_verificar.place(x=15, y=440)


    ############# Tree #############

    def tree(clientes):
        
        tabelaColunas = ["ID_cliente","Nome","CPF","Endereço"]

        tabelaDF = clientes

        tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
        vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)

        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        frameTabela.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center"]
        h =[80,160,160,240]
        n = 0

        for col in tabelaColunas:
            tree.heading(col, text=col, anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
                    
            n+=1

        for item in tabelaDF:
            tree.insert("", "end", values=item)

    tree(cliente.exibirClientes())


    janela.mainloop()
            