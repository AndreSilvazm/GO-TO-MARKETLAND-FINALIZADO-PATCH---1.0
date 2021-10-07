from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import random
from time import sleep



class Cadastrar():

    def CadastrarBackend(self):

        Certa = True
        nomec = self.nome.get()
        sobrec = self.sobrenome.get()
        usuac = self.usuarioc.get()
        senhaxd = self.senhac.get()
        confis = self.confisenha.get()
        confirmac = int(self.confirma.get())


        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                passwd='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor


            )
        except:
            print('Erro ao tentar conectar ao banco de dados')




        if len(usuac)>2 <= 13:
            if len(senhaxd) >5 <= 8:

                if senhaxd != confis:
                    messagebox.showinfo('SENHA', 'AS SENHAS NÃO AS MESMAS')

                else:
                    Certa = True

                if Certa:
                    if confirmac == self.ra:
                        usuariomaiusculo = usuac.upper()

                        try:
                            with conexao.cursor() as cursor:
                                cursor.execute('insert into usuarios(nome, sobrenome, usuario, senha) values (%s, %s, %s, %s)', (nomec, sobrec, usuac, senhaxd))
                                conexao.commit()
                                messagebox.showinfo('CADASTRADO', f' | {usuariomaiusculo} |  CADASTRADO COM SUCESSO').upper()
                                self.cadastro.destroy()
                        except:
                            messagebox.showinfo('ERROR', 'ERRO AO TENTAR CADASTRAR NO BANCO DE DADOS')

                    else:
                        messagebox.showinfo('ERRO', 'A CHAVE DE SEGURANÇA ESTA ERRADA')


            else:
                messagebox.showinfo('ERRO', 'SENHA DEVE TER ATÉ 8 CARACTERES')

        else:
            messagebox.showinfo('ERRO', 'USUARIO DEVE TER ATÉ 13 CARACTERES')


    def __init__(self):

        self.cadastro = Tk()
        self.cadastro.geometry('250x500')
        self.cadastro.title('CADASTRAR')
        self.cadastro.resizable(False, False)

        self.ra = int(random.randrange(1000, 10000))


        Label(self.cadastro, text='').grid(row=12, column=0)

        Label(self.cadastro, text='CADASTRAR', width=30, bg='Black', fg='white').grid(row=13, column=0, columnspan=2 )



        Label(self.cadastro, text='NOME').grid(row=14, column=0, padx=10, pady=10)
        self.nome = Entry(self.cadastro, width=30)
        self.nome.grid(row=15, column=0)



        Label(self.cadastro, text='SOBRENOME').grid(row=16, column=0, padx=10, pady=10)
        self.sobrenome = Entry(self.cadastro, width=30)
        self.sobrenome.grid(row=17, column=0)


        Label(self.cadastro, text='USUARIO').grid(row=18, column=0, padx=10, pady=10)
        self.usuarioc = Entry(self.cadastro, width=30)
        self.usuarioc.grid(row=19, column=0)



        Label(self.cadastro, text='SENHA').grid(row=20, column=0, padx=10, pady=10)
        self.senhac = Entry(self.cadastro, width=30)
        self.senhac.grid(row=21, column=0)



        Label(self.cadastro, text='CONFIRME SUA SENHA').grid(row=22, column=0, padx=10, pady=10)
        self.confisenha = Entry(self.cadastro, width=30)
        self.confisenha.grid(row=23, column=0)




        self.ra = int(random.randrange(1000, 10000))
        Label(self.cadastro, text='INSIRA A CHAVE DE SEGURANÇA:', bg='BLACK', fg='white', width=30, relief='flat').grid(row=25,column=0,padx=10,pady=10)
        Label(self.cadastro, text=self.ra, width=5, fg='green').grid(row=26, column=0, padx=10, )
        self.confirma = Entry(self.cadastro, width=30)
        self.confirma.grid(row=27, column=0, padx=10)


        self.confircadastro = Button(self.cadastro, width=30, text='CONFIRMAR CADASTRO', command=self.CadastrarBackend, bg='yellow', relief='flat')
        self.confircadastro.grid(row=29, column=0, padx=10, pady=30)

        self.cadastro.mainloop()


