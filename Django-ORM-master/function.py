import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

import leitor_de_oferta as l_o

from db.models import *


class Esqueleton:
    def __init__(self,nome, matricula, cpfx):
       self.aluno = nome
       self.mat = matricula
       self.cpf = cpfx

    def salvar(self):
        cadastro = StudentData.objects.create(name = self.aluno, matricula = self.mat, cpf = self.cpf)
        cadastro.save()
    def vincular_materia(materia):
        
        pass
    
    def periodos(self,periodo,periodo_mais_um):
        self.planilha = l_o.reader("Oferta.xlsx",113,0,10)
        peri_list = []
        for i in range(periodo,periodo_mais_um):
            for x in self.planilha[i]:    #x = linha
                if x[0].value and not x[0].value.startswith('DISCIPLINA'):
                    peri_list.append(x[0].value)
            return peri_list
        
#a = Esqueleton("Lucas","17111178","12448031460")


