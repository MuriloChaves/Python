#coding: utf-8

"""
Gerador de código de barra desenvolvido em Python para múltiplos produtos - PÓS SISOS

Modelo: PIMACO A4251 (13 linhas X 5 colunas)
Documento: A4 (21.0cm x 29.7cm)
Tamanho útil: 21,2mm x 38,2mm
Qtd. Etiquetas/Folha: 65

Requirements:
Python==3.7.0
Pillow==5.3.0
reportlab==3.5.9

Autor: JAYME, M. C.
Última modificação: 30 de outubro de 2018
"""

import sys
import json

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128

class Entidade:

    """
    Implementação de classe com objetivo de realizar a abstração de uma entidade - no caso, um obj etiqueta.

    Modo de uso com a declaração de seus args[]:
    nomeEtiqueta = Entidade(
        descrição = 'descricao ou nome do produto', barcode = 'número do código de barro à ser gerado', 
        codigo = 'número do código para ser impresso na tela', 
        valor = 'preço do produto'
        )
    """

    # Construtor
    def __init__(self, desc = None, barcode = None, cod = None, valor = None, qtd = None):
        self.desc = desc
        self.barcode = barcode
        self.cod = cod
        self.valor = valor
        self.qtd = qtd

    # Setters
    def setDesc(self, desc):
        self.desc = desc
    
    def setBarcode(self, barcode):
        self.barcode = barcode

    def setCod(self, cod):
        self.cod = cod
    
    def setValor(self, valor):
        self.valor = valor

    def setQtd(self, qtd):
        self.qtd = qtd

    # Getters
    def getDesc(self):
        return self.desc

    def getBarcode(self):
        return self.barcode

    def getCod(self):
        return self.cod

    def getValor(self):
        return self.valor

    def getQtd(self):
        return self.qtd

def switchCase_desc(desc):

    if (len(desc) > 25):
        desc = desc[:25]

    desc = desc[:25]
    tamanhoString = str(len(desc))

    return {
        '1' : 55,
        '2' : 54,
        '3' : 52,
        '4' : 51,
        '5' : 48,
        '6' : 46,
        '7' : 48,
        '8' : 45,
        '9' : 44,
        '10' : 43,
        '11' : 41,
        '12' : 40,
        '12' : 40,
        '13' : 38,
        '14' : 36,
        '15' : 35,
        '16' : 33,
        '17' : 31,
        '18' : 29,
        '19' : 27,
        '20' : 25,
        '21' : 23,
        '22' : 21,
        '23' : 19,
        '24' : 17,
        '25': 14,
    } [tamanhoString]

def switchCase_barCode(barCode):

    tamanhoBarCode = str(len(barCode))

    return {
        '1' : 25,
        '2' : 27,
        '3' : 22,
        '4' : 25,
        '5' : 19,
        '6' : 22,
        '7' : 16,
        '8' : 19,
        '9' : 13,
        '10' : 16,
        '11' : 10,
        '12' : 13,
        '12' : 13,
        '13' : 7,
        '14' : 7,
    } [tamanhoBarCode]

def switchCase_code(cod):

    tamanhoCod = str(len(cod))

    return {
        '1' : 54,
        '2' : 54,
        '3' : 52,
        '4' : 51,
        '5' : 49,
        '6' : 47,
        '7' : 46,
        '8' : 44,
        '9' : 42,
        '10' : 40,
    } [tamanhoCod]

def switchCase_preco(preco):

    tamanhoPreco = str(len(preco))

    return {
        '4' : 44,
        '5' : 45,
        '6' : 43,
        '7' : 41,
        '8' : 40,
        '9' : 38,
    } [tamanhoPreco]

def constituir(arquivo = "etiqueta.pdf", pagesize = A4, margemX = 0, tamHorizontal = 0, margemY = 0, tamanhoVertical = 0, larguraEtiqueta = 0, alturaEtiqueta = 0, imprimirGrade = False):
    PDF = canvas.Canvas("%s" % arquivo, pagesize)
    PDF.setFont("Helvetica", 6)
    
    if (imprimirGrade != False):
        PDF.grid(range(int(margemX), int(tamHorizontal), int(larguraEtiqueta + (margemX / 2))), range(int(margemY), int(tamanhoVertical), int(alturaEtiqueta)))
    
    return PDF

def plotar(PDF, margemXInicial = 0, tamanhoVertical = 0, margemYInicial = 0, larguraEtiqueta = 0, alturaEtiqueta = 0):

    print('\n### Iniciando Processo de Plotagem ###\n')

    desc = '888888888 ALCON CLUB ALIM'
    if (len(desc) > 25): 
        desc = desc[:25]
    ajuste_desc = switchCase_desc(desc)

    code = 12345678965213
    if (len(str(code)) > 14):
        print('Tamanho excede 14 dígitos, perdendo centralização')
    ajuste_barCode = switchCase_barCode(str(code))
    barcode = code128.Code128(code)

    cod = '1'
    if (len(cod) > 10):
        print('Código excede 10 dígitos')
    ajuste_cod = switchCase_code(cod)

    preco = '1.99'
    ajuste_preco = switchCase_preco(preco)

    for linha in range(10):
        print('Linha:', linha)
        for coluna in range(5):
            print('\tColuna:', coluna)
            PDF.drawString(
                x = margemXInicial + ajuste_desc + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (0.5 * cm) - (alturaEtiqueta * linha), 
                text=desc
                )
            barcode.drawOn(
                PDF, 
                x = margemXInicial + ajuste_barCode + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.3 * cm) - (alturaEtiqueta * linha)
                )
            PDF.drawString(
                x = margemXInicial + ajuste_cod + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.55 * cm) - (alturaEtiqueta * linha), 
                text=cod
                )
            PDF.drawString(
                x = margemXInicial + ajuste_preco + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.9 * cm) - (alturaEtiqueta * linha), 
                text='R$ ' + preco
                )

    PDF.showPage()
    PDF.save()

