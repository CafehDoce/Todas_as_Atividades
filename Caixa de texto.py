import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkPurple')

        layout = [
            [sg.Text ('Nome', size=(5,1)),sg.Input(size=(20,0), key='nome')],
            [sg.Text ('Mensagem', size=(8,1)), sg.Input(size=(20,0), key='mensagem')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,15))]
        ]

        self.janela = sg.Window('Escreva uma mensagem.').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            mensagem = self.values['mensagem']
            print(f'nome: {nome}')
            print(f'mensagem: {mensagem}')

tela = TelaPython()
tela.Iniciar()