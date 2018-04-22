#Leitor de planilhas no formato(apenas colunas 0,8 e 9): aux_lineX(start_colx,end_colx)

import xlrd

def reader(arquivo,linha,coluna_inicial,coluna_final):
    
    book = xlrd.open_workbook(arquivo)
    first_sheet = book.sheet_by_index(0)
    #first_sheet = book.sheet_by_index(0)
    dictionare_grade,lista_periodo,lista,aux_line,periodo = {},[],[],1,1
    while aux_line <linha:
        aux_colum = 0
        cells = first_sheet.row_slice(rowx=aux_line, start_colx=coluna_inicial, end_colx=coluna_final)
        for cell in cells:
            if aux_colum == 0 or 8<=aux_colum<=9:
                lista.append(cell)
            else:
                pass
            aux_colum+=1
        aux_line +=1
        lista_periodo.append(lista)
        lista = []
    l_periodo,materia,key = [],1,1
    for u in lista_periodo:
        if materia<11:
            l_periodo.append(u)
            materia+=1
        else:
            dictionare_grade[key] = l_periodo
            key+=1
            l_periodo = []
            materia = 1
    return dictionare_grade


#a = reader("oferta.xlsx",113,0,10)
#print(a[1][0])


