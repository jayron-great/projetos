from random import randint
import PySimpleGUI as sg

lista = [randint(1, 6) for c in range(2)]

class TelaPython():
    def __init__(self):

        #layout
        layout = [
            [sg.Text(f'Maior valor: {max(lista)}')],
            [sg.Text(f'Menor valor: {min(lista)}')]
        ]
        #janela
        janela = sg.Window('Dados').layout(layout)

        #Extrair dados
        self.values = janela.read()

    def Iniciar(self):
        print(self.values)

a = TelaPython()
a.Iniciar()