def main(args):

    '''
    Esta função tem como objetivo executar todo o escopo do algoritmo.

    É passado os argumentos do console para ter seu conteúdo separado para ser utilizado no decorrer do fluxo.
    '''

    # imprimindo processo no console
    print('\n### Iniciando Processo das Etiquetas ###\n')

    # setando uma variável com todo o conteúdo do JSON
    carrJSON = json.loads(args[1])
    # imprimindo processo no console
    print('\t* JSON:', carrJSON)
    
    # setando uma variável com o id do cliente por meio do arg
    cliente = json.loads(args[2])
    # imprimindo processo no console
    print('\t* Cliente:', cliente)

    # setando uma variável com o total de etiquetas a serem geradas
    qtd_Total_etiquetas = carrJSON["total"]
    # imprimindo processo no console
    print('\t* Total de Etiquetas:', qtd_Total_etiquetas)
    
    # setando um array com todos os produtos do JSON
    produtos = carrJSON["prod"]
    # imprimindo processo no console
    print('\t* Total de produtos:', len(produtos))
    
    # criando um array para embarcar cada conteúdo da etiqueta
    lista_produtos = []
    
    # laço de repetição com objetivo de percorrer todos os produtos informados no JSON e criando um objeto com as informações 
    for item in produtos:
        # imprimindo processo no console
        print(item)
        
        # adicionando objeto com as informações na lista de produtos
        lista_produtos.append(
            # criando o objeto com as informações selecionadas do JSON
            Entidade(
                desc = item['pro_desc'],
                barcode = item['cod_bar'],
                cod = item['cod_bar'],
                valor = item['pro_vlr'],
                qtd = item['qtd']
            )
        )
    
    # imprimindo processo no console
    print('\n\t* Vetor de Objetos criados:', lista_produtos)

    # definindo todos os ajustes referentes à impressão da página da etiqueta (obtido no proprio site da PIMACO)
    
    # dimensão vertical da folha
    tamanhoX = 21.0 * cm
    # dimensão horizontal da folha
    tamanhoY = 29.7 * cm

    # dimensão da margem superior
    margemSuperior = 1.07 * cm
    # dimensão da margem lateral (esquerda)
    margemLateral = 0.45 * cm

    # dimensão da altura da própria etiqueta em questão
    alturaUtilEtiqueta = 2.12 * cm
    # dimensão da largura da própria etiqueta em questão
    larguraUtilEtiqueta = 3.82 * cm
    
    # criando o PDF passando todos os argumentos para facilitar a manipulação posteriormente
    PDF = constituir(
        arquivo = 'etiqueta.pdf', 
        pagesize = (tamanhoX, tamanhoY), 
        margemX = margemLateral, 
        tamHorizontal = tamanhoX, 
        margemY = margemSuperior, 
        tamanhoVertical = tamanhoY,
        larguraEtiqueta = larguraUtilEtiqueta,
        alturaEtiqueta = alturaUtilEtiqueta,
        imprimirGrade = True
        )

    # plotando todas as informações no documento
    plotar(
        PDF,
        margemXInicial = margemLateral,
        tamanhoVertical = tamanhoY,
        margemYInicial = margemSuperior,
        larguraEtiqueta = larguraUtilEtiqueta,
        alturaEtiqueta = alturaUtilEtiqueta
        )

if __name__ == '__main__':

    '''
    Esta função tem como objetivo  chamar o programa principal, passando os argumentos informados via console.

    argv[1] = Conteúdo JSON
    argv[2] = idCliente

    EX: python3 script.py '{ "prod":[ { "pro_desc":"888888888 ALCON CLUB ALIM EXTRUS 500G", "cod_bar":1878, "pro_un":"KG", "pro_vlr":"110.000", "qtd":5 }, { "pro_desc":"ADORE SNACKS CAES MINI/FILHOTE 80G", "cod_bar":3013, "pro_un":"UN", "pro_vlr":"3.970", "qtd":3 }, { "pro_desc":"ADORE SNACKS GATOS BOLAS DE PELOS 80G", "cod_bar":3012, "pro_un":"UN", "pro_vlr":"6.250", "qtd":7 }, { "pro_desc":"ALCON BOTTON FISH 50G", "cod_bar":1894, "pro_un":"PT", "pro_vlr":"6.690", "qtd":2 }, { "pro_desc":"BANHEIRO CAT TOILETTE 56X40X38CM - 96301", "cod_bar":3790, "pro_un":"UN", "pro_vlr":"104.000", "qtd":7 } ], "config":{ "pageWidith":29.7, "pageHeight":21, "marginLeft":0.7, "marginRight":0.3, "barCodeBase":"pro_cod_pro", "cols":3, "fontSize":7 }, "total":24 }' 1236

    E como resposta, é criado um arquivo PDF com todas as etiquetas referentes ao JSON.
    '''

    # chamando o programa principal, passando os args 
    main(sys.argv)
