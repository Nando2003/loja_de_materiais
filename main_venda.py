from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from crud import venda
from datetime import date
venda = venda.Venda()

def vendaMenu(root):

    janela = Toplevel(root)
    janela.title("CRUD DE VENDA")
    janela.geometry("1300x800")
    janela.configure(bg="#e9edf5")
    janela.resizable(width=False, height=False)

    def atualizar_data(event):
        data_selecionada = e_data_venda.get_date()
        print("Data selecionada:", data_selecionada)

    frameTitulo = Frame(janela,
                width=640,
                height=50,
                bg="#a0a0a0", 
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

    appNome = Label(frameTitulo, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CRUD DE VENDA", bg="#a0a0a0", fg="#feffff", relief="flat")
    appNome.place(x=210, y=11)

    l_cadastrarTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="CADASTRO", bg="#feffff", fg="#a0a0a0", relief="flat")
    l_cadastrarTitulo.place(x=10, y=10)

    l_data_venda = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Venda*", bg="#feffff", fg="#403d3d", relief="flat")
    l_data_venda.place(x=10, y=50)
    e_data_venda = DateEntry(framePrincipal_esquerda, width=42, selectmode="day", borderwidth=2)
    e_data_venda.place(x=15, y=80)

    e_data_venda.bind("<<DateEntrySelected>>", atualizar_data)

    l_valor_total = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Valor total*", bg="#feffff", fg="#403d3d", relief="flat")
    l_valor_total.place(x=10, y=110)
    e_valor_total = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_valor_total.place(x=15, y=140)

    l_fk_id_cliente = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="ID Cliente*", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_cliente.place(x=10, y=170)
    e_fk_id_cliente = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_fk_id_cliente.place(x=15, y=200)

    def cadastrarV():
        data_venda = e_data_venda.get_date()
        valor_total = e_valor_total.get()
        id_cliente = e_fk_id_cliente.get()
        
        if data_venda and valor_total and id_cliente:
            retorno = venda.cadastrarVenda(data_venda, valor_total, id_cliente)
            if retorno[0]:
                messagebox.showinfo("SUCESSO", retorno[1])
                e_valor_total.delete(0,"end")
                e_fk_id_cliente.delete(0,"end")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
            
                tree(venda.exibirTudo())
            else:
                messagebox.showerror("ERRO", retorno[1])
        else:
            messagebox.showerror("ERRO", "PREECHA TODOS OS CAMPOS DE CADASTRO!")

    b_cadastrar = Button(framePrincipal_esquerda, command=cadastrarV, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISA", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_cadastrar.place(x=15, y=240)

    l_pesquisarTitulo = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="PESQUISA", bg="#feffff", fg="#a0a0a0", relief="flat")
    l_pesquisarTitulo.place(x=10, y=10)

    l_dia_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Dia:", bg="#feffff", fg="#403d3d", relief="flat")
    l_dia_pesquisar.place(x=10, y=50)
    e_dia_pesquisar = Entry(framePrincipal_direita, width=13, justify="left", relief="solid")
    e_dia_pesquisar.place(x=15, y=80)

    l_mes_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Mês:", bg="#feffff", fg="#403d3d", relief="flat")
    l_mes_pesquisar.place(x=103, y=50)
    e_mes_pesquisar = Entry(framePrincipal_direita, width=13, justify="left", relief="solid")
    e_mes_pesquisar.place(x=108, y=80)

    l_ano_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Ano:", bg="#feffff", fg="#403d3d", relief="flat")
    l_ano_pesquisar.place(x=200, y=50)
    e_ano_pesquisar = Entry(framePrincipal_direita, width=13, justify="left", relief="solid")
    e_ano_pesquisar.place(x=205, y=80)

    l_valor_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Valor total", bg="#feffff", fg="#403d3d", relief="flat")
    l_valor_pesquisar.place(x=10, y=110)
    e_valor_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_valor_pesquisar.place(x=15, y=140)

    l_fk_id_cliente_pesquisar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Pesquisar Cliente", bg="#feffff", fg="#403d3d", relief="flat")
    l_fk_id_cliente_pesquisar.place(x=10, y=170)
    e_fk_id_cliente_pesquisar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_fk_id_cliente_pesquisar.place(x=15, y=200)

    def pesquisarV():
        
        campos_pesquisa = {
            "ano_p": e_ano_pesquisar.get() or None,
            "mes_p": e_mes_pesquisar.get() or None,
            "dia_p": e_dia_pesquisar.get() or None,
            "valor_p": e_valor_pesquisar.get() or None,
            "fk_id_cliente_p": e_fk_id_cliente_pesquisar.get() or None,
        }

        print(any(valor for valor in campos_pesquisa.values()))
        # se tudo for none = False / se pelo menos um campo não for none = True
        
        if any(valor for valor in campos_pesquisa.values()):
            
            mensagem = venda.pesquisar(**campos_pesquisa)
            if mensagem[0]:
                for widget in frameTabela.winfo_children():
                    widget.destroy()
                tree(mensagem[1])
            else:
                messagebox.showerror("ERRO", mensagem[1])

            e_ano_pesquisar.delete(0, "end")
            e_mes_pesquisar.delete(0, "end")
            e_dia_pesquisar.delete(0, "end")
            e_valor_pesquisar.delete(0, "end")
            e_fk_id_cliente_pesquisar.delete(0, "end")
        else:
            messagebox.showerror("ERRO", "Nenhum campo preenchido para pesquisa.")

    def voltarPesquisa():
        for widget in frameTabela.winfo_children():
            widget.destroy()
            
        tree(venda.exibirTudo())
        
    b_pesquisar = Button(framePrincipal_direita, command=pesquisarV, width=25, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="PESQUISAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=15, y=240)

    b_pesquisar = Button(framePrincipal_direita, command=voltarPesquisa, width=10, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_pesquisar.place(x=205, y=240)


    l_excluirTitulo = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 16 bold"), text="EXCLUSÃO", bg="#feffff", fg="#a0a0a0", relief="flat")
    l_excluirTitulo.place(x=10, y=350)

    l_excluir = Label(framePrincipal_esquerda, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Excluir por:", bg="#feffff", fg="#403d3d", relief="flat")
    l_excluir.place(x=10, y=390)

    excluirPor = StringVar()
    excluirPor.set("ID")

    b_excluirID = Radiobutton(framePrincipal_esquerda, text="ID", font=("ARIAL 10 bold"), variable=excluirPor, value="ID",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirData = Radiobutton(framePrincipal_esquerda, text="Data", font=("ARIAL 10 bold"), variable=excluirPor, value="Data",bg="#feffff", fg="#403d3d", relief="flat")
    b_excluirValor = Radiobutton(framePrincipal_esquerda, text="Valor", font=("ARIAL 10 bold"), variable=excluirPor, value="Valor",bg="#feffff", fg="#403d3d", relief="flat")

    b_excluirID.place(x=90, y=390)
    b_excluirData.place(x=135, y=390)
    b_excluirValor.place(x=195, y=390)

    e_excluir = Entry(framePrincipal_esquerda, width=45, justify="left", relief="solid")
    e_excluir.place(x=15,y=420)

    def excluirVenda():
        excluir = e_excluir.get()
        
        if excluir and venda.temVenda():
            excluir = excluir.strip()
            if excluirPor.get() == "ID":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir a venda com ID {excluir}?")
                if resultado:
                    mensagem = venda.excluirID(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda.exibirTudo())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
                    
            elif excluirPor.get() == "Data":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir as vendas com data {excluir}?")
                if resultado:
                    mensagem = venda.excluirData(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda.exibirTudo())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")
            
            elif excluirPor.get() == "Valor":
                resultado = messagebox.askyesno("Confirmação", f"Você deseja excluir a venda com valor {excluir}?")
                if resultado:
                    mensagem = venda.excluirValor(excluir)
                    messagebox.showinfo("Ação confirmada", mensagem)
                    e_excluir.delete(0, "end")
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                    tree(venda.exibirTudo())
                else:
                    messagebox.showerror("Ação negada", f"Não foi possível excluir!")

    def excluirTudo():
        if venda.temVenda() is False:
            messagebox.showinfo("AVISO", "NÃO HÁ VENDAS CADASTRADOS!")
            
        else:
            resultado = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir tudo?")
            
            if resultado:
                messagebox.showinfo("Ação confirmada", "Todos os cadastros foram excluídos com sucesso!")
                venda.excluirTudo()
                for widget in frameTabela.winfo_children():
                        widget.destroy()
            
                tree(venda.exibirTudo())
            else:
                messagebox.showerror("Ação negada", "Não foi possível excluir tudo!")

    # EXCLUIR BOTAO
    b_excluir = Button(framePrincipal_esquerda, command=excluirVenda, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir.place(x=15, y=450)

    # EXCLUIR TUDO BOTAO
    b_excluir_tudo = Button(framePrincipal_esquerda, command=excluirTudo, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="EXCLUIR TUDO", bg="#d07684", fg="#403d3d", relief="raised", overrelief="ridge")
    b_excluir_tudo.place(x=15, y=480)

    l_atualizarTitle = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 16 bold"), text="ATUALIZAÇÃO", bg="#feffff", fg="#a0a0a0", relief="flat")
    l_atualizarTitle.place(x=10, y=350)

    l_ID_verificar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Verificar ID", bg="#feffff", fg="#403d3d", relief="flat")
    l_ID_verificar.place(x=10, y=390)
        
    e_ID_verificar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
    e_ID_verificar.place(x=15, y=420)

    def verificarVenda():
        
            def atualizarBotao():
                            data = e_data_atualizar.get()
                            valor_total = e_valor_total_atualizar.get()
                            cliente = e_fk_cliente_atualizar.get()
                            
                            if data and len(data) == 10:
                                mensagem = venda.atualizarVenda(id, nova_data_venda=data)
                            
                            else:
                                mensagem = [False, ""]
                            
                            if valor_total:
                                mensagem = venda.atualizarVenda(id, nova_valor_total=valor_total)
                                
                            if cliente:
                                mensagem = venda.atualizarVenda(id, nova_fk_id_cliente=cliente)
                            
                                        
                            if mensagem[0]:
                                messagebox.showinfo("SUCESSO", mensagem[1])
                                e_data_atualizar.delete(0,"end")
                                e_valor_total_atualizar.delete(0,"end")
                                e_fk_cliente_atualizar.delete(0,"end")
                                
                                for widget in frameTabela.winfo_children():
                                    widget.destroy()
                            
                                tree(venda.exibirTudo())
                                
                                l_data_atualizar.destroy()
                                e_data_atualizar.destroy()
                                l_valor_total_atualizar.destroy()
                                e_valor_total_atualizar.destroy()
                                l_fk_cliente_atualizar.destroy()
                                e_fk_cliente_atualizar.destroy()
                                b_atualizar.destroy()
                                b_atualizar_voltar.destroy()
                                b_atualizar.destroy()
                                b_atualizar_voltar.destroy()
                                e_ID_verificar.delete(0,"end")
                                
                            else:
                                messagebox.showerror("ERRO", mensagem[1])
            
            def voltarAtualizar():
                
                e_ID_verificar.delete(0,"end")
                
                for widget in frameTabela.winfo_children():
                    widget.destroy()
                        
                tree(venda.exibirTudo())
                            
                l_data_atualizar.destroy()
                e_data_atualizar.destroy()
                l_valor_total_atualizar.destroy()
                e_valor_total_atualizar.destroy()
                l_fk_cliente_atualizar.destroy()
                e_fk_cliente_atualizar.destroy()
                b_atualizar.destroy()
                b_atualizar_voltar.destroy()
            
            id = e_ID_verificar.get()

            if id:
                
                if venda.verificarID(id):
                    messagebox.showinfo("SUCESSO", "ID_PRODUTO EXISTE!")
                    
                    for widget in frameTabela.winfo_children():
                        widget.destroy()
                    
                    resultado = venda.pesquisarID(id_p=id)
                    
                    tree(resultado[1])
                    
                    # Data
                    l_data_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Data(XX/XX/XXXX): ", bg="#feffff", fg="#403d3d", relief="flat")
                    l_data_atualizar.place(x=10, y=480)
                    e_data_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_data_atualizar.place(x=15, y=510)
                    
                    # Venda
                    l_valor_total_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Valor Total", bg="#feffff", fg="#403d3d", relief="flat")
                    l_valor_total_atualizar.place(x=10, y=540)
                    e_valor_total_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_valor_total_atualizar.place(x=15, y=570)
                    
                    # Cliente
                    l_fk_cliente_atualizar = Label(framePrincipal_direita, height=50, anchor=NW, font=("ARIAL 10 bold"), text="Atualizar Cliente", bg="#feffff", fg="#403d3d", relief="flat")
                    l_fk_cliente_atualizar.place(x=10, y=600)
                    e_fk_cliente_atualizar = Entry(framePrincipal_direita, width=45, justify="left", relief="solid")
                    e_fk_cliente_atualizar.place(x=15, y=630)
                    
                    # Botão confirmar
                    b_atualizar = Button(framePrincipal_direita, command=atualizarBotao, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="ATUALIZAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar.place(x=15, y=660)
                    
                    b_atualizar_voltar = Button(framePrincipal_direita, command=voltarAtualizar, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), text="VOLTAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
                    b_atualizar_voltar.place(x=15, y=690)
                    
                else:
                    messagebox.showerror("ERRO", "ID_PRODUTO NÃO EXISTE!")

    b_ID_verificar = Button(framePrincipal_direita, width=38, height=1, anchor=CENTER, font=("ARIAL 8 bold"), command=verificarVenda, text="VERIFICAR", bg="#feffff", fg="#403d3d", relief="raised", overrelief="ridge")
    b_ID_verificar.place(x=15, y=450)

    def tree(clientes):
        
        tabelaColunas = ["ID_venda","Data venda","Valor total","ID_cliente"]

        tabelaDF = clientes

        tree = ttk.Treeview(frameTabela, selectmode="extended", columns=tabelaColunas, show="headings")
        vsb = ttk.Scrollbar(frameTabela, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)

        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        frameTabela.grid_rowconfigure(0, weight=12)

        hd = ["center","center", "center", "center"]
        h =[155,165,165,155]
        n = 0

        for col in tabelaColunas:
            tree.heading(col, text=col, anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
                    
            n+=1

        for item in tabelaDF:
            tree.insert("", "end", values=item)

    tree(venda.exibirTudo())

    janela.mainloop()