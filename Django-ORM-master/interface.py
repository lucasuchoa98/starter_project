from tkinter import *
from functools import partial
from tkinter import ttk
import leitor_de_oferta as l_o
import function as ft

class Open:
    def __init__(self):
        #passando argumento para o command

        self.arg_prof = partial(self.autenticacao,"prof")
        self.arg_al = partial(self.autenticacao,"al")

        #Criating a window
        self.wind = Tk()
        self.wind.title("Pré-matricula")
        self.wind.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)

        #Widgets
        
        self.b_aluno = Button(self.wind, width=20, text = "Aluno",command = self.arg_al, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.b_aluno.grid(row=1,column=0)
        self.b_prof = Button(self.wind, width = 20, text="Professor",command = self.arg_prof ,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.b_prof.grid(row=1,column=1)
        
    def aluno_sheet(self):
        #PAGINA DO ALUNO

        #Passa argumento dentro do command
        self.action_padrao = partial(self.pre_matricula, "padrao")
        self.action_individual = partial(self.pre_matricula,"individual")

        #Criating a window
        self.sheet_al = Tk()
        self.sheet_al.title("Aluno")
        self.sheet_al.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)

        #Widgets
        self.lb_const = ttk.Label(self.sheet_al,text= "Em construção ", style = "BW.TLabel")
        self.lb_const.grid(row=3,column=0)

        self.lb_act = ttk.Label(self.sheet_al, text= "Selecione ", style = "BW.TLabel")
        self.lb_act.grid(row=0,column=0)

        self.padrao = Button(self.sheet_al, width=20, text = "Fluxo Padrão",command = self.action_padrao, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.padrao.grid(row=1,column=0)
        self.individual = Button(self.sheet_al,width=20, text = "Fluxo Individual", font="Arial 10 bold",command = self.action_individual, bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.individual.grid(row=2, column=0)
          
        self.sheet_al.mainloop()

    def professor_sheet(self):
        #Criating a window
        self.sheet_pf = Tk()
        self.sheet_pf.title("Professor")
        self.sheet_pf.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)

        self.lista_primeiro = partial(self.lista_periodo, 1,2)
        self.lista_segundo = partial(self.lista_periodo, 2,3)
        self.lista_terceiro = partial(self.lista_periodo, 3,4)
        self.lista_quarto = partial(self.lista_periodo, 4,5)
        self.lista_quinto = partial(self.lista_periodo, 5,6)
        self.lista_sexto = partial(self.lista_periodo, 6,7)
        self.lista_setimo = partial(self.lista_periodo, 7,8)
        self.lista_oitavo = partial(self.lista_periodo, 8,9)
        self.lista_nono = partial(self.lista_periodo, 9,10)
        
        self.periodo_1 = Button(self.sheet_pf, width=20, text = "Primeiro Periodo",command = self.lista_primeiro, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_1.grid(row=0,column=0)
        self.periodo_2 = Button(self.sheet_pf, width=20, text = "Segundo Periodo",command = self.lista_segundo, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_2.grid(row=1,column=0)
        self.periodo_3 = Button(self.sheet_pf, width=20, text = "Terceiro Periodo", command = self.lista_terceiro, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_3.grid(row=2,column=0)
        self.periodo_4 = Button(self.sheet_pf, width=20, text = "Quarto Periodo",command = self.lista_quarto,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_4.grid(row=3,column=0)
        self.periodo_5 = Button(self.sheet_pf, width=20, text = "Quinto Periodo",command = self.lista_quinto,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_5.grid(row=4,column=0)
        self.periodo_6 = Button(self.sheet_pf, width=20, text = "Sexto Periodo",command = self.lista_sexto, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_6.grid(row=5,column=0)
        self.periodo_7 = Button(self.sheet_pf, width=20, text = "Setimo Periodo", command = self.lista_setimo,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_7.grid(row=6,column=0)
        self.periodo_8 = Button(self.sheet_pf, width=20, text = "Oitavo Periodo", command = self.lista_oitavo,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_8.grid(row=7,column=0)
        self.periodo_9= Button(self.sheet_pf, width=20, text = "Nono Periodo", command = self.lista_nono,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_9.grid(row=8,column=0)

        self.sheet_pf.geometry("300x150+100+100")
        self.sheet_pf.mainloop()

    def autenticacao(self,tipo):
        #Criating a window
        self.janela = Tk()
        self.janela.title("Login")
        self.janela.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)
        
        self.lb1 = ttk.Label(self.janela, text= "Usuário:", style = "BW.TLabel")
        self.lb1.grid(row=1,column=0)
        self.lb2 = ttk.Label(self.janela, text= "Senha:", style = "BW.TLabel")
        self.lb2.grid(row=2,column=0)
        self.lb3 = ttk.Label(self.janela, text= "", style = "BW.TLabel")
        self.lb3.grid(row=0,column=1)
        self.lb4 = ttk.Label(self.janela, text= "" , style = "BW.TLabel")
        self.lb4.grid(row=4,column=1)

        self.entrada1 = Entry(self.janela)
        self.entrada1.grid(row=1,column=1,sticky=W+E)
        self.entrada2 = Entry(self.janela,show="*")
        self.entrada2.grid(row=2, column=1,sticky=W+E)

        if tipo=="prof":
            self.butao = Button(self.janela, width=20,text="ConfirmaR",
                                command=self.analisa_senha,font="Arial 10 bold",bg = "#00FA9A",fg = "white",bd=1,relief=RIDGE)
            self.butao.grid(row=3,column=1)
            
        elif tipo=="al":
            self.arg_not = partial(self.aluno_sheet, "n")
            
            self.butao = Button(self.janela, width=20,text="Confirmar",
                                command=self.aluno_sheet,font="Arial 10 bold",bg = "#00FA9A",fg = "white",bd=1,relief=RIDGE)
            self.butao.grid(row=3,column=1)

            self.ask_but = Button(self.janela, width=20,text="Ainda não é cadastrado ? ",
                                command=self.cadastro_al,font="Arial 10 bold",bg = "#00FA9A",fg = "white",bd=1,relief=RIDGE)
            self.ask_but.grid(row=4,column=1)
        
        self.janela.geometry("300x150+100+100")

        self.janela.mainloop()

    def cadastro_al(self):
        
        self.cadastro_sheet = Tk()
        self.cadastro_sheet.title("Login")
        self.cadastro_sheet.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)

        self.lb_nome = ttk.Label(self.cadastro_sheet, text= "Nome:", style = "BW.TLabel")
        self.lb_nome.grid(row=1,column=0)
        self.lb_matricula = ttk.Label(self.cadastro_sheet, text= "Matricula:", style = "BW.TLabel")
        self.lb_matricula.grid(row=2,column=0)
        self.lb_cpf = ttk.Label(self.cadastro_sheet, text= "CPF:", style = "BW.TLabel")
        self.lb_cpf.grid(row=3,column=0)

        self.lb_andamento = ttk.Label(self.cadastro_sheet, text="")
        self.lb_andamento.grid(row=5,column=1)
        
        
        self.butao = Button(self.cadastro_sheet, width=20,text="Confirmar",
                                command=self.cad_al,font="Arial 10 bold",bg = "#00FA9A",fg = "white",bd=1,relief=RIDGE)
        self.butao.grid(row=4,column=1)

        self.nome = Entry(self.cadastro_sheet)
        self.nome.grid(row=1,column=1,sticky=W+E)
        self.matricula = Entry(self.cadastro_sheet)
        self.matricula.grid(row=2, column=1,sticky=W+E)
        self.cpf = Entry(self.cadastro_sheet)
        self.cpf.grid(row=3,column=1,sticky=W+E)
        
        
        self.janela.geometry("300x150+100+100")

        self.janela.mainloop()

    def cad_al(self):
        a = ft.Esqueleton(self.nome.get() , self.matricula.get() ,self.cpf.get())
        try:
            a.salvar()
            self.lb_andamento["text"] = "Cadastrado com sucesso"
        except:
            self.lb_andamento["text"] = "Matricula já cadastrada"
        
    def  pre_matricula(self,fluxo):
        from function import Esqueleton
        
        a = Esqueleton("nome","matricula","cpfx")
        
        self.mat_sheet = Tk()
        self.mat_sheet.title("Pré-Matricula")
        self.mat_sheet.configure(background="#00FA9A")
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="#00FA9A", font="System 10 bold", foreground="white",aspect=800)

        self.lista_primeiro = partial(self.lista_periodo, 1,2)
        self.lista_segundo = partial(self.lista_periodo, 2,3)
        self.lista_terceiro = partial(self.lista_periodo, 3,4)
        self.lista_quarto = partial(self.lista_periodo, 4,5)
        self.lista_quinto = partial(self.lista_periodo, 5,6)
        self.lista_sexto = partial(self.lista_periodo, 6,7)
        self.lista_setimo = partial(self.lista_periodo, 7,8)
        self.lista_oitavo = partial(self.lista_periodo, 8,9)
        self.lista_nono = partial(self.lista_periodo, 9,10)
        
        self.periodo_1 = Button(self.mat_sheet, width=20, text = "Primeiro Periodo",command = self.lista_primeiro, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_1.grid(row=0,column=0)
        self.periodo_2 = Button(self.mat_sheet, width=20, text = "Segundo Periodo",command = self.lista_segundo, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_2.grid(row=1,column=0)
        self.periodo_3 = Button(self.mat_sheet, width=20, text = "Terceiro Periodo", command = self.lista_terceiro, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_3.grid(row=2,column=0)
        self.periodo_4 = Button(self.mat_sheet, width=20, text = "Quarto Periodo",command = self.lista_quarto,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_4.grid(row=3,column=0)
        self.periodo_5 = Button(self.mat_sheet, width=20, text = "Quinto Periodo",command = self.lista_quinto,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_5.grid(row=4,column=0)
        self.periodo_6 = Button(self.mat_sheet, width=20, text = "Sexto Periodo",command = self.lista_sexto, font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_6.grid(row=5,column=0)
        self.periodo_7 = Button(self.mat_sheet, width=20, text = "Setimo Periodo", command = self.lista_setimo,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_7.grid(row=6,column=0)
        self.periodo_8 = Button(self.mat_sheet, width=20, text = "Oitavo Periodo", command = self.lista_oitavo,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_8.grid(row=7,column=0)
        self.periodo_9= Button(self.mat_sheet, width=20, text = "Nono Periodo", command = self.lista_nono,font="Arial 10 bold", bg = "#00FA9A", fg = "white", bd=1,relief=RIDGE)
        self.periodo_9.grid(row=8,column=0)

        self.mat_sheet.mainloop()            
    
    def lista_periodo(self,periodo,periodo_mais_um):
        self.root = Tk()

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.root, selectmode= EXTENDED)
        self.listbox.pack()

        self.but_confirmar = Button(self.root, text = "Confirmar", command = self.selection)
        self.but_confirmar.pack()
        
        self.planilha = l_o.reader("oferta.xlsx",113,0,10)

        for i in range(periodo,periodo_mais_um):
            for x in self.planilha[i]:
                if x[0].value and not x[0].value.startswith('DISCIPLINA'):
                    self.listbox.insert(END,x[0].value)
            
        # attach listbox to scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        mainloop()

    def selection(self):
        a = self.listbox.curselection()
        for i in a:
            print(self.listbox.get(i))
    
    def analisa_senha(self):
        """
        Function that takes ent of "janela" and compair with the true password
        """
        user = ""
        password = ""
        # Analisando se a senha e usuario estão certos
        if str(self.entrada1.get())==user and str(self.entrada2.get())==password:
            self.janela.destroy()
            self.professor_sheet()
            
        elif str(self.entrada1.get())=="" and str(self.entrada2.get())=="":
            pass
        else:
            self.lb4["text"] = "Erro de usuario ou senha"

if __name__ == '__main__':
    abrir = Open()