class Telaprinc():


    #EXCLUINDO PRODUTOS
    def ExcluirJP(self):

        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar ao banco de dados')

        # CONFIRMAR SOBRE EXCLUIR

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from japão where id = {}'.format(idDeletar))
                certeza = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

            for linha in certeza:
                print(linha['produto'])


        if messagebox.askokcancel('TEM CERTEZA?', 'VOCE TEM CERTEZA QUE QUER ELIMINAR O PRODUTO {} ?'.format(certeza)):

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from japão where id = {}'.format(idDeletar))
                    conexao.commit()
            except:
                print('erro ao fazer a consulta')

            self.MostrarProdutosBackEndJP()


    # CADASTRAR OS PRODUTOS
    def JapaoCadastrarBE(self):

        #PEGANDO OS DASDOS DAS VARIAVEIS

        produto = self.produto.get()
        marca = self.marca.get()
        tipo = self.tipo.get()
        preco = float(self.preco.get())



        #ADICIONANDO AO BANCO DE DADOS

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                passwd='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )

        except:

            messagebox.showinfo('ERRO', 'ERRO AO TENTAR CONECTAR O BANCO DE DADOS - JJAPAOCADASTRARBE')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into japão (produto, marca, tipo, preco) values (%s, %s, %s, %s)',(produto, marca, tipo, preco))
                conexao.commit()
                messagebox.showinfo('SUCESSO', f'|{produto}| ADICIONADO COM SUCESSO')
                self.jcbe.destroy()
        except:
            messagebox.showinfo('ERRO', 'ERRO AO TENTAR CADASTRAR O NOVO PRODUTO - JAPAOCADASTRARBE')

        self.MostrarProdutosBackEndJP()

    def JapaoCadastrarFE(self):


        self.jcbe = Tk()
        self.jcbe.title('CADASTRAR PRODUTO - SUPERMERCADO JAPÃO')
        self.jcbe['bg'] = '#636F6C'

        messagebox.showinfo('NAO SE ESQUEÇA','NAO SE ESQUEÇA DE DECLARAR SUA CARTEIRA PARA FAZER UMA COMPRA!')

        Label(self.jcbe, text='CADASTRE UM PRODUTO', width=30, fg='white', bg='black').grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        Label(self.jcbe, text='NOME DO PRODUTO', bg='black', fg='white', width=30).grid(row=1, column=0, padx=5, pady=5)
        self.produto = Entry(self.jcbe, width=30)
        self.produto.grid(row=2, column=0, padx=5, pady=5)

        Label(self.jcbe, text='MARCA DO PRODUTO', bg='Black', fg='white', width=30).grid(row=3, column=0, padx=5, pady=5)
        self.marca = Entry(self.jcbe, width=30)
        self.marca.grid(row=4, column=0, padx=5, pady=5)

        Label(self.jcbe, text='TIPO DO PRODUTO', bg='black', fg='white', width=30).grid(row=5, column=0, padx=5, pady=5)
        self.tipo = Entry(self.jcbe, width=30)
        self.tipo.grid(row=6, column=0, padx=5, pady=5)

        Label(self.jcbe, text='PREÇO', bg='black', fg='white', width=30).grid(row=7, column=0, padx=5, pady=5)
        self.preco = Entry(self.jcbe, width=30)
        self.preco.grid(row=8, column=0, padx=5, pady=5)

        Button(self.jcbe, text='CADASTRAR O PRODUTO', bg='#2BA385', fg='white', command=self.JapaoCadastrarBE).grid(row=9, column=0, padx=5, pady=5)


        self.jcbe.mainloop()

    ###################

    def Excluirprdcarrinho(self):

        idDeletar = int(self.carrinho.selection()[0])

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar ao banco de dados')

        # CONFIRMAR SOBRE EXCLUIR

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from carrinho where id = {}'.format(idDeletar))
                certeza = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

            for linha in certeza:
                print(linha['produto'])

        if messagebox.askokcancel('TEM CERTEZA?', 'VOCE TEM CERTEZA QUE QUER ELIMINAR O PRODUTO {} ?'.format(certeza)):

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from carrinho where id = {}'.format(idDeletar))
                    conexao.commit()
            except:
                print('erro ao fazer a consulta')

        self.MostrarProdutosdocarrinho()



    def MostrarProdutosdocarrinho(self):

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from carrinho')
                produtos = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.carrinho.delete(*self.carrinho.get_children())

        carreta = []

        for linha in produtos:
            carreta.append(linha['produto'])
            carreta.append(linha['marca'])
            carreta.append(linha['tipo'])
            carreta.append(linha['preco'])

            self.carrinho.insert("", END, values=carreta, iid=linha['id'])

            carreta.clear()


    def ContasBE(self):

        self.MostrarProdutosdocarrinho

        carteira = int(self.carteira.get())

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                passwd='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao tentar acessar - CONTASBE')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from carrinho')
                resultado = cursor.fetchall()
        except:
            print('ERRO AO TENTAR ACESSAR - CONTASBE')




        soma = 0

        for valor in resultado:

            preço = float(valor['preco'])

            soma += preço


        if soma > carteira:

            sominha = soma - carteira
            messagebox.showinfo('ERRO', f'SALDO INSUFICIENTE, VOCE AINDA PRECISA {sominha} PARA CONSEGUIR EFETUAR SUA COMPRA')

        if carteira > soma:

            troco = carteira - soma
            messagebox.showinfo('COMPRA EFETUADA', f'SUA COMPRA FOI EFETUADA COM SUCESSO E AINDA COM UM TROQUINHO DE {troco} R$')

            self.notinha = Tk()
            self.notinha.title('NOTA FISCAL')
            self.notinha['bg'] = '#262F31'

            Label(self.notinha, text='PRODUTOS COMPRADOS', bg='black', fg='white', width=30).grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            Label(self.notinha, text=resultado).grid(row=1, column=0)

            Label(self.notinha, text='VALOR DA COMPRA', bg='black', fg='white', width=30).grid(row=2, column=0, pady=5, columnspan=2)
            Label(self.notinha, text=soma, width=30).grid(row=3, column=0, columnspan=2, pady=5)

            Label(self.notinha, text='TROCO', bg='black', fg='white', width=30).grid(row=4, column=0, columnspan=2, pady=5)
            Label(self.notinha, text=troco).grid(row=5, column=0, columnspan=2, pady=5)

            messagebox.showinfo('EMITIDO', 'NOTA FISCAL EMITIDA')
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('truncate table carrinho')
                    conexao.commit()
            except:
                print('erro')

            self.vizu.destroy()

        if carteira == soma:

            troco = carteira - soma
            messagebox.showinfo('COMPRA EFETUADA', f'SUA COMPRA FOI EFETUADA COM SUCESSO ')

            self.notinha = Tk()
            self.notinha.title('NOTA FISCAL')
            self.notinha['bg'] = '#262F31'

            Label(self.notinha, text='PRODUTOS COMPRADOS', bg='black', fg='white', width=30).grid(row=0, column=0, columnspan=2, pady=5)
            Label(self.notinha, text=resultado).grid(row=1, column=0)

            Label(self.notinha, text='VALOR DA COMPRA', bg='black', fg='white', width=30).grid(row=2, column=0, pady=5, columnspan=2)
            Label(self.notinha, text=soma, width=30).grid(row=3, column=0, pady=5, columnspan=2)

            Label(self.notinha, text='TROCO', bg='black', fg='white', width=30).grid(row=4, column=0, pady=5, columnspan=2)
            Label(self.notinha, text=troco).grid(row=5, column=0, padx=5, pady=5, columnspan=2)

            messagebox.showinfo('EMITIDO', 'NOTA FISCAL EMITIDA')
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('truncate table carrinho')
                    conexao.commit()
            except:
                print('erro')

            self.vizu.destroy()

        self.notinha.mainloop()







    def VizualizarCARRINHOJP(self):


        self.carteirada = self.carteira.get()

        if self.carteirada:

            self.vizu = Tk()
            self.vizu.title('CARRINHO')
            self.vizu['bg'] = 'BLACK'


            self.carrinho = ttk.Treeview(self.vizu, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')

            self.carrinho.column("column1", width=400, minwidth=500, stretch=NO)
            self.carrinho.heading('#1', text='PRODUTO')

            self.carrinho.column("column2", width=150, minwidth=200, stretch=NO)
            self.carrinho.heading('#2', text='MARCA')

            self.carrinho.column("column3", width=150, minwidth=500, stretch=NO)
            self.carrinho.heading('#3', text='TIPO')

            self.carrinho.column("column4", width=70, minwidth=500, stretch=NO)
            self.carrinho.heading('#4', text='PREÇO')

            self.carrinho.grid(row=0, column=0)



            carteira = int(self.carteira.get())

            try:
                conexao = pymysql.connect(

                    host='localhost',
                    user='root',
                    passwd='',
                    db='gotomarketland',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor

                )


            except:
                print('erro ao tentar acessar - CONTASBE')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from carrinho')
                    resultado = cursor.fetchall()
            except:
                print('ERRO AO TENTAR ACESSAR - CONTASBE')

            soma = 0



            for valor in resultado:
                preço = float(valor['preco'])

                self.MostrarProdutosdocarrinho()

                soma += preço

                print(soma)





            Label(self.vizu, text='QUANTO DEU SUA COMPRA').grid(row=1, column=0, padx=5, pady=5)


            Label(self.vizu, text=soma, bg='black', fg='white').grid(row=2, column=0)

            Button(self.vizu, text='EXCLUIR PRODUTO', command=self.Excluirprdcarrinho).grid(row=3, column=0, pady=5, padx=5)

            Button(self.vizu, text='EXECUTAR A COMPRA', command=self.ContasBE).grid(row=4, column=0, padx=5, pady=5)

            Button(self.vizu, text='ATUALIZAR CARRINHO', command=self.MostrarProdutosdocarrinho).grid(row=5, column=0)

            self.MostrarProdutosdocarrinho()


            self.vizu.mainloop()

        else:
            messagebox.showinfo('ERRO', 'VOCE TEM QUE DECLARAR SUA CARTEIRA PARA PROSEGUIR AO CARRINHO')

    def ComprarProdutosBEJP(self):



        #ESSA DEF VAI MANDAR TODOS OS PRODUTOS PARA O BANCO DE DADOS CARRINHO

        idDeletar = int(self.tree.selection()[0])

        #EXTRAINDO OS DADOS DO BANCO DE DADOS PRODUTOS
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar ao banco de dados')

        #PEGANDO OS DADOS DA CARTEIRA
        self.cart = self.carteira.get()

        if self.cart:

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from japão where id = {}'.format(idDeletar))
                    produts = cursor.fetchall()
            except:
                print('erro ao fazer a consulta')

            for p in produts:
                self.idadd = p['id']
                self.produtadd = p['produto']
                self.marcaadd = p['marca']
                self.tipoadd = p['tipo']
                self.precoadd = float(p['preco'])

                print(self.idadd, self.produtadd, self.marcaadd, self.tipoadd, self.precoadd)

            # ADICIONANDO AO BANCO DE DADOS CARRINHOS

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into carrinho (produto, marca, tipo, preco) values (%s, %s, %s, %s)', (self.produtadd, self.marcaadd, self.tipoadd, self.precoadd))
                    conexao.commit()
                    messagebox.showinfo('SUCESSO', 'PRODUTO ADICIONADO AO CARRINHO')
            except:
                messagebox.showinfo('ERRO', 'ERRO AO TENTAR ENVIAR OS DADOS PARA CARRINHO')

        else:
            messagebox.showinfo('ERRO', 'VOCE PRECISA DECLARAR SUA RENDA PARA ADICIONAR COMPRAS AO CARRINHo')

        self.MostrarProdutosdocarrinho()




    def MostrarProdutosBackEndJP(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from japão')
                produtos = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in produtos:
            linhaV.append(linha['produto'])
            linhaV.append(linha['marca'])
            linhaV.append(linha['tipo'])
            linhaV.append(linha['preco'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'])

            linhaV.clear()


    def Japão(self):

        self.janp.destroy()
        self.japa = Tk()
        self.japa.title('COMPRAR NO JAPÃO')
        self.japa['bg'] = '#636F6C'


        Button(self.japa, text='CADASTRAR NOVO PRODUTO', width=30, relief='flat', bg='#D3525F', command=self.JapaoCadastrarFE).grid(row=1, column=1, padx=5, pady=5 )
        Button(self.japa, text='EXCLUIR PRODUTO', width=30, relief='flat',bg='#EE4B5C', command=self.ExcluirJP).grid(row=2, column=1, padx=5, pady=5 )
        Button(self.japa, text='COMPRAR ', width=40, relief='flat', bg='#08814A', command=self.ComprarProdutosBEJP).grid(row=1, column=0, padx=5, pady=5 )
        Button(self.japa, text='VER MEU CARRINHO', width=30, relief='flat', bg='#5CDCA2', command=self.VizualizarCARRINHOJP).grid(row=2, column=0, padx=5, pady=5)
        Button(self.japa, text='ATUALIZAR TABELA', width=30, relief='flat', bg='#97303B', command=self.MostrarProdutosBackEndJP).grid(row=3, column=1, padx=5, pady=5)

        Label(self.japa, text='DECLARE A SUA CARTEIRA', width=30, bg='black', fg='white').grid(row=1, column=3, pady=5, padx=5)
        self.carteira = Entry(self.japa, width=30, fg='green3')
        self.carteira.grid(row=3, column=3,)


        #TREE VIEW DOS PRODUTOS

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='gotomarketland',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            messagebox.showinfo('ERRO','DEU UM ERRO ao tentar conectar - JAPA')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from japão')
                produtos = cursor.fetchall()
        except:
            messagebox.showinfo('ERRO','ERRO AO TENTAR SELECIONAR OS DADOS - JAPAO')


        self.tree = ttk.Treeview(self.japa, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')

        self.tree.column("column1", width=400, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='PRODUTO')

        self.tree.column("column2", width=150, minwidth=200, stretch=NO)
        self.tree.heading('#2', text='MARCA')

        self.tree.column("column3", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='TIPO')

        self.tree.column("column4", width=70, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='PREÇO')

        self.tree.grid(row=0, column=0)

        self.MostrarProdutosBackEndJP()


        self.japa.mainloop()
        
    #TELA DE MERCADOS
    def __init__(self):

        self.janp = Tk()
        self.janp.geometry('280x500')
        self.janp['bg'] = '#524f4f'

        Label(self.janp, text='MERCADOS DISPONIVEIS', fg='white', bg='black', width=40).grid(row=1, column=0, pady=10)
        Button(self.janp, text='SUPERMERCADO JAPÃO', width=35, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.Japão).grid(row=2, column=0, padx=10, pady=10)


        self.janp.mainloop()


class Login():


    def Logar(self):

        autenticado = False

        try:

            conexao = pymysql.connect(

                host='localhost',
                user='root',
                passwd='',
                db='gotomarketland',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
        except:
            print('ERRO AO TENTAR ACESSAR AO BANCO DE DADOS')

        try:

            with conexao.cursor() as cursor:
                cursor.execute('select * from usuarios')
                resultado = cursor.fetchall()
        except:
            print('ERRO AO TENTAR PUXAR AS COISAS')

        usuario = self.usuario.get()
        senha = self.senha.get()

        # Validar

        for dado in resultado:
            if usuario == dado['usuario'] and senha == dado['senha']:
                autenticado = True

        if not autenticado:
            messagebox.showinfo('USUARIO', 'SENHA OU USUARIO ERRADOS')

        if autenticado:
            sleep(1)
            messagebox.showinfo('USUARIO', f'SEJA MUITO BEM VINDO! {usuario}'.upper())
            self.login.destroy()

            Telaprinc()



    def __init__(self):



        self.login = Tk()
        self.login.title('TELA DE LOGIN GO TO MARKET')
        self.login.geometry('200x300')
        self.login['bg'] = '#2593AC'
        self.login.resizable(False,False)

        Label(self.login, text='USUARIO', fg='black', font='impact',  width=25, bg='#2593AC').grid(row=3, column=0, pady=5, )


        self.usuario = Entry(self.login, width=30, fg='black')
        self.usuario.grid(row=4, column=0, pady=10)


        Label(self.login, text='SENHA', fg='black', font='impact', width=25, bg='#2593AC').grid(row=5, column=0, pady=5)


        self.senha = Entry(self.login, width=30, fg='black')
        self.senha.grid(row=6, column=0)

        Button(self.login, text='LOGIN', bg='Green3',font='impact', command=self.Logar, width=20, relief='flat').grid(row=9, column=0, pady=10 )
        Button(self.login, text='INSCREVA-SE', bg='Orange3', font='impact', command=Cadastrar, relief='flat').grid(row=11, column=0)





        self.login.mainloop()


Login()


