import PySimpleGUI as sg
from datetime import datetime

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome',size=(10,0)), sg.Input(size=(30,0),key='Nome')],
            [sg.Text('Sobrenome',size=(10,0)), sg.Input(size=(30,0),key='Sobrenome')],
            [sg.Text('CPF',size=(10,0)), sg.Input(size=(30,0),key='CPF')],
            [sg.Text('Data de Nascimento (dd/mm/aaaa)',size=(10,0)), sg.Input(size=(30,0),key='Data_de_Nascimento')],
            [sg.Button('Salvar Dados')],
            [sg.Output(size=(40,20))]
        ]
        # Janela
        self.janela = sg.Window('Informações do Candidato').layout(layout)
        # Calculo idade



    def Iniciar(self):

        while True:
            # Extrair os dados da tela

            self.Button, self.values = self.janela.Read()
            Nome = self.values['Nome']
            Sobrenome = self.values['Sobrenome']
            CPF = self.values['CPF']
            Data_de_Nascimento = self.values['Data_de_Nascimento']

            # Calculo da idade
            nova_data_nasc = datetime.strptime(Data_de_Nascimento, '%d/%m/%Y')
            data_atual = datetime.now()
            idade = ((data_atual - nova_data_nasc).days / 365.25)

            print(f'Nome: {Nome}')
            print(f'Sobrenome: {Sobrenome}')
            print(f'CPF: {CPF}')
            print(f'Data de Nascimento: {Data_de_Nascimento}')
            print(f'Idade: {idade:.0f}')

            if idade >= 18:
                print('Maior de idade')
            else:
                print('Menor de idade')





tela = TelaPython()
tela.Iniciar()
